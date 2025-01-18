from dataclasses import dataclass
from src.shared.library import AbstractEntity


@dataclass
class Genre(AbstractEntity):
    name: str
