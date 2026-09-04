## AI Customer Support API 
\n
A FastAPI-based backend service that automatically analyzes customer support queries — classifying category, sentiment, and priority, and generating a professional suggested reply, all in structured JSON.
\n
## Features
\n
- **Query Analysis** — Accepts raw customer messages via a REST API \n
- **Automatic Categorization** — Classifies queries (Billing, Technical Support, Delivery Issue, General Inquiry)\n
- **Sentiment Detection** — Identifies customer emotion (Positive, Negative, Neutral) \n
- **Priority Scoring** — Flags urgency level (Low, Medium, High) \n
- **AI-Generated Reply** — Produces a professional, empathetic suggested response \n
- **Guaranteed Structured Output** — Pydantic schema validation ensures consistent, reliable JSON every time \n
- **Input Validation & Error Handling** — Graceful handling of empty messages, missing fields, and API failures 
\n
## Architecture
\n
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
\n

## Tech Stack
\n
- **Python 3.12** \n
- **FastAPI** — Web framework for building the API \n
- **Uvicorn** — ASGI server to run the application \n
- **Google Gemini API** (`google-genai`) — LLM provider for analysis \n
- **Pydantic** — Data validation and structured output enforcement \n
- **python-dotenv** — Secure environment variable management
\n

## Setup & Installation
\n
1. Clone the repository: \n
git clone https://github.com/MonamZahidAbbasi/ai-customer-support-api.git \n
cd ai-customer-support-api 
\n
2. Create and activate a virtual environment: \n
python -m venv venv \n
venv\Scripts\activate
\n
3. Install dependencies: \n
pip install -r requirements.txt
\n
4. Create a .env file in the root directory: \n
GEMINI_API_KEY=your_api_key_here
\n
## Usage
\n
Start the server: \n
uvicorn main:app --reload
\n
Open the interactive API docs at: \n
http://127.0.0.1:8000/docs \n


## Example Request
\n
POST /analyze-query \n
{ \n
  "customer_message": "I ordered a laptop 2 weeks ago and it still hasn't arrived. This is really frustrating, I need it for work urgently!" \n
}
\n
## Example Response
\n
{\n
  "category": "Delivery Issue", \n
  "sentiment": "Negative", \n
  "priority": "High", \n
  "suggested_reply": "We sincerely apologize for the delay in your laptop delivery..." \n
}
\n

## What I Learned:
\n
- Designing a clean **Service Layer Architecture** that separates API routing from LLM logic, making the codebase easier to maintain and extend. \n
- Using **Pydantic Enums** to force the LLM into returning a fixed, predictable set of category/sentiment/priority values instead of arbitrary text. \n
- Combining multiple prompt engineering techniques (role prompting, structured instructions, output constraints) into a single production-style prompt. \n
- Leveraging FastAPI's built-in request validation to automatically reject malformed requests before they reach business logic. \n
- Handling edge cases (empty input) with explicit checks to avoid unnecessary API calls and reduce cost.
\n
## Author:
\n
**Monam Zahid Abbasi** \n
- GitHub: @MonamZahidAbbasi
