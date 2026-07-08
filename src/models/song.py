from dataclasses import dataclass
from pathlib import Path


@dataclass
class Song:
    path: Path
    vocals_path: Path | None = None
    srt_path: Path | None = None

    @property
    def name(self):
        return self.path.stem

    @property
    def extension(self):
        return self.path.suffix