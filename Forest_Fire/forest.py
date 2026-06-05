try:
    from .versions.simple_fire import SimpleFire
    from .versions.forest_age import ForestAge
except ImportError:
    from versions.simple_fire import SimpleFire
    from versions.forest_age import ForestAge

VERSIONS = {
    "simple fire": SimpleFire,
    "forest age": ForestAge,
}

def available_versions() -> list[str]:
    return list(VERSIONS.keys())


def forest_factory(version: str, horizontal_size: int = 64, vertical_size: int = 64, seed: int | None = None):
    version_key = version.lower()
    if version_key not in VERSIONS:
        raise ValueError(f"Version {version} not found. Available versions: {', '.join(available_versions())}")

    return VERSIONS[version_key](horizontal_size, vertical_size, seed)


if __name__ == "__main__":
    forest = forest_factory("forest age", horizontal_size=10, vertical_size=10, seed=42)
    forest.generate_forest()
    print(forest.grid)
