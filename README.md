# VoiceGuard

VoiceGuard is a voice-security prototype designed to detect potential
voice-based attacks using audio artifact detection and speaker verification.

## Project Structure

```text
voiceguard/
├── frontend/       # React dashboard and audio capture
├── backend/        # FastAPI gateway, preprocessing, fusion and APIs
├── ml/             # Detection and speaker-verification models
├── docs/            # Architecture, references and presentation material
├── .env.example     # Environment variable template
├── .gitignore
└── README.md