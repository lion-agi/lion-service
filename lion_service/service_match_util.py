import inspect
import re
import warnings
from os import getenv

from .service import ServiceSetting

imported_services = {}


def match_service(service_name: str, **kwargs):
    service_name = service_name.lower()

    def check_key_match(key1, key2):
        if key1 is not None:
            key1 = getenv(key1) if getenv(key1) else key1
        if key2 is not None:
            key2 = getenv(key2) if getenv(key2) else key2
        return key1 == key2

    if service_name == "openai":
        try:
            from lion_openai import OpenAIService
        except ImportError:
            raise ImportError(
                "To use OpenAI, please install the `lion_openai` package"
            )

        api_key = kwargs.get("api_key")
        openai_organization = kwargs.get("openai_organization")
        openai_project = kwargs.get("openai_project")

        for service in ServiceSetting.services.values():
            if isinstance(service, OpenAIService):
                if (
                    check_key_match(service.api_key, api_key)
                    and check_key_match(
                        service.openai_organization, openai_organization
                    )
                    and check_key_match(service.openai_project, openai_project)
                ):
                    return service

        # when no matching
        return OpenAIService(
            api_key=api_key,
            openai_organization=openai_organization,
            openai_project=openai_project,
        )

    elif service_name == "anthropic":
        try:
            from lion_anthropic import AnthropicService
        except ImportError:
            raise ImportError(
                "To use Anthropic, please install the `lion_anthropic` package"
            )

        api_key = kwargs.get("api_key")
        api_version = kwargs.get("api_version", "2023-06-01")

        for service in ServiceSetting.services.values():
            if isinstance(service, AnthropicService):
                if check_key_match(
                    service.api_key, api_key
                ) and check_key_match(service.api_version, api_version):
                    return service

        # when no matching
        return AnthropicService(
            api_key=api_key,
            api_version=api_version,
        )

    elif service_name == "perplexity":
        try:
            from lion_perplexity import PerplexityService
        except ImportError:
            raise ImportError(
                "To use Perplexity, please install the `lion_perplexity` package"
            )

        api_key = kwargs.get("api_key")
        api_version = kwargs.get("api_version", "2023-06-01")

        for service in ServiceSetting.services.values():
            if isinstance(service, PerplexityService):
                if check_key_match(service.api_key, api_key):
                    return service

        # when no matching
        return PerplexityService(api_key=api_key)

    elif service_name == "groq":
        try:
            from lion_groq import GroqService
        except ImportError:
            raise ImportError(
                "To use Groq, please install the `lion_groq` package"
            )

        api_key = kwargs.get("api_key")
        for service in ServiceSetting.services.values():
            if isinstance(service, GroqService):
                if check_key_match(service.api_key, api_key):
                    return service

        # when no matching
        return GroqService(api_key=api_key)

    raise ValueError(f"Service {service_name} is not available")


def match_task_method(task_name, service_obj):
    def clean_name(name):
        return re.sub(r"[^a-zA-Z0-9]", "", name).lower()

    task_name = clean_name(task_name)
    if task_name.endswith("s"):
        task_name = task_name[:-1]
    methods = [
        method_name
        for method_name in dir(service_obj)
        if task_name in clean_name(method_name)
    ]
    return methods


def match_parameters(method, model, interval_tokens, interval_requests):
    method_params = inspect.signature(method).parameters
    kwargs = {}
    if "model" in method_params:
        kwargs["model"] = model
    if "limit_requests" in method_params:
        kwargs["limit_requests"] = interval_requests
    else:
        # no limit_requests but interval_requests provided
        if interval_requests is not None:
            warnings.warn(
                f"The system does not support tracking limit requests per minute for {method.__name__}"
            )
    if "limit_tokens" in method_params:
        kwargs["limit_tokens"] = interval_tokens
    else:
        # no limit_tokens but interval_tokens provided
        if interval_tokens is not None:
            warnings.warn(
                f"The system does not support tracking limit tokens per minute for {method.__name__}"
            )

    return kwargs
