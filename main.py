from schemas import ReviewEvaluation

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert satisfaction and dissatisfaction extractor."
            "Only extract the satisfaction and dissatisfaction from the review.",
        ),
        
        (
            "human",
            "{text}"
        ),
    ]
)