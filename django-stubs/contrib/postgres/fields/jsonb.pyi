from django.db.models import JSONField as BuiltinJSONField

class JSONField(BuiltinJSONField): ...

__all__ = ["JSONField"]
