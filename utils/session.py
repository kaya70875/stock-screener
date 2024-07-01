import requests

class QSession:

    def __init__(self , headers , cookies):
        self.headers = headers
        self.cookies = cookies

    def createSession(self):
        session = requests.Session()
        session.headers.update(self.headers)
        session.cookies.update(self.cookies)

        return session