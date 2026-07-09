import streamlit as st
from main import run_pipeline
from core.rag_engine import ask_question

# ------------------------------------
# Page Configuration
# ------------------------------------
st.set_page_config(
    page_title="AI Meeting Summarizer",
    page_icon="📝",
    layout="wide"
)

# ------------------------------------
# Custom CSS
# ------------------------------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

.main-title{
    font-size:2.6rem;
    font-weight:700;
    margin-bottom:0.2rem;
}

.subtitle{
    color:gray;
    margin-bottom:1.5rem;
}

.result-card{
    padding:1rem;
    border-radius:12px;
    background-color:#1E1E1E;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------
# Session State
# ------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# ------------------------------------
# Header
# ------------------------------------
st.markdown(
    '<div class="main-title">📝 AI Meeting Summarizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload a meeting recording or provide a YouTube link to generate transcripts, summaries, action items, and key decisions.</div>',
    unsafe_allow_html=True
)

# ------------------------------------
# Input Section
# ------------------------------------

col1, col2 = st.columns([4,1])

with col1:

    source = st.text_input(
        "Meeting Audio / Video Path or YouTube URL"
    )

with col2:

    language = st.selectbox(
        "Language",
        [
            "english",
            "hinglish"
        ]
    )

# ------------------------------------
# Process
# ------------------------------------

if st.button("🚀 Generate Meeting Report", use_container_width=True):

    if not source:
        st.warning("Please provide a meeting recording or YouTube URL.")
        st.stop()

    with st.spinner("Analyzing meeting..."):

        st.session_state.result = run_pipeline(
            source,
            language
        )

# ------------------------------------
# Results
# ------------------------------------

if st.session_state.result:

    result = st.session_state.result

    st.success("Meeting analysis completed successfully.")

    st.markdown(f"# 📌 {result['title']}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📝 Summary",
            "📋 Action Items",
            "✅ Key Decisions",
            "⚠ Risks / Open Issues",
            "📄 Transcript"
        ]
    )

    with tab1:

        st.subheader("Meeting Summary")
        st.write(result["summary"])

    with tab2:

        st.subheader("Action Items")
        st.write(result["action_items"])

    with tab3:

        st.subheader("Key Decisions")
        st.write(result["key_decisions"])

    with tab4:

        st.subheader("Risks / Open Issues")
        st.write(result["open_questions"])

    with tab5:

        st.write(result["transcript"])

    st.divider()

    st.subheader("💬 Ask Questions About This Meeting")

    st.caption("Bonus Feature powered by RAG")

    question = st.text_input(
        "Ask anything from this meeting...",
        key="chat_input"
    )

    if question:

        with st.spinner("Thinking..."):

            answer = ask_question(
                result["rag_chain"],
                question
            )

        st.markdown("### 🤖 AI Assistant")

        st.write(answer)
