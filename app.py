import streamlit as st
from src.agent.agent import create_supply_chain_agent
import pandas as pd

st.set_page_config(
    page_title="SupplyChain AI • Professional Assistant",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x150/1E88E5/FFFFFF?text=SCAI", width=120)
    st.title("SupplyChain AI")
    st.caption("Enterprise Supply Chain Copilot")
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main
st.title("📦 AI Supply Chain Assistant")
st.markdown("**Ask anything** — inventory, EOQ, forecasts, supplier risk, reorder alerts...")

if "agent" not in st.session_state:
    with st.spinner("Loading professional agent..."):
        st.session_state.agent = create_supply_chain_agent()

# Suggested prompts (professional touch)
if not st.session_state.get("messages"):
    st.info("💡 Try asking:\n"
            "• Show current inventory status\n"
            "• Calculate EOQ for Laptop\n"
            "• What should I reorder this week?")

# Chat logic (same as yours but cleaner)
for msg in st.session_state.get("messages", []):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your supply chain question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking like a Supply Chain Manager..."):
            response = st.session_state.agent.invoke({"input": prompt})
            answer = response["output"]
            st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
