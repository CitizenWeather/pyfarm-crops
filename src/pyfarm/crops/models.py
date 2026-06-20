"""Data models for crops and cultivars."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class CropType(str, Enum):
    """Crop type enumeration."""
    MUSHROOM = "mushroom"
    MICROGREEN = "microgreen"


class PhenoPhaseType(str, Enum):
    """Phenological phase type."""
    COLONIZATION = "colonization"
    PINNING = "pinning"
    FRUITING = "fruiting"
    HARVEST = "harvest"


@dataclass
class Range:
    """A numeric range with min and max."""
    min: float = 0.0
    max: float = 100.0

    def __post_init__(self):
        if self.min > self.max:
            raise ValueError(f"min ({self.min}) cannot exceed max ({self.max})")

    def contains(self, value: float) -> bool:
        return self.min <= value <= self.max

    def clamp(self, value: float) -> float:
        return max(self.min, min(self.max, value))


@dataclass
class PhenoPhase:
    """A phenological phase of a cultivar."""
    stage: str = ""
    duration_days: int = 0
    light_dli: Optional[float] = None
    temperature: Range = field(default_factory=lambda: Range(15, 25))
    humidity: Range = field(default_factory=lambda: Range(60, 80))

    def __post_init__(self):
        if not self.stage:
            raise ValueError("stage is required")
        if self.duration_days <= 0:
            raise ValueError("duration_days must be positive")


@dataclass
class Cultivar:
    """A crop cultivar with optimal growing conditions."""
    id: str = ""
    species: str = ""
    name: str = ""
    crop_type: CropType = CropType.MICROGREEN
    phenophases: list[PhenoPhase] = field(default_factory=list)
    optimal_light_dli: Optional[float] = None
    optimal_temperature: Range = field(default_factory=lambda: Range(15, 25))
    optimal_humidity: Range = field(default_factory=lambda: Range(60, 80))
    optimal_ec: Optional[Range] = None
    optimal_ph: Optional[Range] = None
    cycle_days: int = 0
    yield_g_per_m2: float = 0.0
    source: str = ""

    def __post_init__(self):
        if not self.id:
            raise ValueError("id is required")
        if not self.name:
            raise ValueError("name is required")
        if self.cycle_days <= 0:
            raise ValueError("cycle_days must be positive")
