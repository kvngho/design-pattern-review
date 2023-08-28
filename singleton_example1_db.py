'''
여러서비스가 한개의 DB를 공유하는 구조

* 데이터 베이스 작업간의 일관성이 유지되어야 한다.
* 메모리와 CPU 자원을 효율적으로 사용하여햐 한다.

* 여러 웹앱이 사용하면 연결 풀링 사용하는게 효율적
'''

import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DataBase(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = DataBase().connect()
db2 = DataBase().connect()

print(db1, db2)

