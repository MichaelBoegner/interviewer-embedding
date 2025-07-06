from fastapi import APIRouter, HTTPException
from app.model import get_embedding
from app.schemas import QueryEmbedRequest, QueryEmbedResponse, ContextEmbedRequest, ContextEmbedResponse

router = APIRouter()

@router.post("/embed_query", response_model=QueryEmbedResponse)
def embed_batch(req: QueryEmbedRequest):
    vector = get_embedding(req.text)
    return {"embeddings": vector}


@router.post("/embed_context", response_model=ContextEmbedResponse)
def embed_batch(req: ContextEmbedRequest):
    texts = [chunk.text for chunk in req.chunks]
    vectors = get_embedding(texts)
    return {"embeddings": vectors}
