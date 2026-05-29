import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/run"

st.set_page_config(page_title="Multi-Agent Business AI", layout="wide")

st.title("🤖 Multi-Agent Business AI System")

st.markdown("Enter your business problem and get AI-powered strategy + execution")

# Input
user_input = st.text_input("Enter your query:")

if st.button("Run AI System"):
    if not user_input.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Running multi-agent system..."):
            try:
                response = requests.post(API_URL, json={"query": user_input})
                data = response.json()

                if data["status"] == "success":
                    result = data["data"]

                    # Display Plan
                    st.subheader("📌 Plan")
                    for i, step in enumerate(result["plan"], 1):
                        st.write(f"{i}. {step}")

                    # Display Results
                    st.subheader("⚙️ Execution Results")
                    for item in result["results"]:
                        st.markdown(f"**Task:** {item['task']}")
                        st.markdown(f"**Result:** {item['result']}")
                        st.markdown("---")

                else:
                    st.error(data["message"])

            except Exception as e:
                st.error(f"Error: {str(e)}")