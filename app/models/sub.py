from dataclasses import dataclass
from models.base import Base


@dataclass
class SubDTO(Base):
    id: str = None
    sub: str = None