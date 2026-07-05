# Voice Agent

[![CI](https://github.com/kogunlowo123/voice-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/voice-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Customer Service | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Conversational voice AI agent that handles inbound and outbound calls, performs speech-to-text and text-to-speech, manages IVR flows, detects customer sentiment in real-time, and provides agent assist during live calls.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `transcribe_call` | Transcribe a live or recorded call to text |
| `synthesize_speech` | Convert text response to natural speech |
| `detect_intent` | Detect caller intent from transcribed speech |
| `analyze_sentiment` | Analyze customer sentiment from voice and text signals |
| `suggest_response` | Suggest a response for the agent during a live call |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/voice/transcribe` | Transcribe call |
| `POST` | `/api/v1/voice/synthesize` | Synthesize speech |
| `POST` | `/api/v1/voice/intent` | Detect intent |
| `POST` | `/api/v1/voice/sentiment` | Analyze sentiment |
| `POST` | `/api/v1/voice/suggest` | Suggest response |

## Features

- Speech Recognition
- Voice Synthesis
- Ivr Management
- Sentiment Detection
- Agent Assist

## Integrations

- Twilio
- Amazon Connect
- Genesys
- Google Dialogflow
- Assemblyai

## Architecture

```
voice-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── voice_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Voice Platform + STT/TTS + NLU + Contact Center**

---

Built as part of the Enterprise AI Agent Platform.
