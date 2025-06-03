# InfernalCV

## The Introduction
A Streamlit application that delivers brutally honest and sarcastically witty critique of your carefully crafted Curriculum Vitae, while providing actionable steps you can take to take your Resume Game to the next level! Supports a variety of modalities - from locally-hosted Ollama-powered models for the privacy possum, to free SOTA models.

## 🌟 Features

*   **📄 Versatile Resume Upload:** Supports PDF, DOCX, and TXT file formats.
*   **🧠 Multiple LLM Choices:** Select from a range of powerful Large Language Models:
    *   Local models via Ollama (e.g., Qwen, Llama3, Deepseek, Gemma)
    *   Google Gemini models (e.g., Gemini 2.0 Flash Lite)
    *   Models via OpenRouter (e.g., DeepSeek R1, Mistral)
*   **🎯 Targeted Feedback:** Specify your target job role for tailored advice.
*   **😂 Humorous Roasting:** Get a witty, sarcastic, and brutally honest (but funny!) take on your resume.
*   **🛠️ Constructive Criticism:** Receive actionable feedback and concrete suggestions for improvement.
*   **✨ Interactive UI:** Easy-to-use interface built with Streamlit.

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.8+
*   **`uv` (Recommended for fast environment and package management):** Install `uv` by following the instructions at [Astral's `uv` documentation](https://docs.astral.sh/uv/getting-started/installation/).
    *   Alternatively, you can use standard Python `venv` and `pip`.
*   Access to API keys for Google Gemini and/or OpenRouter (if you plan to use those models).
*   Ollama installed and running if you want to use local models (see [Ollama Setup](#ollama-setup)).

