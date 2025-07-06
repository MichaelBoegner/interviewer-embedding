from pydantic import BaseModel
from typing import List

class QueryEmbedRequest(BaseModel):
    text: str
class EmbedChunk(BaseModel):
    topic_number: int
    question_number: int
    text: str
class ContextEmbedRequest(BaseModel):
    chunks: List[EmbedChunk]

class QueryEmbedResponse(BaseModel):
    embeddings: List[float]
class ContextEmbedResponse(BaseModel):
    embeddings: List[List[float]]
