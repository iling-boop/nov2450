import streamlit as st
import random
import time

def response_generator():
    response = random.choice(
        [
            "Sorry we ran out of OpenAI API quota. Please consider donating to my project. Thank you! ",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("SAVE Identification Bot")
st.write("Identify trash by talking a photo and copying it to the SAVE GPT.")

camera_photo = st.camera_input("Take a photo")


# Show title and description.
st.title("Photo ID")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)


# Let the user upload a file via `st.file_uploader`.
uploaded_file = st.file_uploader(
    "Upload a photo here"
)
if uploaded_file is not None:
    st.success("Photo uploaded successfully!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




