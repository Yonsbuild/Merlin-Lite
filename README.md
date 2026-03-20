# Merlin-Lite

A simplified demonstration of a production AI analysis pipeline. This repository showcases architectural patterns and design decisions for building scalable, modular analysis systems.

## What It Is

This repository demonstrates a **multi-stage analysis pipeline** designed to:
- **Process data through structured stages** (ingestion → processing → output)
- **Handle async operations** for real-world I/O-bound workflows
- **Return structured JSON responses** with typed models and validation
- **Separate concerns** across logical layers (API, pipeline, analysis)

The codebase shows how to design systems for scale and maintainability, using patterns commonly found in production data processing platforms.

## What It Does

The pipeline orchestrates three key stages:

1. **Ingestion**: Validate and prepare input text and context
2. **Processing**: Execute analysis through a modular analysis layer
3. **Output**: Validate results and structure final response

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

## Architecture

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

## Design Decisions

### 1. **Async Processing**

Every operation is implemented as async (`async/await`). This demonstrates understanding of real-world constraints:
- Processing often requires I/O (API calls, database queries, file operations)
- Async patterns allow serving multiple concurrent requests efficiently
- Simulated processing delays show how delays are managed

**See**: `app/pipeline.py:18-25`, `app/analyzer.py:16-40`

### 2. **Modular Pipeline**

The pipeline is decomposed into distinct stages (ingest → process → output):
- Each stage has a single responsibility
- Easy to test, debug, and modify independently
- Clear data flow between stages
- Real systems scale this pattern with advanced orchestration tools

**See**: `app/pipeline.py:11-70`

### 3. **Structured Data Models**

All inputs and outputs use Pydantic models:
- Type-safe request/response handling
- Automatic validation and documentation
- OpenAPI schema generation for API documentation
- Easier maintenance and refactoring

**See**: `app/models.py`

### 4. **Separation of Concerns**

- **main.py**: HTTP layer (FastAPI endpoints)
- **pipeline.py**: Business logic orchestration
- **analyzer.py**: Analysis operations (mocked)
- **models.py**: Data contracts

This separation makes the system:
- Testable (swap components easily)
- Maintainable (changes isolated to relevant modules)
- Scalable (each layer can evolve independently)

### 5. **Error Handling**

Proper error handling at system boundaries:
- Input validation (empty strings rejected)
- Output validation (structured data verified)
- Exception handling with meaningful messages
- HTTP status codes reflect error types

**See**: `app/main.py:50-75`

## What's Omitted

This repository demonstrates architectural patterns and system design for an AI pipeline. Proprietary validation and verification components are intentionally excluded.

Specifically omitted:
- **Proprietary verification logic**: Complex algorithms specific to the full system
- **Real AI models**: Analysis operations are mocked to demonstrate interface design
- **Production datasets**: Uses synthetic sample data only
- **Implementation details**: No real prompts or algorithmic logic exposed
- **Database integration**: In-memory processing for demonstration
- **Monitoring infrastructure**: Basic logging only

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

## Key Takeaways

This codebase demonstrates:

✅ **Production API Design**: FastAPI with proper models, validation, error handling

✅ **Async Architecture**: Understanding of concurrency for I/O-bound operations

✅ **Modular Pipeline**: Clear separation of concerns and data flow

✅ **Code Organization**: Logical structure that scales with complexity

✅ **Documentation**: Self-documenting code with docstrings and comments

✅ **Type Safety**: Pydantic models for data validation

This architecture is foundational for building larger, production-grade analysis systems.

## Future Enhancements

In a production system, this would expand to include:

- Database integration (PostgreSQL/MongoDB)
- Advanced caching strategies (Redis)
- Asynchronous task queues (Celery/RabbitMQ)
- Comprehensive monitoring (Prometheus/Grafana)
- Advanced validation and error recovery
- Multi-step processing pipelines
- Real AI model integration
- Complex orchestration logic

## License

This is a demonstration project created for educational and hiring purposes.
