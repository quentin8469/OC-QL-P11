from locust import HttpUser, task, between
import server

class HelloWorldUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def index(self):
        """"""
        self.client.get("/")

