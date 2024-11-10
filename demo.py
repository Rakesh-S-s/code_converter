import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCDGLYDel_NwRJAtJb4scL6GBhvOJgqSt0")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)