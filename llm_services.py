from google import genai
from dotenv import load_dotenv
from models import CustomerQuery, SupportAnalysis
import os

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API Key not found.")
client=genai.Client(api_key=api_key)

def build_prompt(customer_message:str)->str:
    prompt=f""" 
you are an expert customer support analyst for an e-commerce company.
your task is to analyze the customer message and provide:
1. The category of the issue.
2. The sentiment of the customer.
3. The priority level.
4. A professional, empathetic reply.
Rules:
- Base the priority on how urgent/severe the issue sounds, not just the worth used.
- The suggested reply should acknowledge the customer's concern before offering next steps.
- Keep the suggested reply under 60 words.
customer message:{customer_message}
"""
    return prompt

def analyze_customer_query(customer_message:str)->SupportAnalysis:
    prompt=build_prompt(customer_message)
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type":"application/json",
            "response_schema":SupportAnalysis
        }
    )
    return response.parsed
                