'''
생성패턴 - 싱글톤 패턴

글로벌하게 접근 가능한 하나의 패턴을 제공하는 패턴.
로깅, 데이터베이스등의 동일한 리소스에 대한 동시 요청의 충돌을 방지하기 위해 하나의 인스턴스를 공유하는 작업에 주로 사용됌

* 클래스에 대한 단일 객체 생성
* 전역 객체 제공
* 공유된 리소스에 대한 동시 접근 제어
'''


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s = Singleton()
print("First ", s)

s1 = Singleton()
print("Second ", s1)
