import random
import time
import streamlit as st
from openai import OpenAI

def default_response_generator():
    response = random.choice(
        [
            "Sorry we ran out of OpenAI API quota. Please consider donating to my project. Thank you! ",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("SAVE via GPT")
open_ai_key = st.secrets["OPENAI_API_KEY"]["key"]
client = OpenAI(api_key=open_ai_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type any question about recycling / upcycling..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
                )
            response = st.write_stream(stream)
        except:
            response = st.write_stream(default_response_generator)

    st.session_state.messages.append({"role": "assistant", "content": response})

