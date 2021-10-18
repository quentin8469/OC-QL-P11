from datetime import datetime
import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients


def test_new_competitions_dates(client):
    """
    check if the competition date is still valid
    """
    date = datetime.today()
    date_competition = datetime.strptime(server.competitions[0]['date'], '%Y-%m-%d %H:%M:%S')
    if date_competition < date:
        today=True
        assert today
    

def test_past_competitions_dates(client):
    """
    check if the date of the competition is no longer valid
    """
    date = datetime.today()
    date_competition = datetime.strptime(server.competitions[0]['date'], "%Y-%m-%d %H:%M:%S")
    if date_competition < date:
        today=False
        assert today
