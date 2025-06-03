import re
import ollama
from google import genai
from google.genai import types
from openai import OpenAI
import os
from dotenv import load_dotenv
from config import google_models, openrouter_models
load_dotenv()


gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"), 
                             http_options=types.HttpOptions(api_version='v1alpha'))
openrouter_client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)


def use_ollama_sdk(query, model):
    response = ollama.generate(
        model=model,
        prompt = query
    )['response']
    
    think_match = re.search(r'<think>(.*?)</think>', response, re.DOTALL)
    if not think_match:
        return response.strip()
    answer_start = response.find('</think>') + len('</think>')
    answer = response[answer_start:].strip()

    parsed_response = {
            "thinking": think_match.group(1).strip() if think_match else "",
            "answer": answer,
            "raw_response": response
        }
    print(parsed_response)
    return parsed_response['answer']


def get_text_from_gemini_response(response):
    """Returns the concatenation of all text parts in the response.

    This is an internal method that allows customizing the warning message.
    """
    if (
        not response.candidates
        or not response.candidates[0].content
        or not response.candidates[0].content.parts
    ):
      return None

    text = ''
    any_text_part_text = False
    non_text_parts = []
    for part in response.candidates[0].content.parts:
      for field_name, field_value in part.model_dump(
          exclude={'text', 'thought'}
      ).items():
        if field_value is not None:
          non_text_parts.append(field_name)
      if isinstance(part.text, str):
        if isinstance(part.thought, bool) and part.thought:
          continue
        any_text_part_text = True
        text += part.text
    
    # part.text == '' is different from part.text is None
    return text if any_text_part_text else None

def use_gemini_sdk(query, model):
   

    response = gemini_client.models.generate_content(
        model=model,
        # config=types.GenerateContentConfig(
        #     response_mime_type="text/plain",
        #     ),
        contents= query,
    )   
    return response.text
   

def use_openrouter_sdk(query, model):
    completion = openrouter_client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message.content

    

def generate_and_parse_answer(query, model) -> str:
    
    """
    Based on the selected model , we use an inference provider
    """
    if model in google_models:
        return use_gemini_sdk(query, model)
    elif model in openrouter_models:
        return use_openrouter_sdk(query, model)
    else:
        return use_ollama_sdk(query, model)