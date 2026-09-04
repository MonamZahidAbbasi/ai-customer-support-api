from pydantic import BaseModel,Field
from enum import Enum

class Category(str,Enum):
    billing="Billing"
    technical="Technical Support"
    delivery="Delivery Issues"
    general="General Inquiry"

class Sentiment(str,Enum):
    negative="Negative"
    positive="Positive"
    neutral="Neutral"

class Priority(str,Enum):
    low="Low"
    high="High"
    medium="Medium"

class CustomerQuery(BaseModel):
    customer_message:str = Field(description="The raw message/complaint from the customer.")

class SupportAnalysis(BaseModel):
    category:Category = Field(description="The category this query belongs to")
    sentiment:Sentiment=Field(description="The emotional one of the customer's message.")
    priority:Priority=Field(description="how urgently this needs to be addressed.")
    suggested_reply:str=Field(description="A professional, empathetic reply to customer.")