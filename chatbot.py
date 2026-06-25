from langchain_groq import ChatGroq

from langchain_classic.chains import RetrievalQA

from langchain_core.prompts import PromptTemplate

import os

from dotenv import load_dotenv


load_dotenv()



def create_llm():

    print("Loading Groq model...")


    llm = ChatGroq(

        model="llama-3.1-8b-instant",

        temperature=0.1,

        max_tokens=500,

        api_key=os.getenv("GROQ_API_KEY")

    )


    return llm





def create_qa_chain(db):


    llm = create_llm()



    prompt_template = """

You are a helpful PDF assistant.

Answer the question only using the provided PDF context.

Give a clear explanation.

For theory questions:
- Give definition
- Explain each important point
- Use simple language

Do not add information outside the PDF.

If the answer is not available in the PDF, say:

"I cannot find this information in the PDF."


Context:

{context}


Question:

{question}


Answer:

"""



    prompt = PromptTemplate(

        template=prompt_template,

        input_variables=[

            "context",

            "question"

        ]

    )



    qa_chain = RetrievalQA.from_chain_type(


        llm=llm,


        retriever=db.as_retriever(

            search_kwargs={

                "k":5

            }

        ),


        chain_type="stuff",


        chain_type_kwargs={

            "prompt": prompt

        },


        return_source_documents=True

    )


    return qa_chain