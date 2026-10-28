import logging
import time

import streamlit as st

from agent import run_research_agent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 AI Research Agent")
st.write(
    "Enter a topic to search the web and generate "
    "a concise research brief using Google Gemini."
)

topic = st.text_input(
    "Enter your research topic",
    placeholder="e.g. Artificial Intelligence in Education"
)

if st.button("Search and Summarize", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        start_time = time.perf_counter()

        try:
            with st.spinner(
                "Searching the web and summarizing with Gemini..."
            ):
                logger.info("Research request started")

                brief = run_research_agent(topic)

            elapsed = time.perf_counter() - start_time

            logger.info(
                "Research request completed in %.2f seconds",
                elapsed
            )

            st.subheader("Research Brief")
            st.markdown(brief)
            st.caption(f"Request completed in {elapsed:.2f} seconds.")

        except Exception:
            elapsed = time.perf_counter() - start_time

            logger.exception(
                "Research request failed after %.2f seconds",
                elapsed
            )

            st.error(
                "The request failed. Check the application logs, "
                "API configuration, and internet connection, "
                "then try again."
            )