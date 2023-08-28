class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super().__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("s 1")
        self._servers.append("s 2")
        self._servers.append("s 3")
    def changeServer(self):
        self._servers.pop()
        self._servers.append("s 4")

h1 = HealthCheck()
h2 = HealthCheck()

h1.addServer()
for i in range(3):
    print(h1._servers[i])

h2.changeServer()
for i in range(3):
    print(h2._servers[i])