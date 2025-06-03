import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from config import model_map
from llm_services import generate_and_parse_answer
from file_handler import extract_text


st.title("AI Resume Roaster")
st.divider()
st.badge("Resume Review")
st.markdown("Upload Your Resume and AI powered roasting")
model = st.selectbox(
    "Which inference model do you want to run?",
    (
        "qwen3 - 1.7b",
        "qwen3 - 4b",
        "Llama3 - 8b",
        "Deepseek-r1 8b",
        "Gemma3 - 27B",
        "Gemini 2.0 Flash Lite",
        "DeepSeek R1 - 0528",
        "Mistral",
    ),
    index=None,
    placeholder="Select Inference Model...",
)

uploaded_file = st.file_uploader(
    "Upload your resume here (PDF, docx and txt only)", type=["pdf", "txt", "docx"]
)

job_role = st.text_input("Enter the job role that you are targeting")
analyse = st.button("Analyse Resume")
print(analyse)

if analyse and uploaded_file and model:
    try:
        file_content = extract_text(uploaded_file)
        if not file_content.strip():
            st.error("File does not have any content")
            st.stop()
        else:
            prompt = f"""You are a brutally honest no-nonsense AI resume roaster who has been reviewing resumes for decades. Roast the resume content provided below like you are on a comedy night skit, be witty, critical and sarcastic and 
            provide constructive feedback on how to improve it for landing a job for the job role: {job_role} in a good company.
            Here is the resume content:
                    {file_content}
            make it sting - GO WILD!"""
            model_to_use = model_map[model]
            with st.spinner(f"🔥 ... This might take a moment... 🔥", show_time=True):
                response = generate_and_parse_answer(prompt, model_to_use)
                print(f"Response from model {model_to_use}: {response}")
            st.markdown("### 🎤 AI Roasting Result 🎤")

            st.markdown(response)

    except Exception as e:
        st.error(f"some error occured: {e}")
        import traceback

        print(f"Error details: {e}")
        traceback.print_exc()
