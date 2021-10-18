import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_good_update_points_after_reservation(client):
    """ """
    club_points = server.clubs[0]['points']
    print(club_points)
    reponse = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'numberOfPlaces': 25})
    update_points = club_points
    assert club_points != update_points


def test_bad_update_points_after_reservation(client):
    """"""
    club_points = 13
    reponse = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'numberOfPlaces': 25})
    update_points = club_points
    assert club_points == update_points

