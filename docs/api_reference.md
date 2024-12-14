# API Reference

## iModel

Main interface for interacting with AI services.

```python
class iModel:
    def __init__(
        provider: str | Service,
        task: str = "chat",
        model: str = None,
        api_key: str = None,
        api_key_schema: str = None,
        interval_tokens: int = None,
        interval_requests: int = None,
        **kwargs
    )
```

### Parameters

- `provider`: Service name ("openai", "anthropic", etc.) or Service instance
- `task`: Task type (default: "chat")
- `model`: Model name
- `api_key`: API key for the service
- `api_key_schema`: Environment variable name for API key
- `interval_tokens`: Token limit per minute
- `interval_requests`: Request limit per minute

### Methods

```python
async def invoke(**kwargs)
```
Makes a request to the service.

```python
def list_tasks()
```
Lists available tasks for the service.

## RateLimiter

Handles rate limiting for tokens and requests.

```python
class RateLimiter:
    def __init__(
        limit_tokens: int = None,
        limit_requests: int = None
    )
```

### Methods

```python
def check_availability(
    request_token_len: int = 0,
    estimated_output_len: int = 0
) -> bool
```
Checks if request is within limits.

## TokenCalculator

Calculates token usage using tiktoken.

```python
class TiktokenCalculator:
    def __init__(encoding_name: str)
```

### Methods

```python
def calculate(text: str) -> int
```
Returns token count for text.

```python
def tokenize(
    text: str,
    decode_byte_str: bool = False,
    decoder: str = "utf-8"
) -> list
```
Returns list of tokens.

## Service

Base class for implementing service providers.

```python
@register_service
class CustomService(Service):
    def __init__(self):
        self.name = "custom_service"

    def list_tasks(self):
        return ["chat", "completion"]
```

## Exceptions

```python
class RateLimitError(Exception):
    def __init__(message: str, input_token_len: int, estimated_output_len: int)
```
Raised when rate limits are exceeded.
