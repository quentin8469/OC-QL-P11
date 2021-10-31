import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_user(client):
    """"""
    reponse = client.get('/')
    
    club = server.clubs[2]
    competition = server.competitions[0]

    assert reponse.status_code == 200
    reponse = client.post('/showSummary',
                      data={'email': club['email']})
    assert b'Welcome, kate@shelifts.co.uk' in reponse.data
    assert reponse.status_code == 200

    
    points = int(club['points'])
    reponse = client.post('/purchasePlaces',
                       data={'club': club['name'],
                             'competition': competition['name'],
                             'places': '1'}
                       )
    updated_points = int(club['points'])
    assert reponse.status_code == 200
    assert updated_points == 9
    assert updated_points != points
    