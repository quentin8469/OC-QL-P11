import server

server.app.config['TESTING'] = True
client = server.app.test_client()


def test_email_error():
    """ """
    reponse = client.post('/showSummary',
                           data={'email': 'admin@bob.com'})
    assert reponse.status_code == 302


def test_good_email():
    """"""
    reponse = client.post('/showSummary',
                           data={'email': 'john@simplylift.co'})
    assert reponse.status_code == 200