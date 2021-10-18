import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_good_update_points_after_reservation():
    """ """
    club_points = 1
    reponse = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'numberOfPlaces': 10})
    
    assert reponse

def test_bad_update_points_after_reservation():
    """"""
    reponse = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'numberOfPlaces': 1})
    assert reponse

