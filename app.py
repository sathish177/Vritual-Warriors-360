import streamlit as st
from agent import agent

st.title("🛠️ AutoDockAgent Web Interface")

user_input = st.text_input("Enter a command")

if st.button("Run"):
    result = agent.run(user_input)
    st.success(result.output)