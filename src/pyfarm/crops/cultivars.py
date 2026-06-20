"""Phase 1 cultivar data: mushrooms and microgreens."""

from pyfarm.crops.models import Cultivar, CropType, PhenoPhase, Range

# Mushroom cultivars

OYSTER_GREY = Cultivar(
    id="oyster-grey-strain-a",
    species="Pleurotus",
    name="Grey Oyster",
    crop_type=CropType.MUSHROOM,
    phenophases=[
        PhenoPhase(
            stage="colonization",
            duration_days=21,
            temperature=Range(20, 25),
            humidity=Range(70, 85),
        ),
        PhenoPhase(
            stage="pinning",
            duration_days=7,
            temperature=Range(15, 20),
            humidity=Range(85, 95),
            light_dli=4.0,
        ),
        PhenoPhase(
            stage="fruiting",
            duration_days=7,
            temperature=Range(15, 20),
            humidity=Range(80, 90),
            light_dli=8.0,
        ),
    ],
    optimal_temperature=Range(15, 25),
    optimal_humidity=Range(70, 90),
    cycle_days=35,
    yield_g_per_m2=800,
    source="Citizen Weather Strain A",
)

SHIITAKE_DARK_OAK = Cultivar(
    id="shiitake-dark-oak",
    species="Lentinula",
    name="Dark Oak Shiitake",
    crop_type=CropType.MUSHROOM,
    phenophases=[
        PhenoPhase(
            stage="colonization",
            duration_days=30,
            temperature=Range(18, 24),
            humidity=Range(65, 80),
        ),
        PhenoPhase(
            stage="initiation",
            duration_days=5,
            temperature=Range(10, 15),
            humidity=Range(85, 95),
        ),
        PhenoPhase(
            stage="fruiting",
            duration_days=10,
            temperature=Range(12, 18),
            humidity=Range(80, 95),
            light_dli=6.0,
        ),
    ],
    optimal_temperature=Range(12, 24),
    optimal_humidity=Range(65, 95),
    cycle_days=45,
    yield_g_per_m2=600,
    source="Citizen Weather Oak Strain",
)

LIONS_MANE_STANDARD = Cultivar(
    id="lions-mane-standard",
    species="Hericium",
    name="Lion's Mane",
    crop_type=CropType.MUSHROOM,
    phenophases=[
        PhenoPhase(
            stage="colonization",
            duration_days=24,
            temperature=Range(20, 25),
            humidity=Range(70, 85),
        ),
        PhenoPhase(
            stage="pinning",
            duration_days=8,
            temperature=Range(15, 20),
            humidity=Range(85, 95),
            light_dli=3.0,
        ),
        PhenoPhase(
            stage="fruiting",
            duration_days=8,
            temperature=Range(15, 18),
            humidity=Range(80, 90),
            light_dli=6.0,
        ),
    ],
    optimal_temperature=Range(15, 25),
    optimal_humidity=Range(70, 90),
    cycle_days=40,
    yield_g_per_m2=700,
    source="Citizen Weather Hericium Standard",
)

# Microgreens cultivars

RADISH_MICROGREEN = Cultivar(
    id="radish-microgreen",
    species="Raphanus sativus",
    name="Radish Microgreen",
    crop_type=CropType.MICROGREEN,
    phenophases=[
        PhenoPhase(
            stage="germination",
            duration_days=2,
            temperature=Range(20, 25),
            humidity=Range(80, 95),
        ),
        PhenoPhase(
            stage="growth",
            duration_days=5,
            temperature=Range(18, 22),
            humidity=Range(65, 80),
            light_dli=12.0,
        ),
    ],
    optimal_light_dli=12.0,
    optimal_temperature=Range(18, 25),
    optimal_humidity=Range(60, 90),
    cycle_days=7,
    yield_g_per_m2=150,
    source="Standard Radish Seed",
)

BROCCOLI_MICROGREEN = Cultivar(
    id="broccoli-microgreen",
    species="Brassica oleracea",
    name="Broccoli Microgreen",
    crop_type=CropType.MICROGREEN,
    phenophases=[
        PhenoPhase(
            stage="germination",
            duration_days=2,
            temperature=Range(20, 25),
            humidity=Range(80, 95),
        ),
        PhenoPhase(
            stage="establishment",
            duration_days=3,
            temperature=Range(18, 22),
            humidity=Range(70, 85),
            light_dli=6.0,
        ),
        PhenoPhase(
            stage="growth",
            duration_days=5,
            temperature=Range(18, 22),
            humidity=Range(60, 75),
            light_dli=14.0,
        ),
    ],
    optimal_light_dli=14.0,
    optimal_temperature=Range(18, 25),
    optimal_humidity=Range(60, 85),
    cycle_days=10,
    yield_g_per_m2=120,
    source="Standard Broccoli Seed",
)

SUNFLOWER_MICROGREEN = Cultivar(
    id="sunflower-microgreen",
    species="Helianthus annuus",
    name="Sunflower Microgreen",
    crop_type=CropType.MICROGREEN,
    phenophases=[
        PhenoPhase(
            stage="germination",
            duration_days=2,
            temperature=Range(20, 25),
            humidity=Range(80, 95),
        ),
        PhenoPhase(
            stage="growth",
            duration_days=8,
            temperature=Range(18, 23),
            humidity=Range(60, 75),
            light_dli=10.0,
        ),
    ],
    optimal_light_dli=10.0,
    optimal_temperature=Range(18, 25),
    optimal_humidity=Range(60, 80),
    cycle_days=10,
    yield_g_per_m2=180,
    source="Standard Sunflower Seed",
)

PEA_SHOOTS_MICROGREEN = Cultivar(
    id="pea-shoots-microgreen",
    species="Pisum sativum",
    name="Pea Shoots",
    crop_type=CropType.MICROGREEN,
    phenophases=[
        PhenoPhase(
            stage="germination",
            duration_days=2,
            temperature=Range(20, 25),
            humidity=Range(80, 95),
        ),
        PhenoPhase(
            stage="growth",
            duration_days=7,
            temperature=Range(18, 23),
            humidity=Range(65, 80),
            light_dli=8.0,
        ),
    ],
    optimal_light_dli=8.0,
    optimal_temperature=Range(18, 25),
    optimal_humidity=Range(60, 85),
    cycle_days=9,
    yield_g_per_m2=140,
    source="Standard Pea Seed",
)

ALFALFA_MICROGREEN = Cultivar(
    id="alfalfa-microgreen",
    species="Medicago sativa",
    name="Alfalfa Microgreen",
    crop_type=CropType.MICROGREEN,
    phenophases=[
        PhenoPhase(
            stage="germination",
            duration_days=2,
            temperature=Range(20, 25),
            humidity=Range(80, 95),
        ),
        PhenoPhase(
            stage="growth",
            duration_days=6,
            temperature=Range(18, 22),
            humidity=Range(60, 75),
            light_dli=6.0,
        ),
    ],
    optimal_light_dli=6.0,
    optimal_temperature=Range(18, 24),
    optimal_humidity=Range(60, 80),
    cycle_days=8,
    yield_g_per_m2=100,
    source="Standard Alfalfa Seed",
)

# Phase 1 cultivar registry
PHASE_1_CULTIVARS = [
    OYSTER_GREY,
    SHIITAKE_DARK_OAK,
    LIONS_MANE_STANDARD,
    RADISH_MICROGREEN,
    BROCCOLI_MICROGREEN,
    SUNFLOWER_MICROGREEN,
    PEA_SHOOTS_MICROGREEN,
    ALFALFA_MICROGREEN,
]
