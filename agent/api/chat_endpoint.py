from fastapi import APIRouter, Header, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from core.config import settings
from router.orchestrator import orchestrator

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    message: str
    user_id: str
    user_name: str = "there"
    user_gender: str = "unknown"
    language: str = "en"


@router.post("/chat")
async def chat(
    request: ChatRequest,
    x_internal_key: str = Header(default=""),
):
    if x_internal_key != settings.internal_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")

    async def token_stream():
        async for chunk in orchestrator.stream_response(
            session_id=request.session_id,
            message=request.message,
            user_name=request.user_name,
            user_gender=request.user_gender,
            language=request.language,
            user_id=request.user_id,
        ):
            yield chunk

    return StreamingResponse(
        token_stream(),
        media_type="text/plain; charset=utf-8",
        headers={"X-Content-Type-Options": "nosniff"},
    )
