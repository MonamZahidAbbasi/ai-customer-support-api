## AI Customer Support API 

A FastAPI-based backend service that automatically analyzes customer support queries — classifying category, sentiment, and priority, and generating a professional suggested reply, all in structured JSON.

## Features

- **Query Analysis** — Accepts raw customer messages via a REST API 
- **Automatic Categorization** — Classifies queries (Billing, Technical Support, Delivery Issue, General Inquiry)
- **Sentiment Detection** — Identifies customer emotion (Positive, Negative, Neutral) 
- **Priority Scoring** — Flags urgency level (Low, Medium, High) 
- **AI-Generated Reply** — Produces a professional, empathetic suggested response 
- **Guaranteed Structured Output** — Pydantic schema validation ensures consistent, reliable JSON every time 
- **Input Validation & Error Handling** — Graceful handling of empty messages, missing fields, and API failures 

## Architecture

Client Request (JSON)
        ↓
FastAPI Route (/analyze-query)
        ↓
Pydantic Request Validation
        ↓
LLM Service Layer (structured prompt)
        ↓
Gemini API (with response_schema enforcement)
        ↓
Pydantic Response Validation
        ↓
Structured JSON Response

## Tech Stack

- **Python 3.12** 
- **FastAPI** — Web framework for building the API 
- **Uvicorn** — ASGI server to run the application 
- **Google Gemini API** (`google-genai`) — LLM provider for analysis 
- **Pydantic** — Data validation and structured output enforcement 
- **python-dotenv** — Secure environment variable management


## Setup & Installation

1. Clone the repository: 
git clone https://github.com/MonamZahidAbbasi/ai-customer-support-api.git 
cd ai-customer-support-api 

2. Create and activate a virtual environment: 
python -m venv venv 
venv\Scripts\activate

4. Install dependencies: 
pip install -r requirements.txt

5. Create a .env file in the root directory: 
GEMINI_API_KEY=your_api_key_here

## Usage

Start the server: 
uvicorn main:app --reload

Open the interactive API docs at: 
http://127.0.0.1:8000/docs 


## Example Request

POST /analyze-query 
{ 
  "customer_message": "I ordered a laptop 2 weeks ago and it still hasn't arrived. This is really frustrating, I need it for work urgently!" 
}

## Example Response

{
  "category": "Delivery Issue", 
  "sentiment": "Negative", 
  "priority": "High", 
  "suggested_reply": "We sincerely apologize for the delay in your laptop delivery..." 
}

## What I Learned:

- Designing a clean **Service Layer Architecture** that separates API routing from LLM logic, making the codebase easier to maintain and extend. 
- Using **Pydantic Enums** to force the LLM into returning a fixed, predictable set of category/sentiment/priority values instead of arbitrary text. 
- Combining multiple prompt engineering techniques (role prompting, structured instructions, output constraints) into a single production-style prompt. 
- Leveraging FastAPI's built-in request validation to automatically reject malformed requests before they reach business logic. 
- Handling edge cases (empty input) with explicit checks to avoid unnecessary API calls and reduce cost.

## Author:

**Monam Zahid Abbasi** 
- GitHub: @MonamZahidAbbasi
