from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from src.exception import CustomeExceptionClass
import sys
from utils import *
<<<<<<< HEAD
try:
    st.title('My Chatbot')
=======

try:
    from src.components.preprocessing import docs  
    context = "\n".join([doc.page_content for doc in docs]) 
except Exception as e:
    raise CustomeExceptionClass(e, sys)
try:
    st.title("My Chatbot")
>>>>>>> 707750bd44022204c9b456671eb1e98c236be02b
    st.subheader("Chatbot with Langchain, ChatGPT, Pinecone, and Streamlit")

    if 'responses' not in st.session_state:
        st.session_state['responses'] = ["How can I assist you?"]

    if 'requests' not in st.session_state:
        st.session_state['requests'] = []
<<<<<<< HEAD
    llm = ChatOpenAI(model_name = 'gpt-3.5-turbo',openai_api_key='')
    if 'buffer_memory' not in st.session_state:
        st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)


    system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context, 
    and if the answer is not contained within the text below, say 'I don't know'""")


    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

    prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

    conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)
except Exception as e:
    raise CustomeExceptionClass(e,sys)
=======

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="")


    if 'buffer_memory' not in st.session_state:
        st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)

    system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context, 
    and if the answer is not contained within the text below, say 'I don't know'""")

    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

    prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])
    conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)
except Exception as e:
            raise CustomeExceptionClass(e,sys)
>>>>>>> 707750bd44022204c9b456671eb1e98c236be02b

try:
    response_container = st.container()
    textcontainer = st.container()
<<<<<<< HEAD

=======
>>>>>>> 707750bd44022204c9b456671eb1e98c236be02b
    with textcontainer:
        query = st.text_input("Query: ", key="input")
        if query:
            with st.spinner("typing..."):
<<<<<<< HEAD
                conversation_string = get_conversation_string()
                refined_query = query_refiner(conversation_string, query)
                st.subheader("Refined Query:")
                st.write(refined_query)
                context = find_match(refined_query) 
                response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
            st.session_state.requests.append(query)
            st.session_state.responses.append(response) 
    with response_container:
        if st.session_state['responses']:

=======
                response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
            st.session_state.requests.append(query)
            st.session_state.responses.append(response)
    with response_container:
        if st.session_state['responses']:
>>>>>>> 707750bd44022204c9b456671eb1e98c236be02b
            for i in range(len(st.session_state['responses'])):
                message(st.session_state['responses'][i],key=str(i))
                if i < len(st.session_state['requests']):
                    message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')
<<<<<<< HEAD
except Exception as e:
    raise CustomeExceptionClass(e,sys)
=======

except Exception as e:
            raise CustomeExceptionClass(e,sys)

>>>>>>> 707750bd44022204c9b456671eb1e98c236be02b
