import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients

def test_more_than_12_places():
    """
    """
    pass

def test_12_places():
    """
    """
    pass


def test_less_than_12_places():
    """
    """
    pass