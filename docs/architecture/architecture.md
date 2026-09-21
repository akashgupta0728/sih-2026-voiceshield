# VoiceGuard Architecture

## System Overview

VoiceGuard consists of three main components:

1. Frontend
2. Backend
3. ML models

## Data Flow

Frontend
    ↓
WebSocket
    ↓
FastAPI Backend
    ↓
Audio Preprocessing
    ↓
ML Models
    ↓
Risk Fusion
    ↓
Alert / Risk Score
    ↓
Frontend Dashboard

## Components

### Frontend

The React frontend handles:

- Microphone/audio capture
- Attack simulation
- Risk score visualization
- Alerts and dashboard UI

### Backend

The FastAPI backend handles:

- WebSocket communication
- Audio ingestion
- Audio preprocessing
- Communication with ML models
- Risk-score fusion
- Alert logic
- REST APIs

### ML

The ML component contains:

- Audio artifact/spoof detection
- Speaker verification
- Model inference wrappers

## Prototype Architecture

For the 36-hour prototype, ML models will run directly inside the
FastAPI backend process instead of being deployed as separate services.