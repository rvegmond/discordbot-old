"""
these tests should cover functions and classes in robin.py
"""
import sqlite3
import pytest
from mock import AsyncMock
from bot.modules.robin import Robin, _sanitize


def test_sanitize():
    """
    These tests will check if the strings get sanitized properly.
    """
    assert _sanitize(msg_in='Dit is een teststring') == 'Dit is een teststring'
    assert _sanitize(msg_in='TestString met een at @') == 'TestString met een at _'
    assert _sanitize(msg_in='TestString met een hash #') == 'TestString met een hash _'
    assert _sanitize(msg_in='TestString met een hash #') == 'TestString met een hash _'
    assert _sanitize(
        msg_in='TestString met een lange string',
        maxlength=20) == 'TestStr .. truncated'
    assert _sanitize(msg_in='Korte TestString', maxlength=12) == ' .. truncated'


@pytest.mark.asyncio
async def test_feedback():
    """
    These tests will check feedback result when everything is fine.
    """
    robin = Robin()
    ctx = AsyncMock()
    res = await robin._feedback(ctx=ctx, msg='Dit is een teststring')
    assert res == 'feedback sent successful'


@pytest.mark.asyncio
async def test_feedback_no_ctx():
    """
    These tests will check feedback result when contexts is nog spedified
    """
    robin = Robin()
    res = await robin._feedback(msg='Dit is een teststring')
    assert res == 'context not spedified'


@pytest.mark.asyncio
async def test_feedback_delete_failed():
    """
    These tests will check feedback result when deletion of msg failed.
    """
    robin = Robin()
    ctx = AsyncMock()
    ctx.message.delete.side_effect = Exception('Boom!')
    res = await robin._feedback(ctx=ctx, msg='Dit is een teststring', delete_message=True)
    assert res == 'message deletion failed Boom!'


@pytest.mark.asyncio
async def test_feedback_delete_message_wrong_argument():
    """
    These tests will check feedback result when wrong argument is specified.
    """
    robin = Robin()
    ctx = AsyncMock()
    res = await robin._feedback(ctx=ctx, msg='Dit is een teststring', delete_message=7)
    assert res == "Invallid option for delete_message 7"


@pytest.mark.asyncio
async def test_feedback_delete_message_fail():
    """
    These tests will check feedback result when deletion of msg succeeds.
    """
    robin = Robin()
    ctx = AsyncMock()
    res = await robin._feedback(ctx=ctx, msg='Dit is een teststring', delete_message=True)
    assert res == 'feedback sent successful'


@pytest.mark.asyncio
async def test_feedback_delete():
    """
    These tests will check feedback result when deletion of msg succeeds.
    """
    robin = Robin()
    ctx = AsyncMock()
    res = await robin._feedback(ctx=ctx, msg='Dit is een teststring', delete_after=4)
    assert res == 'feedback sent successful'


def test_usermap():
    """
    These tests will test update usermap.
    """
    robin = Robin()
    robin.conn = sqlite3.connect('tests/hades-test.db')
    res = robin._getusermap(1)
    assert res['discordid'] == 'discordid1'
