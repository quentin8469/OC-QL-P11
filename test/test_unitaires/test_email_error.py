import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_unknow_email():
    """ """
    reponse = client.post('/showSummary',
                           data={'email': 'admin@bob.com'})
    assert reponse


def test_empty_email():
    """ """
    reponse = client.post('/showSummary',
                           data={'email': ''})
    assert reponse


def test_know_email():
    """"""
    reponse = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'})
    assert reponse

def test_not_a_email():
    """"""
    reponse = client.post('/showSummary',
                           data={'email': '1585d456qef'})
    assert reponse