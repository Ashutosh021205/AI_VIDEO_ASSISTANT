"""
Meeting Information Extractor

Extracts:
1. Action Items
2. Key Decisions
3. Open Questions / Follow-up Items
"""

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import os


# ---------------------------------------------------
# Initialize LLM
# ---------------------------------------------------

def get_llm():
    return ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0.0
    )


# ---------------------------------------------------
# Generic Prompt Chain Builder
# ---------------------------------------------------

def build_chain(system_prompt: str):
    llm = get_llm()

    return (
        RunnablePassthrough()
        | RunnableLambda(lambda x: {"text": x})
        | ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{text}")
            ]
        )
        | llm
        | StrOutputParser()
    )


# ---------------------------------------------------
# Action Items
# ---------------------------------------------------

def extract_action_items(transcript: str) -> str:
    """
    Extract all action items from the meeting.
    """

    prompt = """
You are an expert AI Meeting Assistant.

Analyze the meeting transcript and identify ALL action items.

For each action item provide:

1. Owner
2. Task
3. Deadline
4. Priority (High / Medium / Low)

Format exactly like this:

1.
Owner:
Task:
Deadline:
Priority:

If Owner or Deadline is missing, write:
Not Specified

If no action items are present, return ONLY:

No action items found.
"""

    chain = build_chain(prompt)

    return chain.invoke(transcript)


# ---------------------------------------------------
# Key Decisions
# ---------------------------------------------------

def extract_key_decisions(transcript: str) -> str:
    """
    Extract all finalized decisions.
    """

    prompt = """
You are an expert AI Meeting Assistant.

Read the meeting transcript carefully.

Identify every decision finalized during the meeting.

For each decision include:

1. Decision
2. Reason (if discussed)
3. Impact (if mentioned)

Format:

1.
Decision:
Reason:
Impact:

If information is unavailable write:

Not Specified

If no decisions exist return ONLY:

No key decisions found.
"""

    chain = build_chain(prompt)

    return chain.invoke(transcript)


# ---------------------------------------------------
# Open Questions / Follow-ups
# ---------------------------------------------------

def extract_questions(transcript: str) -> str:
    """
    Extract pending discussions and unresolved questions.
    """

    prompt = """
You are an expert AI Meeting Assistant.

From the transcript identify:

• Unanswered Questions
• Pending Discussions
• Risks
• Blockers
• Follow-up Topics

Format:

1.
Question / Issue:
Reason:
Owner (if mentioned):

If Owner is unavailable write:

Not Specified

If no pending items exist return ONLY:

No open questions found.
"""

    chain = build_chain(prompt)

    return chain.invoke(transcript)
