from fastapi import FastAPI, WebSocket
from preprocessing import bytes_to_array, is_speech

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        audio = bytes_to_array(data)
        speech_detected = is_speech(audio)
        await websocket.send_json({"speech_detected": speech_detected})