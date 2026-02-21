import streamlit as st
from src.agent.agent import create_supply_chain_agent

st.set_page_config(page_title="Supply Chain Assistant", page_icon="📦")
st.title("📦 AI Supply Chain Assistant")

if "agent" not in st.session_state:
    with st.spinner("Loading agent..."):
        st.session_state.agent = create_supply_chain_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about inventory, calculations, or real-time data..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.invoke({"input": prompt})
            assistant_response = response["output"]
            st.markdown(assistant_response)
    
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
