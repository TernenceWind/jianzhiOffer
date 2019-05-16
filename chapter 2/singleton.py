# coding = utf-8

# 元类
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        print("...")
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
class Myclass(metaclass=Singleton):
    def fun(self):
        pass
s = [1,2]
a = Myclass(*s)
b = Myclass(*s)