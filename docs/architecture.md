# Voice Agent Architecture

Conversational voice AI agent that handles inbound and outbound calls, performs speech-to-text and text-to-speech, manages IVR flows, detects customer sentiment in real-time, and provides agent assist during live calls.

## Domain Tools

- **transcribe_call**: Transcribe a live or recorded call to text
- **synthesize_speech**: Convert text response to natural speech
- **detect_intent**: Detect caller intent from transcribed speech
- **analyze_sentiment**: Analyze customer sentiment from voice and text signals
- **suggest_response**: Suggest a response for the agent during a live call