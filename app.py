import streamlit as st
from data_preprocessing import load_and_preprocess_data
from langchain_core.output_parsers import StrOutputParser
from build_vector import building_vector_store
from retrieve_documents import retrieve_documents
from model import model
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

@st.cache_data
def load_data():
    return load_and_preprocess_data('scraped_data.json')

@st.cache_resource
def load_model():
    return model()

@st.cache_resource(show_spinner="Building Vector Datastore...")
def get_vector_store(documents):
        return building_vector_store(documents)

template = """Always Greet the user. Use the following pieces of context to answer the question at the end.
Try to give meaningful answers to all the questions related to Jobsflow.

If the context does not mention anything about the question. 
Reply with:
"I am sorry, but I couldn't find the information you are looking for. If you have another question regarding Jobsflow.ai, feel free to ask!"

If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.

Context: {context}

Question: {question}
"""

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

custom_rag_prompt = PromptTemplate.from_template(template)


def ui():
    st.title("Chat with Jobsflow.ai website")
    st.write("Ask any question about the content on the website.")

    llm = load_model()
    documents = load_data()
        
    vector_store = get_vector_store(documents)
    retriever = retrieve_documents(vector_store)

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    def clear_input():
        st.session_state.user_input = st.session_state.widget
        st.session_state.widget = ""

    user_input = st.text_input("You: ", key="widget", on_change=clear_input, placeholder="Type your question here...")
    user_input = st.session_state.user_input

    if user_input:
        with st.spinner("Generating response..."):
            rag_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | custom_rag_prompt
                | llm
                | StrOutputParser()
            )

            response = rag_chain.invoke(user_input)
            st.session_state.conversation.append({"user": user_input, "bot": response})

    if st.session_state.conversation:
        for exchange in st.session_state.conversation:
            st.write(f"You: {exchange['user']}")
            st.write(f"Support Agent: {exchange['bot']}")

if __name__ == "__main__":
    ui()
