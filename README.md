# Merlin-Lite

A simplified demonstration of a production AI analysis pipeline. This repository showcases architectural patterns and design decisions for building scalable, modular analysis systems.


**Flow**: `input → ingest → process → output → structured JSON response`

### Example Request
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Artificial intelligence is transforming software development",
    "context": {"domain": "technology"}
  }'
```

### Example Response
```json
{
  "status": "success",
  "result": {
    "summary": "Analysis of text: 'Artificial intelligence is transforming...' (mock result)",
    "entities": ["entity_1", "entity_2", "entity_3"],
    "confidence": 0.87,
    "processing_time_ms": 500
  },
  "message": null
}
```

### System Design

```
┌─────────────────────────────────────────┐
│         FastAPI Application              │
│  (/analyze, /health, documentation)     │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│        Analysis Pipeline                 │
│  ┌─────────┬────────────┬───────────┐  │
│  │ Ingest  │  Process   │  Output   │  │
│  └─────────┴────────────┴───────────┘  │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│      Analysis Layer (Mocked)             │
│  • Text analysis                         │
│  • Entity extraction                     │
│  • Confidence scoring                    │
│  • Output validation                     │
└─────────────────────────────────────────┘
```

### Folder Structure

```
merlin-lite/
├── app/
│   ├── main.py          # FastAPI application
│   ├── pipeline.py      # Core orchestration logic
│   ├── analyzer.py      # Mock AI analysis layer
│   └── models.py        # Pydantic data models
├── data/
│   └── sample_input.json  # Example requests
├── README.md
├── requirements.txt
└── .env.example
```


## What's Omitted

This repository demonstrates architectural patterns and system design for an AI pipeline. Proprietary validation and verification components are intentionally excluded.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository
2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment
   ```bash
   cp .env.example .env
   ```

### Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### Testing the API

Health check:
```bash
curl http://localhost:8000/health
```

Analyze text:
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your text here",
    "context": {"domain": "example"}
  }'
```

## License

This is a demonstration project created for educational and hiring purposes.

## Notes

*This scaffolded directory was created with use of AI for time and infrastructural signaling* 
