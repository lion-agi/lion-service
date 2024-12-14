# Lion Service

A unified interface for AI model providers (OpenAI, Anthropic, Perplexity, Groq) with rate limiting and token management.

[![Version](https://img.shields.io/pypi/v/lion-service.svg)](https://pypi.org/lion-agi/lion-service/)
[![License](https://img.shields.io/github/license/lion-agi/lion-service.svg)](LICENSE)

## Features

- Unified interface for multiple AI providers
- Built-in rate limiting and token tracking
- Automatic retries with exponential backoff
- Token calculation using tiktoken

## Installation

```bash
uv pip install lion-service

# Provider-specific packages
uv pip install lion-openai      # For OpenAI
uv pip install lion-anthropic   # For Anthropic
uv pip install lion-perplexity  # For Perplexity
uv pip install lion-groq        # For Groq
```

## Usage

```python
from lion_service import iModel

# Initialize
model = iModel(
    provider="openai",
    task="chat",
    model="gpt-4",
    api_key="your-api-key",
    interval_tokens=90000,  # Optional: Token limit per minute
    interval_requests=3500  # Optional: Request limit per minute
)

# Make requests
async def chat():
    response = await model.invoke(
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response)
```

## Rate Limiting

```python
# Token and request limits
model = iModel(
    provider="openai",
    interval_tokens=90000,  # 90K tokens/min
    interval_requests=3500  # 3.5K requests/min
)
```

## Error Handling

```python
from lion_service import RateLimitError

try:
    response = await model.invoke(...)
except RateLimitError as e:
    print(f"Rate limit exceeded: {e.requested_tokens} tokens")
```

## Custom Services

```python
from lion_service import Service, register_service

@register_service
class MyService(Service):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.name = "my_service"

    def list_tasks(self):
        return ["chat", "completion"]
```

## Contributing

1. Fork and clone the repository
2. Install dev dependencies: `uv pip install -e ".[dev]"`
3. Make changes
4. Run tests: `pytest`
5. Submit a pull request

See [Contributing Guide](docs/contributing.md) for detailed instructions.

## License

Apache License 2.0 - see [LICENSE](LICENSE)
