import gradio as gr

from pdf_loader import load_pdf
from vector_store import create_vector_db
from chatbot import create_qa_chain


qa_chain = None



def upload_pdf(file):

    global qa_chain


    if file is None:

        return "Please upload a PDF file"



    chunks = load_pdf(file.name)


    db = create_vector_db(chunks)


    qa_chain = create_qa_chain(db)


    return "PDF processed successfully. You can ask questions now."





def ask_question(question, history):

    global qa_chain



    if qa_chain is None:


        history.append(
            {
                "role": "user",
                "content": question
            }
        )


        history.append(
            {
                "role": "assistant",
                "content": "Please upload a PDF first."
            }
        )


        return history, ""





    response = qa_chain.invoke(
        {
            "query": question
        }
    )



    answer = response["result"]



    pages = set()



    for doc in response["source_documents"]:


        page = doc.metadata.get(
            "page",
            None
        )


        if page is not None:

            pages.add(page + 1)




    if pages:


        answer += "\n\nSources: "

        answer += ", ".join(

            [
                f"Page {p}"
                for p in sorted(pages)
            ]

        )





    history.append(

        {
            "role": "user",
            "content": question
        }

    )



    history.append(

        {
            "role": "assistant",
            "content": answer
        }

    )


    return history, ""








custom_css = """

body {

    background:#f4f6f9;

}


#title {

    text-align:center;

    font-size:30px;

    font-weight:600;

}


#chatbot {

    height:520px;

}



button {

    border-radius:8px !important;

}



textarea {

    border-radius:10px !important;

}

"""







with gr.Blocks(

    css=custom_css,

    theme=gr.themes.Soft()

) as app:



    gr.Markdown(

        """
        <div id="title">
        PDF AI Assistant
        </div>

        <center>
        Ask questions from your documents using AI
        </center>
        """

    )





    with gr.Row():



        with gr.Column(scale=1):


            gr.Markdown(

                "### Document Upload"

            )



            pdf = gr.File(

                label="Select PDF",

                file_types=[".pdf"]

            )



            upload_btn = gr.Button(

                "Process PDF",

                variant="primary"

            )



            status = gr.Textbox(

                label="Status",

                interactive=False

            )





        with gr.Column(scale=2):


            gr.Markdown(

                "### Conversation"

            )



            chatbot = gr.Chatbot(

                label="Assistant",

                elem_id="chatbot"

            )



            question = gr.Textbox(

                placeholder="Ask a question about your PDF",

                show_label=False

            )





            with gr.Row():


                send_btn = gr.Button(

                    "Send",

                    variant="primary"

                )


                clear_btn = gr.Button(

                    "Clear"

                )







    upload_btn.click(

        upload_pdf,

        inputs=pdf,

        outputs=status

    )





    send_btn.click(

        ask_question,

        inputs=[question, chatbot],

        outputs=[chatbot, question]

    )





    question.submit(

        ask_question,

        inputs=[question, chatbot],

        outputs=[chatbot, question]

    )





    clear_btn.click(

        lambda: [],

        outputs=chatbot

    )







app.launch()