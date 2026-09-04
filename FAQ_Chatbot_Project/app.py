from importlib import import_module

st = import_module("streamlit")
from chatbot import get_response

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 FAQ Chatbot")
st.caption("NLP-powered FAQ matching using TF-IDF and cosine similarity")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a question about your account, order, payment, delivery...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    answer, score, matched = get_response(question)

    with st.chat_message("assistant"):
        st.write(answer)
        if matched:
            st.caption(f"Similarity: {score:.2f} | Matched FAQ: {matched}")

    st.session_state.messages.append({"role": "assistant", "content": answer})
