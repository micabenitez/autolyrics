from dataclasses import dataclass, field
from pathlib import Path
from models.subtitle import Subtitle

@dataclass
class Song:
    path: Path

    vocals_path: Path | None = None
    srt_path: Path | None = None

    segments: list = field(default_factory=list)
    
    subtitles: list[Subtitle] = field(default_factory=list)

    @property
    def name(self):
        return self.path.name

    @property
    def extension(self):
        return self.path.suffix