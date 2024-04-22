from typing import Optional, List

from langchain_core.pydantic_v1 import BaseModel, Field

class ReviewEvaluation(BaseModel):
    """Evaluation of a product based on a review given by a user. Product features with which the user is satisfied are grouped together with those with which he is not satisfied."""
    
    satisfaction: Optional[List[str]] = Field(
        default=None,
        description="List of product features with which the user is satisfied"
    )
    
    dissatisfaction: Optional[List[str]] = Field(
        default=None,
        description="List of product features with which the user is not satisfied"
    )