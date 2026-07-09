from dotenv import load_dotenv

from utils.audio_processor import process_input

from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)

from core.rag_engine import (
    build_rag_chain,
    ask_question,
)

# -------------------------------------------------
# Load Environment Variables
# -------------------------------------------------

load_dotenv()


# -------------------------------------------------
# Main Pipeline
# -------------------------------------------------

def run_pipeline(source: str, language: str = "english") -> dict:
    """
    AI Meeting Summarizer Pipeline

    Flow:
    Input Audio/Video
            ↓
    Audio Processing
            ↓
    Speech-to-Text
            ↓
    Meeting Title
            ↓
    Meeting Summary
            ↓
    Action Items
            ↓
    Key Decisions
            ↓
    Open Questions
            ↓
    RAG Chat (Bonus)
    """

    print("\n========== AI Meeting Summarizer ==========\n")

    # ------------------------------------------
    # Process Audio
    # ------------------------------------------

    chunks = process_input(source)

    # ------------------------------------------
    # Speech Recognition
    # ------------------------------------------

    transcript = transcribe_all(
        chunks,
        language
    )

    print("\nTranscript generated successfully.\n")

    # ------------------------------------------
    # Generate Meeting Insights
    # ------------------------------------------

    print("Generating meeting title...")

    title = generate_title(transcript)

    print("Generating meeting summary...")

    summary = summarize(transcript)

    print("Extracting action items...")

    action_items = extract_action_items(transcript)

    print("Extracting key decisions...")

    key_decisions = extract_key_decisions(transcript)

    print("Extracting open questions...")

    open_questions = extract_questions(transcript)

    # ------------------------------------------
    # Build RAG Chain (Optional Feature)
    # ------------------------------------------

    print("Building Meeting Knowledge Base...")

    rag_chain = build_rag_chain(transcript)

    print("\nMeeting analysis completed.\n")

    # ------------------------------------------
    # Return Results
    # ------------------------------------------

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": key_decisions,
        "open_questions": open_questions,
        "rag_chain": rag_chain,
    }


# -------------------------------------------------
# CLI Entry
# -------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print(" AI Meeting Summarizer ")
    print("=" * 60)

    source = input(
        "\nEnter Meeting Audio/Video Path or YouTube URL:\n> "
    ).strip()

    language = (
        input(
            "\nLanguage (english / hinglish): "
        ).strip()
        or "english"
    )

    result = run_pipeline(
        source,
        language,
    )

    print("\n" + "=" * 60)

    print(f"\n📌 Meeting Title\n{result['title']}")

    print("\n" + "=" * 60)

    print("\n📝 Meeting Summary\n")
    print(result["summary"])

    print("\n" + "=" * 60)

    print("\n📋 Action Items\n")
    print(result["action_items"])

    print("\n" + "=" * 60)

    print("\n✅ Key Decisions\n")
    print(result["key_decisions"])

    print("\n" + "=" * 60)

    print("\n⚠ Open Questions / Pending Discussions\n")
    print(result["open_questions"])

    print("\n" + "=" * 60)

    # ------------------------------------------
    # Bonus Feature
    # ------------------------------------------

    print("\n💬 Ask Questions About This Meeting")
    print("Type 'exit' anytime to quit.\n")

    rag_chain = result["rag_chain"]

    while True:

        question = input("You: ").strip()

        if question.lower() in ["exit", "quit", "q"]:
            print("\n👋 Thank you for using AI Meeting Summarizer!")
            break

        if not question:
            continue

        answer = ask_question(
            rag_chain,
            question,
        )

        print(f"\n🤖 Assistant:\n{answer}\n")
