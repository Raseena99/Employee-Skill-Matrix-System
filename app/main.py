from fastapi import FastAPI
from .database import Base
from .database import engine
from .routes import router
Base.metadata.create_all(bind=engine)
app = FastAPI(
title="Employee Skill Matrix System",
version="1.0.0",
description="Enterprise skill tracking platform"
)
app.include_router(router)
@app.get("/")
def home():
return {
"message": "Employee Skill Matrix API Running"
}
