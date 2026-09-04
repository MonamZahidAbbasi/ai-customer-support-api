from fastapi import FastAPI,HTTPException
from models import CustomerQuery,SupportAnalysis
from llm_services import analyze_customer_query

app=FastAPI(title="AI Customer Support API",
            description="automatically analyzes customer queries and suggest replies. ")
@app.get("/")
def home():
    return {
        "message":"AI customer Support API is running..."
    }

@app.post("/analyze-query",response_model=SupportAnalysis)
def analyze_query(query:CustomerQuery):
    if not query.customer_message:
        raise HTTPException(
            status_code=400,
            detail="Customer message is required."
        )
    try:
        result=analyze_customer_query(query.customer_message)
        return result
    except Exception as e:
        print("Error:",e)
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while analyzing this query."
        )
        
