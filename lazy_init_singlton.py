'''
게으른 초기화는 싱글톤 패턴을 기반으로 하는 초기화 방식
인스턴스를 꼭 필요한 시점에 생성
'''

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__")
        else:
            print("Already created", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton
        return cls.__instance

s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton()
