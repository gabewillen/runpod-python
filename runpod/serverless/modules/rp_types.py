"""
This module defines custom types and type hints for the RunPod Serverless Worker.

It includes:
- Custom TypedDict classes for job and configuration data structures
- Type aliases for different handler function signatures
- Type variables and parameter specifications for generic typing

Note: These types are intentionally verbose and explicit to make them understanble and prevent conflicts with other types.
      Additionally, you can use these with `Unpack` to accept them as keyword arguments.

"""

import typing
from typing import Annotated


try:
    # For Python 3.8 and newer versions
    from typing import TypedDict
except ImportError:
    # For Python 3.7 and older versions
    from typing_extensions import TypedDict

__all__ = [
    "RunpodServerlessWorkerJob",
    "RunpodServerlessWorkerStartConfigRunpodArgs",
    "RunpodServerlessWorkerStartConfig",
    "RunpodServerlessWorkerSyncHandler",
    "RunpodServerlessWorkerAsyncHandler",
    "RunpodServerlessWorkerGeneratorHandler",
]

R = typing.TypeVar("ReturnType")


# job type add any job related info here alternatively you can extend this type for custom job types. This is purely for type hinting and to improve developer experience.
class RunpodServerlessWorkerJob(TypedDict):
    id: Annotated[str, "Unique identifier for the job"]


P = typing.ParamSpec("Parameters", bound=RunpodServerlessWorkerJob)

# handler types
RunpodServerlessWorkerSyncHandler = Annotated[
    typing.Callable[P, typing.Iterable],
    "Synchronous handler function that returns an Iterable",
]
RunpodServerlessWorkerAsyncHandler = Annotated[
    typing.Callable[P, typing.AsyncIterable],
    "Asynchronous handler function that returns an AsyncIterable",
]
RunpodServerlessWorkerGeneratorHandler = Annotated[
    typing.Callable[P, typing.Generator[typing.Iterable, None, None]],
    "Generator handler function that yields Iterables",
]


class RunpodServerlessWorkerStartConfigRunpodArgs(TypedDict):
    rp_log_level: Annotated[typing.Optional[str], "Log level for the worker"]
    rp_debugger: Annotated[typing.Optional[bool], "Flag to enable debugger"]
    rp_serve_api: Annotated[typing.Optional[bool], "Flag to serve API"]
    rp_api_port: Annotated[typing.Optional[int], "Port for API server"]
    rp_api_concurrency: Annotated[typing.Optional[int], "Concurrency for API server"]
    rp_api_host: Annotated[typing.Optional[str], "Host for API server"]
    test_input: Annotated[typing.Optional[str], "Test input for the worker"]


class RunpodServerlessWorkerStartConfig(TypedDict):
    handler: Annotated[
        typing.Union[
            RunpodServerlessWorkerSyncHandler,
            RunpodServerlessWorkerAsyncHandler,
            RunpodServerlessWorkerGeneratorHandler,
        ],
        "Handler function for processing jobs",
    ]
    return_aggregate_stream: Annotated[
        typing.Optional[bool], "Flag to return aggregate stream"
    ]
    concurrency_modifier: Annotated[
        typing.Optional[typing.Callable[[int], int]],
        "Function to modify concurrency",
    ]
    rp_args: Annotated[
        typing.Optional[RunpodServerlessWorkerStartConfigRunpodArgs],
        "RunPod specific arguments",
    ]
