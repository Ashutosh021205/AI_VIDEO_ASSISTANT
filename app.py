import streamlit as st
from main import run_pipeline
from core.rag_engine import ask_question

st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎥",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.main-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.result-card {
    padding: 1rem;
    border-radius: 12px;
    background-color: #1E1E1E;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Session State
# ----------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# ----------------------------
# Header
# ----------------------------
st.markdown(
    '<div class="main-title">🎥 AI Video Assistant</div>',
    unsafe_allow_html=True
)

# ----------------------------
# Input Section
# ----------------------------
col1, col2 = st.columns([4, 1])

with col1:
    source = st.text_input(
        "YouTube URL or Local File Path"
    )

with col2:
    language = st.selectbox(
        "Language",
        ["english", "hinglish"]
    )

# ----------------------------
# Process Button
# ----------------------------
if st.button("🚀 Process Video", use_container_width=True):

    if not source:
        st.warning("Please enter a source.")
        st.stop()

    with st.spinner("Processing video..."):
        st.session_state.result = run_pipeline(
            source,
            language
        )

# ----------------------------
# Results
# ----------------------------
if st.session_state.result:

    result = st.session_state.result

    st.success("Processing Complete")

    st.markdown(f"## 📌 {result['title']}")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Summary",
            "✅ Actions",
            "🔑 Decisions",
            "❓ Questions"
        ]
    )

    with tab1:
        st.write(result["summary"])

    with tab2:
        st.write(result["action_items"])

    with tab3:
        st.write(result["key_decisions"])

    with tab4:
        st.write(result["open_questions"])

    with st.expander("📄 Full Transcript"):
        st.write(result["transcript"])

    st.divider()

    st.subheader("💬 Chat with Meeting")

    question = st.text_input(
        "Ask a question about the meeting",
        key="chat_input"
    )

    if question:
        with st.spinner("Thinking..."):
            answer = ask_question(
                result["rag_chain"],
                question
            )

        st.markdown("### 🤖 Assistant")
        st.write(answer)