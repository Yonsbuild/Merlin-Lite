"""
Core analysis pipeline.

This module orchestrates the flow:
  input → ingestion → processing → output

"""

import time
from typing import Dict, Optional
from .analyzer import analyze_text, validate_output


class AnalysisPipeline:
    """Main pipeline orchestrator."""

    async def ingest(self, text: str, context: Optional[Dict] = None) -> Dict:
        """
        Stage 1: Ingestion
        - Validate input
        - Prepare for processing
        """
        if not text or len(text.strip()) == 0:
            raise ValueError("Input text cannot be empty")

        return {
            "text": text.strip(),
            "context": context or {},
            "ingestion_timestamp": time.time()
        }

    async def process(self, ingested_data: Dict) -> Dict:
        """
        Stage 2: Processing
        - Extract features
        - Run analysis
        - Format results
        """
        text = ingested_data["text"]
        context = ingested_data["context"]

        # Call analysis layer
        analysis_result = await analyze_text(text, context)

        return {
            "input_text": text,
            "analysis": analysis_result,
            "processing_timestamp": time.time()
        }

    async def output(self, processed_data: Dict) -> Dict:
        """
        Stage 3: Output
        - Validate results
        - Structure final output
        - Prepare for response
        """
        analysis = processed_data["analysis"]

        # Validate output
        is_valid = await validate_output(analysis)

        if not is_valid:
            raise ValueError("Output validation failed")

        return {
            "status": "success",
            "result": {
                "summary": analysis["summary"],
                "entities": analysis["entities"],
                "confidence": analysis["confidence"],
                "processing_time_ms": analysis["processing_time_ms"]
            }
        }

    async def run(self, text: str, context: Optional[Dict] = None) -> Dict:
        """
        Execute the complete pipeline.

        Flow: input → ingest → process → output
        """
        try:
            if len(text) > 5000:
              raise ValueError("Input exceeds pipeline limit")
            
            # Stage 1: Ingest
            ingested = await self.ingest(text, context)

            # Stage 2: Process
            processed = await self.process(ingested)

            # Stage 3: Output
            output = await self.output(processed)

            return output

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }


# Global pipeline instance
pipeline = AnalysisPipeline()
