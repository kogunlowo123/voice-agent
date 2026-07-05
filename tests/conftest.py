"""Test configuration for Voice Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "voice-agent", "category": "Customer Service"}
