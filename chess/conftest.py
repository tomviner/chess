import pytest

from .game import Game
from .user import FakeUser


@pytest.fixture
def fake_user(monkeypatch):
    monkeypatch.setattr(Game, 'default_user_class', FakeUser)
    return FakeUser()
