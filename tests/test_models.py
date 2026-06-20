"""Tests for crop models."""

import pytest

from pyfarm.crops.models import Cultivar, CropType, PhenoPhase, Range


def test_range_contains():
    r = Range(min=15, max=25)
    assert r.contains(20)
    assert not r.contains(10)
    assert not r.contains(30)


def test_range_clamp():
    r = Range(min=0, max=100)
    assert r.clamp(-10) == 0
    assert r.clamp(50) == 50
    assert r.clamp(150) == 100


def test_range_invalid():
    with pytest.raises(ValueError):
        Range(min=25, max=15)


def test_phenophase_creation():
    phase = PhenoPhase(stage="fruiting", duration_days=7)
    assert phase.stage == "fruiting"
    assert phase.duration_days == 7


def test_phenophase_invalid_duration():
    with pytest.raises(ValueError):
        PhenoPhase(stage="fruiting", duration_days=0)


def test_cultivar_creation():
    cultivar = Cultivar(
        id="oyster-grey",
        name="Grey Oyster",
        crop_type=CropType.MUSHROOM,
        cycle_days=35,
    )
    assert cultivar.id == "oyster-grey"
    assert cultivar.name == "Grey Oyster"
    assert cultivar.crop_type == CropType.MUSHROOM


def test_cultivar_missing_id():
    with pytest.raises(ValueError):
        Cultivar(name="Test", cycle_days=10)
