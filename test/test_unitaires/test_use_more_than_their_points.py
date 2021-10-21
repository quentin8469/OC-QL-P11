import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_use_more_than_their_point(client):
    """
    """
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces', 
                         data={'club': club,
                                'competition': competition['name'],
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 100,
                               })
    assert result.status_code == 200


def test_use_less_than_their_point(client):
    """
    """
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces', 
                         data={'club': club,
                                'competition': competition['name'],
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 2,
                               })
    assert result.status_code == 200