from fastapi import APIRouter, HTTPException
from app.model import get_embedding
from app.schemas import TextRequest, EmbeddingResponse

router = APIRouter()

@router.post("/embed", response_model=EmbeddingResponse)
def embed_text(req: TextRequest):
    try:
        vec = get_embedding(req.text)
        return EmbeddingResponse(embedding=vec)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
