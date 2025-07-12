import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from main import answer_query

st.title("RAG Q&A: Loan Analysis Assistant")

query = st.text_input("Ask your question:")
if query:
    response = answer_query(query)
    st.markdown(response)
