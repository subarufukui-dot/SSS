from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # 追加

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 届くデータの形を定義
class FortuneRequest(BaseModel):
    name: str
    problem: str

@app.post("/fortune") # GETからPOSTに変更し、パスも /fortune に
def get_fortune(request: FortuneRequest):
    # 送られてきたデータを使って文章を作る
    message = f"{request.name}さん、ようこそ！！困っていることは「{request.problem}」ですね！！"
    return {"message": message}