import streamlit as st
from src.financial_assistant import search_policy

st.title("Financial Knowledge Assistant")

question = st.text_input("Enter your question")

if st.button("Search Policy"):

    if question.strip():

        answer = search_policy(question)

        st.subheader("Answer")

        st.write(answer)

    else:
        st.warning("Please enter a question.")