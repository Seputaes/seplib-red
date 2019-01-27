import hashlib

import pytest
from discord.abc import Messageable

from redbot.core.drivers.red_base import BaseDriver

from redbot.core import Config

from redbot.core.bot import Red

__all__ = [
    "red_bot",
    "red_base_driver",
    "red_config",
    "red_context",
    "discord_message",
    "discord_connection",
    "discord_messageable",
]


@pytest.fixture()
def red_bot():
    from redbot.core.cli import parse_cli_flags

    cli_flags = parse_cli_flags([])
    description = "seplib pytest"
    red = Red(cli_flags=cli_flags, description=description)
    yield red


@pytest.fixture()
def red_base_driver():
    id_ = int(hashlib.sha1("Pytest Cog".encode("UTF-8")).hexdigest(), 16)
    return BaseDriver(cog_name="Pytest Cog", identifier=id_)


@pytest.fixture()
def red_config(red_base_driver):
    return Config(
        cog_name=red_base_driver.cog_name,
        unique_identifier=red_base_driver.unique_cog_identifier,
        driver=red_base_driver,
    )


@pytest.fixture()
def discord_connection():
    class ConnectionState(object):
        http = None

    return ConnectionState()


@pytest.fixture()
def discord_messageable():
    from discord.abc import Messageable

    class M(Messageable):
        async def _get_channel(self):
            return self

    return M()


@pytest.fixture()
def discord_message(discord_messageable, discord_connection):
    from discord import Message

    return Message(channel=discord_messageable, data={"id": 1}, state=discord_connection)


@pytest.fixture()
def red_context(discord_message):
    from redbot.core.commands import Context

    return Context(prefix="!", message=discord_message)
