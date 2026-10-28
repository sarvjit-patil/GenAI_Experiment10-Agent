import logging
import os
import re
from duckduckgo_search import DDGS
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

logger = logging.getLogger(__name__)


from dotenv import load_dotenv

# Load private configuration from the local .env file
load_dotenv()

# Verify that the Gemini API key is available
if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError(
        "GOOGLE_API_KEY is missing. Add it to your local .env file."
    )

def validate_topic(topic):
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("Please enter a valid topic.")

    return topic.strip()




STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "in", "on",
    "at", "for", "to", "of", "and", "or", "with", "by", "from",
    "latest", "recent", "new", "developments", "updates", "news",
    "about", "what", "how", "best", "current", "2026"
}

from ddgs import DDGS



def search_web(topic: str) -> str:
    """Search the web and return article details."""

    if not topic or not topic.strip():
        raise ValueError("Please enter a topic.")

    topic = topic.strip()
    collected = {}

    queries = [
        topic,
        f"{topic} latest news",
        f"{topic} research and developments",
    ]

    for query in queries:
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=5)

                for result in results or []:
                    title = result.get("title", "").strip()
                    url = result.get("href", "").strip()
                    body = result.get("body", "").strip()

                    if not title and not body:
                        continue

                    key = url or title

                    if key and key not in collected:
                        collected[key] = (
                            f"Title: {title}\n"
                            f"URL: {url}\n"
                            f"Snippet: {body}"
                        )

        except Exception:
            logger.exception("Search failed for query: %s", query)

    if not collected:
        raise RuntimeError(
            "No search results were returned. Check your connection "
            "and try again."
        )

    return "\n\n".join(list(collected.values())[:10])

def summarize_results(topic, search_results):
    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Gemini API key is missing. Configure GOOGLE_API_KEY."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    prompt =  ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a careful research assistant. "
        "Answer only using the supplied search results. "
        "First check that the results are relevant to the requested topic. "
        "Ignore unrelated results. Never invent facts, dates, or sources. "
        "If there is insufficient relevant information, say so clearly. "
        "Otherwise, provide exactly three concise bullet points."
    ),
    (
        "human",
        "Requested topic: {topic}\n\n"
        "Search results:\n{search_results}\n\n"
        "Summarize only information relevant to the requested topic."
    )
])

    chain = prompt | llm

    response = chain.invoke({
        "topic": topic,
        "search_results": search_results
    })

    return response.content.strip()


def format_three_bullets(text):
    """Normalize model output and require exactly three bullet items."""

    items = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        line = re.sub(r"^(?:[-*•]|\d+[.)])\s*", "", line)

        if line:
            items.append(line)

    if len(items) != 3:
        raise ValueError(
            f"Expected 3 bullet points, but received {len(items)}. "
            "Please retry the request."
        )

    return "\n".join(f"- {item}" for item in items)


def run_research_agent(topic):
    topic = validate_topic(topic)

    logger.info("Research request received")

    results = search_web(topic)
    summary = summarize_results(topic, results)

    return format_three_bullets(summary)