from fastapi import FastAPI, WebSocket
from preprocessing import bytes_to_array, is_speech
from fusion import compute_risk_score

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
        risk_score = compute_risk_score(artifact_prob=0.2, speaker_similarity=0.9)  # dummy values
        await websocket.send_json({"speech_detected": speech_detected, "risk_score": risk_score})