"""Tests for cultivar registry."""

import pytest

from pyfarm.crops import (
    ALFALFA_MICROGREEN,
    OYSTER_GREY,
    CropType,
    MemoryRegistry,
)


@pytest.mark.asyncio
async def test_get_cultivar():
    registry = MemoryRegistry()
    cultivar = await registry.get_cultivar("oyster-grey-strain-a")
    assert cultivar is not None
    assert cultivar.name == "Grey Oyster"
    assert cultivar.cycle_days == 35


@pytest.mark.asyncio
async def test_get_cultivar_missing():
    registry = MemoryRegistry()
    cultivar = await registry.get_cultivar("nonexistent")
    assert cultivar is None


@pytest.mark.asyncio
async def test_list_all_cultivars():
    registry = MemoryRegistry()
    cultivars = await registry.list_cultivars()
    assert len(cultivars) == 8  # 3 mushrooms + 5 microgreens
    ids = [c.id for c in cultivars]
    assert "oyster-grey-strain-a" in ids
    assert "radish-microgreen" in ids


@pytest.mark.asyncio
async def test_list_mushrooms():
    registry = MemoryRegistry()
    cultivars = await registry.list_cultivars(crop_type=CropType.MUSHROOM)
    assert len(cultivars) == 3
    assert all(c.crop_type == CropType.MUSHROOM for c in cultivars)


@pytest.mark.asyncio
async def test_list_microgreens():
    registry = MemoryRegistry()
    cultivars = await registry.list_cultivars(crop_type=CropType.MICROGREEN)
    assert len(cultivars) == 5
    assert all(c.crop_type == CropType.MICROGREEN for c in cultivars)


@pytest.mark.asyncio
async def test_add_cultivar():
    from pyfarm.crops import Cultivar, PhenoPhase, Range

    registry = MemoryRegistry()
    new_cultivar = Cultivar(
        id="test-cultivar",
        name="Test",
        crop_type=CropType.MICROGREEN,
        cycle_days=10,
    )
    await registry.add_cultivar(new_cultivar)

    retrieved = await registry.get_cultivar("test-cultivar")
    assert retrieved is not None
    assert retrieved.name == "Test"


@pytest.mark.asyncio
async def test_oyster_phenophases():
    registry = MemoryRegistry()
    oyster = await registry.get_cultivar("oyster-grey-strain-a")
    assert len(oyster.phenophases) == 3
    assert oyster.phenophases[0].stage == "colonization"
    assert oyster.phenophases[1].stage == "pinning"
    assert oyster.phenophases[2].stage == "fruiting"
    # Verify DLI is set for fruiting phase
    assert oyster.phenophases[2].light_dli == 8.0


@pytest.mark.asyncio
async def test_microgreen_ec_ph_ranges():
    registry = MemoryRegistry()
    radish = await registry.get_cultivar("radish-microgreen")
    # Microgreens don't have EC/pH since they're soil-based in Phase 1
    assert radish.optimal_ec is None
    assert radish.optimal_ph is None
