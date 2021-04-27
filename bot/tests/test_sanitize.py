
from modules.robin import Robin
import pytest
import sqlite3


def test_sanitize():
    robin = Robin()
    assert robin._sanitize(msg_in='Dit is een teststring') == 'Dit is een teststring'
    assert robin._sanitize(msg_in='TestString met een at @') == 'TestString met een at _'
    assert robin._sanitize(msg_in='TestString met een hash #') == 'TestString met een hash _'
    assert robin._sanitize(msg_in='TestString met een hash #') == 'TestString met een hash _'
    assert robin._sanitize(msg_in='TestString met een lange string', maxlength=20) == 'TestStr .. truncated'
    assert robin._sanitize(msg_in='Korte TestString', maxlength=12) == ' .. truncated'


@pytest.mark.asyncio
async def test_feedback():
    robin = Robin()
    res = await robin._feedback(msg='Dit is een teststring')
    assert res == 'feedback sent successful'


def test_usermap():
    robin = Robin()
    robin.conn = sqlite3.connect('tests/hades-test.db')
    res = robin._getusermap(1)
    assert res['discordid'] == 'discordid1'