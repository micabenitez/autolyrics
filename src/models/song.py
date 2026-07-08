from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Song:
    path: Path

    vocals_path: Path | None = None
    srt_path: Path | None = None

    language: str | None = None
    language_probability: float | None = None

    segments: list = field(default_factory=list)

    @property
    def name(self):
        return self.path.stem

    @property
    def extension(self):
        return self.path.suffix