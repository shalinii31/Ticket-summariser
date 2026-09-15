from fastapi import FastAPI
from app.routes.chat_route import router

app = FastAPI(
    title = "Ticket summariser",
    description = "Summarises the custormer query",
    version = "1.0.0"
)


app.include_router(router, prefix="/api")

