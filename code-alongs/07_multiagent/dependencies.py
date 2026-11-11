from dataclasses import dataclass
from typing import Literal


@dataclass
class ClientDeps:
    name: str
    goal: str
    experience_lvl: Literal["beginer", "intermediate", "advanced"] = "beginer"
    weekly_hours: int = 8
    current_role: str | None = None