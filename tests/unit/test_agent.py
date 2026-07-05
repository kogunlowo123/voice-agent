"""Voice Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_transcribe_call():
    """Test Transcribe a live or recorded call to text."""
    tools = AgentTools()
    result = await tools.transcribe_call(audio_source="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_synthesize_speech():
    """Test Convert text response to natural speech."""
    tools = AgentTools()
    result = await tools.synthesize_speech(text="test", voice="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_intent():
    """Test Detect caller intent from transcribed speech."""
    tools = AgentTools()
    result = await tools.detect_intent(transcript="test", context="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_sentiment():
    """Test Analyze customer sentiment from voice and text signals."""
    tools = AgentTools()
    result = await tools.analyze_sentiment(audio_features="test", transcript="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.voice_agent_agent import VoiceAgentAgent
    agent = VoiceAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
