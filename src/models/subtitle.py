from dataclasses import dataclass

@dataclass
class Subtitle:
    index: int
    start: float
    end: float
    text: str