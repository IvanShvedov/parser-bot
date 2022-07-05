from dataclasses import dataclass, asdict


@dataclass
class Base:
    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if v is not None}