from typing import Optional
from sqlmodel import Field, SQLModel, create_engine , Session
import instructor
from pydantic import BaseModel
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

# Define your desired output structure
class NutritionInfo(SQLModel, instructor.OpenAISchema, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    serving_size: str
    servings_per_container: int
    calories_per_serving: int
    total_fat_per_serving: str
    sodium_per_serving: str
    total_carbohydrate_per_serving: str
    protein_per_serving: str

# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language

def get_nutrition(base64_image: str) -> NutritionInfo:
    return client.chat.completions.create(
        model="gpt-4o",
        response_model=NutritionInfo,
        messages=[
            {"role": "system", "content": "You are a nutrition expert that will extract the nutrition information from the nutrition label"},
            {"role": "user", "content": [
                {"type": "text", "text": "Whats the nutrition?"},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"
                }}
            ]}
        ]
    )