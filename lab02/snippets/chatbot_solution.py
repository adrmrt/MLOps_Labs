import streamlit as st
from transformers import pipeline

def message_generator(m: str):
    for char in m:
        yield char

st.title("Chatbot")

qwen = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B", max_new_tokens=100)

prompt = \
"""
<INSTRUCTION>
You are a helpful bot and are answering all questions the human has. 
You only answer the question and do not provide any additional information. 
You are not allowed to ask questions.
</INSTRUCTION>

<QUESTION>
{question}
</QUESTION>

<ANSWER>
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(
            message["content"]
        )  # st.markdown interprets and renders its input as markdown

# React to user input
if inp := st.chat_input("Say something!"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(inp)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": inp})

    # get response
    response=qwen(prompt.format(question=inp).strip())[0]['generated_text']
    # get first entry between ANSWER tags
    response=response.split("<ANSWER>")[1].strip().split("</ANSWER>")[0]

    # Display parrots response in chat message container
    with st.chat_message("🦜"):
        st.write_stream(message_generator(response))

    # Add parrot's response to chat history
    st.session_state.messages.append({"role": "parrot", "content": response})

