"""
Data models for Merlin-Lite analysis pipeline.
These models define the structure of input requests and output responses.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class AnalysisRequest(BaseModel):
    """Input model for analysis requests."""
    text: str = Field(..., min_length=1, max_length=5000)
    context: Optional[Dict[str, str]] = None


class AnalysisResult(BaseModel):
    """Individual analysis result from the pipeline."""
    summary: str
    entities: List[str]
    confidence: float
    processing_time_ms: float


class AnalysisResponse(BaseModel):
    """Output model for analysis requests."""
    status: str
    result: AnalysisResult
    message: Optional[str] = None


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    version: str
