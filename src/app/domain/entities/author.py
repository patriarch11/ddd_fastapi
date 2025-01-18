from dataclasses import dataclass
from src.shared.library import AbstractEntity


@dataclass
class Author(AbstractEntity):
    full_name: str
