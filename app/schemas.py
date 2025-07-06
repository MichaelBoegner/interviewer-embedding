from pydantic import BaseModel
from typing import List

class EmbedChunk(BaseModel):
    topic_number: int
    question_number: int
    text: str

class BatchRequest(BaseModel):
    chunks: List[EmbedChunk]

class EmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
