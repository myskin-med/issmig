import pathlib
import types
from typing import IO, Any, AnyStr, Iterable, Self

import paramiko.transport
from _typeshed import Incomplete

__version__: str
SCP_COMMAND: bytes
PATH_TYPES: Incomplete
PurePath = pathlib.PurePath
PathTypes = str | bytes | PurePath


bytes_sep: Incomplete


class SCPClient:
    transport: Incomplete
    buff_size: Incomplete
    socket_timeout: Incomplete
    channel: Incomplete
    preserve_times: bool
    sanitize: Incomplete
    peername: Incomplete
    scp_command: Incomplete

    def __init__(self,
                 transport: paramiko.transport.Transport,
                 buff_size: int = 16384,
                 socket_timeout: float = 10.0,
                 progress: Incomplete | None = None,
                 progress4: Incomplete | None = None,
                 sanitize: Any = None,
                 limit_bw: Incomplete | None = None
                 ) -> None: ...

    def __enter__(self) -> Self: ...

    def __exit__(self, type: type[BaseException] | None, value: BaseException |
                 None, traceback: types.TracebackType | None) -> None: ...

    def put(self, files: PathTypes | Iterable[PathTypes], remote_path: str |
            bytes = b'.', recursive: bool = False, preserve_times: bool = False) -> None: ...

    def putfo(self, fl: IO[AnyStr], remote_path: str | bytes, mode: str |
              bytes = '0644', size: int | None = None) -> None: ...
    def get(self, remote_path: PathTypes, local_path: str | bytes = '',
            recursive: bool = False, preserve_times: bool = False) -> None: ...

    def close(self) -> None: ...


class SCPException(Exception):
    ...


def put(transport: paramiko.transport.Transport, files: PathTypes |
        Iterable[PathTypes], remote_path: str | bytes = b'.', recursive: bool = False, preserve_times: bool = False) -> None: ...


def get(transport: paramiko.transport.Transport, remote_path: PathTypes, local_path: str |
        bytes = '', recursive: bool = False, preserve_times: bool = False) -> None: ...
