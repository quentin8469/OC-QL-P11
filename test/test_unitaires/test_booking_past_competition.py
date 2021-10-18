import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_new_competitions_dates():
    """
    
    """
    pass


def test_past_competitions_dates():
    """
    
    """
    pass