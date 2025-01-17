from abc import ABC
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class AbstractEntity(ABC):
    id: int | None
    created_at: datetime | None
    updated_at: datetime | None

    def to_dict(self,
                exclude: set[str] | None = None,
                include: dict[str, Any] | None = None,
                ) -> dict[str, Any]:
        data: dict[str, Any] = asdict(self)
        if exclude:
            for key in exclude:
                try:
                    del data[key]
                except KeyError:
                    pass

        if include:
            data.update(include)

        return data
