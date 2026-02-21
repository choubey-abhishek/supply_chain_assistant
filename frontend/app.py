import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Backend ka URL (production mein replace kar)

st.set_page_config(page_title="Supply Chain Assistant", page_icon="📦")
st.title("📦 AI Supply Chain Assistant (Frontend)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(f"{API_URL}/chat", json={"message": prompt})
                if response.status_code == 200:
                    assistant_response = response.json()["response"]
                else:
                    assistant_response = f"Error: {response.text}"
            except Exception as e:
                assistant_response = f"Connection error: {str(e)}"
        st.markdown(assistant_response)

    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
