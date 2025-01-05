from google import genai
from google.genai import types
import requests
import pathlib

client = genai.Client(api_key='AIzaSyCfC90VhSlMX_j3wGsZnjHuze0e0pSJefM')
MODEL_ID = "gemini-2.0-flash-exp"


response = client.models.generate_content(
    model=MODEL_ID,
    contents="What does writing on the image say?"
)

def generate_image_analysis(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=image_data,
        generationConfig={
            "response_mime_type": "application/json",
        }
    )

    return response

# Example usage
image_path = "check_blood.jpg"
analysis_result = generate_image_analysis(image_path)
print(analysis_result)
