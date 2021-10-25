import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients

def test_more_than_12_places(client):
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

def test_12_places(client):
    """
    """
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces', 
                         data={'club': club,
                                'competition': competition['name'],
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 12,
                               })
    assert result.status_code == 200


def test_less_than_12_places(client):
    """
    """
    club = server.clubs[0]['name']
    competition = server.competitions[0]
    result = client.post('/purchasePlaces', 
                         data={'club': club,
                                'competition': competition['name'],
                                'numberOfPlaces': competition['numberOfPlaces'],
                                'places': 3,
                               })
    assert result.status_code == 200
    

def test_clubs_table_points(client):
	reponse = client.get('/displayclubsPoints')
	assert reponse.status_code == 200
	assert server.clubs[0]["name"] in reponse.data.decode()
	assert server.clubs[1]["points"] in reponse.data.decode()