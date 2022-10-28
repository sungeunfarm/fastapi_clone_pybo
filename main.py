from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.question import question_router
from domain.answer import answer_router
import uvicorn

app = FastAPI()

# CORS 처리
origins = ["http://127.0.0.1:5173",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return{"message":"안녕하세요 파이보"}

# 라우터 실행코드
app.include_router(question_router.router)
app.include_router(answer_router.router)

if __name__ == '__main__':
    uvicorn.run(app = "main:app", host= "127.0.0.1", port= 8000, reload=True, workers=4)