'''
모노슬레이트 싱글톤 패턴: 모든 객체가 같은 상태를 공유하는 패턴

'''

class Borg:
    __shared_state = {"1": "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print(b, b1, b.__dict__, b1.__dict__)

class Borg:
    _shared_state = {"1": "2"}
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

b = Borg()
b1 = Borg()
b.x = 4

print(b, b1, b.__dict__, b1.__dict__)