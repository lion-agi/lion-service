# Getting Started with Lion Service

## Installation

```bash
uv pip install lion-service
```

Install provider packages as needed:
```bash
uv pip install lion-openai      # OpenAI
uv pip install lion-anthropic   # Anthropic
uv pip install lion-perplexity  # Perplexity
uv pip install lion-groq        # Groq
```

## Basic Usage

### Initialize a Model

```python
from lion_service import iModel

model = iModel(
    provider="openai",
    task="chat",
    model="gpt-4",
    api_key="your-api-key"
)
```

### Make Requests

```python
async def chat():
    response = await model.invoke(
        messages=[
            {"role": "user", "content": "Hello!"}
        ]
    )
    return response
```

### Rate Limiting

Enable rate limiting by specifying token and request limits:

```python
model = iModel(
    provider="openai",
    task="chat",
    model="gpt-4",
    interval_tokens=90000,  # 90K tokens/min
    interval_requests=3500  # 3.5K requests/min
)
```

### Environment Variables

Use environment variables for API keys:

```python
model = iModel(
    provider="openai",
    task="chat",
    model="gpt-4",
    api_key_schema="OPENAI_API_KEY"  # Uses OPENAI_API_KEY env var
)
```

## Next Steps

- Check [API Reference](api_reference.md) for detailed documentation
- See [Contributing Guide](contributing.md) to contribute
