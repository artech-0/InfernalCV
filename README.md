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

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/artech-0/InfernalCV.git
    cd InfernalCV
    ```
    
2.  **Configure API Keys:**
    *   Create a file named `.env` in the root directory of the project.
    *   Add your API keys to this file. **Do not commit this file to Git!**
        ```env
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        OPENROUTER_API_KEY="YOUR_OPENROUTER_API_KEY_HERE"
        ```
    *   Ensure `.env` is listed in your `.gitignore` file.
3.  **Create and activate a virtual environment and install the dependencies**

    **Using `uv` (Recommended):**
    ```bash
    uv run app.py
    ```
### Ollama Setup (for Local Models)

1.  **Install Ollama:** Follow the instructions at [ollama.com](https://ollama.com/).
2.  **Pull desired models:** Open your terminal and pull the models you want to use from the selection in the app. For example:
    ```bash
    ollama pull qwen:1.7b
    ollama pull llama3.1:8b
    ollama pull deepseek-r1
    # ... and any others you plan to use
    ```
3. ```bash
   ollama serve
   ```

## 🎮 Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  **Open the application in your browser** (usually `http://localhost:8501`).

3.  **Interact with the app:**
    *   **Upload your resume:** Use the file uploader (supports PDF, DOCX, and TXT).
    *   **Select an Inference Model:** Choose your preferred LLM from the dropdown menu.
    *   **Enter Target Job Role:** Type in the job title or field you are aiming for.
    *   **Click "Analyze!"** (or similar button text).

4.  Wait for the AI to analyze your resume and set it on fire !

---

## 🛠️ Technologies Used

*   **Python**
*   **`uv`:** For fast Python packaging and environment management.
*   **Streamlit:** For the web application interface.
*   **Ollama:** For running local LLMs.
*   **Google Gemini API:** For accessing Google's Generative AI models.
*   **OpenRouter API:** For accessing a variety of LLMs through a unified interface.
*   **PyPDF2:** For PDF text extraction.
*   **python-docx:** For DOCX text extraction.
*   **python-dotenv:** For managing environment variables.
*   **ruff:** For linting and code quality checks.
