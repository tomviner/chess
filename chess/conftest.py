import pytest

from .game import Game
from .user import FakeUser


@pytest.fixture
def fake_user(monkeypatch):
    monkeypatch.setattr(Game, 'user_class', FakeUser)
    return FakeUser()
