import streamlit as st
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "To dispose of 19 pounds of Styrofoam, first check if local recycling centers or packaging stores like UPS and FedEx will accept it. Some locations reuse packaging materials, and websites like Earth911 or the Alliance of Foam Packaging Recyclers (AFPR) can help you find nearby drop-off points or mail-in recycling options.\n\nIf recycling isn’t available, you can break the Styrofoam into smaller pieces, place it in secure plastic bags, and throw it in the regular trash to prevent it from scattering. Never burn Styrofoam, as it releases toxic fumes, and avoid dumping it outdoors, where it can harm wildlife. \n\n Alternatively, consider offering it on platforms like Freecycle, Craigslist, or Facebook Marketplace for reuse, or donate it to local schools or art programs for creative projects. Reusing it for home insulation or future packaging can also be a practical option.",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("SAVE GPT")

# Initialize chat history
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