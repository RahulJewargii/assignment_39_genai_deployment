import os
import streamlit as st
from huggingface_hub import InferenceClient
# from openai import OpenAI

st.set_page_config(page_title="GenAI App Deployment", page_icon="AI")
st.title("GenAI App Deployment")
st.write("A simple cloud-ready GenAI application using Hugging Face Inference API.")
DEFAULT_MODEL = "deepseek-ai/DeepSeek-V3-0324"
ModelName = os.getenv("HF_MODEL", DEFAULT_MODEL)

def get_client():
    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError("HF_TOKEN is not configured.")
    return InferenceClient(api_key=token, provider="auto")

def generate_answer(prompt):
    client = get_client()
    # print("calling model:", ModelName)  
    response = client.chat.completions.create(
        model=ModelName,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful GenAI assistant. Give clear and concise answers."
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
    )
    print(response.usage)
    return response.choices[0].message.content

if "history" not in st.session_state:
    st.session_state.history = []
st.sidebar.header("Deployment Info")
st.sidebar.write(f"Model: {ModelName}")
st.sidebar.write("Provider: Hugging Face Inference API")
user_prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: Explain what a vector database is in simple words.",
    height=160,
)

if st.button("Generate Response"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Generating response..."):
                Answer = generate_answer(user_prompt)
            st.session_state.history.append((user_prompt, Answer))
        except Exception as error:
            st.error("The GenAI service could not generate a response.")
            st.code(str(error))

if st.session_state.history:
    st.subheader("Conversation")
    for question, answer in reversed(st.session_state.history):
        st.markdown("**You:** " + question)
        st.markdown("**AI:** " + answer)
        st.divider()
    # print("history length:", len(st.session_state.history))

if st.button("Clear Conversation"):
    st.session_state.history = []
    st.rerun()
    