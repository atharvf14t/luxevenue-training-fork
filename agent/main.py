import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat_endpoint import router as chat_router
from api.health_endpoint import router as health_router
from core.config import settings
from core.database import close_pool, get_pool
from router.orchestrator import orchestrator


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("[LuxeVenue Agent] Starting up...")

    # Warm up DB connection pool
    try:
        await get_pool()
        print("[LuxeVenue Agent] Database connection pool ready.")
    except Exception as e:
        print(f"[LuxeVenue Agent] DB pool warning: {e}")

    # Try to set up Postgres-backed checkpointer for LangGraph state persistence
    try:
        await orchestrator.setup_postgres_checkpointer(settings.database_url)
    except Exception as e:
        print(f"[LuxeVenue Agent] Checkpointer warning (using MemorySaver): {e}")

    yield

    # Shutdown
    await close_pool()
    print("[LuxeVenue Agent] Shutdown complete.")


app = FastAPI(
    title="LuxeVenue AI Agent Service",
    description="Multi-agent AI backend for LuxeVenue corporate event planning",
    version="1.0.0",
    lifespan=lifespan,
)

# Allow calls from Next.js dev server and production domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://luxevenue.ai", "https://www.luxevenue.ai"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(health_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)
