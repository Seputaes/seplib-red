import asyncio
import hashlib
import types
import warnings

import pytest

from redbot.core import Config
from seplib.tests.utils.functions import simple_coroutine

from seplib.cog import SepCog


class TestSepCog(object):
    def test_bot_set(self, empty_cog, red_bot):
        assert isinstance(empty_cog.bot, type(red_bot))

    def test_config_created(self, empty_cog):
        assert isinstance(empty_cog.config, Config)

    def test_config_cog_instance_used(self, empty_cog):
        assert empty_cog.config.cog_name == empty_cog.__class__.__name__

    def test_config_force_registration(self, empty_cog):
        assert empty_cog.config.force_registration is True

    def test_config_identifier(self, empty_cog):
        id_bytes = f"{empty_cog.COG_CONFIG_SALT}{empty_cog.__class__.__name__}".encode("UTF-8")
        identifier = int(hashlib.sha512(id_bytes).hexdigest(), 16)
        config_hash = str(hash(identifier))
        assert empty_cog.config.unique_identifier == config_hash

    def test_init_cache_added(self, empty_cog):
        assert len(empty_cog._futures) == 1
        _init_cache = empty_cog._futures[0]
        assert isinstance(_init_cache, types.CoroutineType)
        assert _init_cache.cr_code.co_name == SepCog._init_cache.__name__

    @pytest.mark.asyncio
    async def test_init_cache_not_implemented(self, empty_cog):
        try:
            await SepCog._init_cache(empty_cog)
            assert False, "NotImplementedError was not thrown on abstract method."
        except NotImplementedError:
            assert True

    @pytest.mark.asyncio
    async def test_register_configs_not_implemented(self, empty_cog, red_config):
        try:
            await SepCog._register_config_entities(empty_cog, config=red_config)
            assert False, "NotImplementedError was not thrown on abstract method."
        except NotImplementedError:
            assert True

    @pytest.mark.asyncio
    async def test_add_futures(self, empty_cog):
        empty_future_count = 0
        future_name = "empty_future"

        empty_cog._add_future(simple_coroutine(future_name))

        for future in empty_cog._futures:
            if future.cr_code.co_name == future_name:
                empty_future_count += 1
        assert empty_future_count == 1, "Future not added to futures list correctly."
