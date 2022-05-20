from typing import Any

from stripe import api_requestor as api_requestor
from stripe.api_resources.abstract import (
    CreateableAPIResource as CreateableAPIResource,
    ListableAPIResource as ListableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
    custom_method as custom_method,
)

class Charge(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str
    def capture(self, idempotency_key: Any | None = ..., **params): ...
    def refund(self, idempotency_key: Any | None = ..., **params): ...
    def update_dispute(self, idempotency_key: Any | None = ..., **params): ...
    def close_dispute(self, idempotency_key: Any | None = ..., **params): ...
    def mark_as_fraudulent(self, idempotency_key: Any | None = ...): ...
    def mark_as_safe(self, idempotency_key: Any | None = ...): ...
