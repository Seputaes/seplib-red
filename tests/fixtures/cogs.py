import pytest

from seplib.cog import SepCog

__all__ = ["empty_cog"]


@pytest.fixture()
def empty_cog(red_bot):
    class EmptyCog(SepCog):
        def __init__(self, bot):
            super(EmptyCog, self).__init__(bot=bot)

            self._ensure_futures()

        async def _init_cache(self):
            pass

        def _register_config_entities(self, config):
            pass

    return EmptyCog(bot=red_bot)
