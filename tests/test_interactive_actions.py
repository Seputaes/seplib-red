import pytest

from seplib.replies import InteractiveActions, SuccessReply


class TestInteractiveActions(object):
    @pytest.mark.asyncio
    async def test_message_xor_embed_provided(self, red_context):

        try:
            await InteractiveActions.yes_or_no_action(ctx=red_context, message=None, embed=None)
            assert False, "TypeError should have been raised, but wasn't"
        except TypeError:
            assert True

        try:
            embed = SuccessReply(message="").build()
            await InteractiveActions.yes_or_no_action(ctx=red_context, message="", embed=embed)
            assert False, "TypeError should have been raised, but wasn't"
        except TypeError:
            assert True
