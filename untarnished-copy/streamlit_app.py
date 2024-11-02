import streamlit as st


intro_page = st.Page(
    page = "sub_groups/streamlit_intro.py",
    title = "Welcome to the SAVE Bot!",
    default = True,
)

about_page = st.Page(
    page = "sub_groups/streamlit_quiz.py",
    title = "Sorting Quiz",
)

project_chat_page = st.Page(
    page = "sub_groups/streamlit_chat.py",
    title = "Chat Bot",
)

project_photo_page = st.Page(
    page = "sub_groups/streamlit_photo.py",
    title = "SAVE ID Bot"
)


pg = st.navigation(pages=[intro_page, about_page, project_chat_page, project_photo_page])


st.sidebar.write("_Made with :red[<3] by Isabelle Ling_")

pg.run()