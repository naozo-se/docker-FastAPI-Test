from fastapi import FastAPI
import json
import uvicorn
import os

app = FastAPI()
jsonExtention = ".json"

@app.api_route("/{path:path}", methods=["GET", "POST"])
async def catch_all(path: str):

    # カレントまでの絶対パス取得
    absPath = os.path.abspath('.')
    jsonFilePath = f"{absPath}{os.sep}{path}"

    # jsonの拡張子付きではない時
    if(os.path.splitext(jsonFilePath)[1] != jsonExtention):
        jsonFilePath = f"{jsonFilePath}{jsonExtention}"

    # ファイルが存在するか
    if os.path.exists(jsonFilePath):
        jsn = None
        with open(jsonFilePath, "r", encoding="utf-8") as f:
            jsn = json.load(f)
        return jsn

    # ファイルがない時
    return {"message": "error"}

if __name__ == '__main__':
    uvicorn.run(app)
