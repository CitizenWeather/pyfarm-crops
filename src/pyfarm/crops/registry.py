"""Cultivar registry interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from pyfarm.crops.models import Cultivar, CropType


class CultivarRegistry(ABC):
    """Interface for querying cultivars."""

    @abstractmethod
    async def get_cultivar(self, cultivar_id: str) -> Optional[Cultivar]:
        """Get a cultivar by ID."""
        pass

    @abstractmethod
    async def list_cultivars(
        self,
        crop_type: Optional[CropType] = None,
    ) -> list[Cultivar]:
        """List all cultivars, optionally filtered by crop type."""
        pass

    @abstractmethod
    async def add_cultivar(self, cultivar: Cultivar) -> None:
        """Add a new cultivar to the registry."""
        pass
