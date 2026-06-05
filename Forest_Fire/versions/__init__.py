try:
    from .simple_fire import SimpleFire
    from .forest_age import ForestAge
except ImportError:
    from simple_fire import SimpleFire
    from forest_age import ForestAge

__all__ = ["SimpleFire", "ForestAge"]
