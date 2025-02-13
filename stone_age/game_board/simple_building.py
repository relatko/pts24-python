from typing import Iterable, Optional
from stone_age.simple_types import Effect
from stone_age.game_board. interfaces import Building


class SimpleBuilding(Building):
    _required_resources: list[Effect]

    def __init__(self, resources: Iterable[Effect]):
        assert all(Effect.is_resource(x) for x in resources)
        self._required_resources = list(resources)

    def build(self, resources: Iterable[Effect]) -> Optional[int]:
        if not all(Effect.is_resource(x) for x in resources):
            return None
        if sorted(self._required_resources) != sorted(resources):
            return None
        return sum(Effect.points(x) for x in resources)
