from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Reset the in-memory activity data before each test and restore it afterward."""
    original = deepcopy(activities)
    activities.clear()
    activities.update(deepcopy(original))

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(deepcopy(original))
