# VoxPilot AI

VoxPilot AI is a general-purpose AI Employee platform.

## Phase 1 — Foundation

This repository contains the first deployment-ready foundation:

- Premium VoxPilot AI web interface
- Core navigation
- Dashboard shell
- AI Employees area
- Leads area
- Campaigns area
- Calls area
- Business Brain area
- Analytics area
- Settings area
- `/health` endpoint
- Render-compatible Python deployment
- Modular directories reserved for future AI, voice, knowledge, campaign, analysis, integration, and database functionality

## Architecture direction

Future phases will add:

1. Business Brain
2. General-purpose AI Employee engine
3. Conversation state and memory
4. Multilingual language detection and switching
5. Tool/action system
6. Streaming STT/LLM/TTS
7. Real-time voice and telephony
8. Campaign scheduling and lead qualification
9. Post-call transcription and analysis
10. Production security, compliance, monitoring and billing

The foundation does not fake these capabilities.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

Health check:

`http://localhost:5000/health`

## Render

Recommended Render Web Service settings:

- Runtime: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

Do not place real API keys in this repository. Use Render Environment Variables for secrets.
