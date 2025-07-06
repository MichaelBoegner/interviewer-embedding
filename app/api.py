from fastapi import APIRouter, HTTPException
from app.model import get_embedding
from app.schemas import BatchRequest, EmbeddingResponse

router = APIRouter()

@router.post("/embed_batch", response_model=EmbeddingResponse)
def embed_batch(req: BatchRequest):
    texts = [chunk.text for chunk in req.chunks]
    vectors = get_embedding(texts)
    return {"embeddings": vectors}
