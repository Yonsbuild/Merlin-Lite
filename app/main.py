"""
Merlin-Lite: Simplified AI pipeline demonstration.
"""

from fastapi import FastAPI, HTTPException
import logging

from .models import AnalysisRequest, AnalysisResponse, HealthResponse
from .pipeline import pipeline

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Merlin-Lite",
    description="Simplified AI analysis pipeline",
    version="0.1.0"
)


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint.

    Returns:
        HealthResponse with status and version
    """
    return HealthResponse(
        status="healthy",
        version="0.1.0"
    )


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest) -> AnalysisResponse:
    """
    Analysis endpoint.

    Takes input text and optional context, runs it through the pipeline,
    and returns structured analysis results.
    
    """
    try:
        logger.info(f"Received analysis request: {len(request.text)} characters")

        # Run pipeline
        result = await pipeline.run(request.text, request.context)

        if result.get("status") == "error":
            raise HTTPException(
                status_code=400,
                detail=result.get("message", "Analysis failed")
            )

        # Structure response
        response = AnalysisResponse(
            status="success",
            result={
                "summary": result["result"]["summary"],
                "entities": result["result"]["entities"],
                "confidence": result["result"]["confidence"],
                "processing_time_ms": result["result"]["processing_time_ms"]
            }
        )

        logger.info("Analysis completed successfully")
        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Merlin-Lite",
        "description": "Simplified AI analysis pipeline",
        "endpoints": {
            "health": "/health",
            "analyze": "/analyze",
            "docs": "/docs"
        }
    }
