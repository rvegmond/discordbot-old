"""
The contents of this file is to reflect happyness of robin.
"""
from discord.ext import commands
from ..robin import Robin
from ..utils import feedback


class Ping(Robin):
    """
    Are you happy Robin?
    """

    @commands.command(
        name="ping",
        help=(
            "Commando om te zien of de bot nog leeft."
            "Als de bot een redelijk blije bot is krijg je en pong terug."
            "Een blije bot is geen garantie op succes en gezondheid...."
        ),
        brief="Commando om te zien of de bot nog leeft.",
    )
    async def command(self, ctx):
        """
        Are you there Robin? should reply a pong.
        """
        await feedback(ctx, msg="pong")
