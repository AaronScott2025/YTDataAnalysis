from collections import Counter
from dataclasses import dataclass, field

@dataclass
class videoItem:
    weight: float
    color: Counter = field(default_factory=Counter)
    title: Counter = field(default_factory=Counter)
    description: Counter = field(default_factory=Counter)

    def __post_init__(self):
        # Convert single string values into Counters
        if isinstance(self.color, str):
            self.color = Counter([self.color])
        if isinstance(self.title, str):
            self.title = Counter(self.title.split())
        if isinstance(self.description, str):
            self.description = Counter(self.description.split())

    def __repr__(self):
        return (
            f"VideoItem(\n"
            f"  weight={self.weight},\n"
            f"  color_counter={self.color},\n"
            f"  title_counter={self.title},\n"
            f"  description_counter={self.description}\n"
            f")"
        )
