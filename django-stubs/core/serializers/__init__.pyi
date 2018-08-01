# Stubs for django.core.serializers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from collections import OrderedDict
from django.apps.config import AppConfig
from django.contrib.admin.apps import SimpleAdminConfig
from django.contrib.sites.apps import SitesConfig
from django.core.serializers.json import Serializer
from django.core.serializers.python import Serializer
from django.core.serializers.xml_serializer import Deserializer, Serializer
from django.db.models.base import Model
from django.db.models.query import QuerySet
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

BUILTIN_SERIALIZERS: Any
_serializers: Any

class BadSerializer:
    internal_use_only: bool = ...
    exception: Any = ...
    def __init__(self, exception: ModuleNotFoundError) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...

def register_serializer(
    format: str, serializer_module: str, serializers: Dict[str, Any] = ...
) -> None: ...
def unregister_serializer(format: Any) -> None: ...
def get_serializer(
    format: str
) -> Union[Type[Serializer], Type[Serializer], Type[Serializer], BadSerializer]: ...
def get_serializer_formats(): ...
def get_public_serializer_formats() -> List[str]: ...
def get_deserializer(format: str) -> Union[Type[Deserializer], Callable]: ...
def serialize(
    format: str, queryset: Union[List[Model], QuerySet], **options: Any
) -> Optional[Union[str, List[OrderedDict]]]: ...
def deserialize(format: str, stream_or_string: Any, **options: Any) -> Deserializer: ...
def _load_serializers() -> None: ...
def sort_dependencies(
    app_list: Union[
        List[Tuple[str, List[Type[Model]]]],
        List[
            Union[
                Tuple[SitesConfig, None],
                Tuple[SimpleAdminConfig, None],
                Tuple[AppConfig, None],
            ]
        ],
        List[Union[Tuple[SitesConfig, None], Tuple[SimpleAdminConfig, None]]],
    ]
) -> List[Type[Model]]: ...