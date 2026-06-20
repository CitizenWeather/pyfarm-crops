"""In-memory cultivar registry implementation."""

from __future__ import annotations

from typing import Optional

from pyfarm.crops.cultivars import PHASE_1_CULTIVARS
from pyfarm.crops.models import Cultivar, CropType
from pyfarm.crops.registry import CultivarRegistry


class MemoryRegistry(CultivarRegistry):
    """In-memory cultivar registry."""

    def __init__(self):
        """Initialize registry with Phase 1 cultivars."""
        self._cultivars: dict[str, Cultivar] = {}
        for cultivar in PHASE_1_CULTIVARS:
            self._cultivars[cultivar.id] = cultivar

    async def get_cultivar(self, cultivar_id: str) -> Optional[Cultivar]:
        """Get a cultivar by ID."""
        return self._cultivars.get(cultivar_id)

    async def list_cultivars(
        self,
        crop_type: Optional[CropType] = None,
    ) -> list[Cultivar]:
        """List all cultivars, optionally filtered by crop type."""
        cultivars = list(self._cultivars.values())
        if crop_type:
            cultivars = [c for c in cultivars if c.crop_type == crop_type]
        return cultivars

    async def add_cultivar(self, cultivar: Cultivar) -> None:
        """Add a new cultivar to the registry."""
        self._cultivars[cultivar.id] = cultivar
