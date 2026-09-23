from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.websocket("/ws")   
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    while True:
        data=await websocket.receive_bytes()
        await websocket.send_bytes(data)   