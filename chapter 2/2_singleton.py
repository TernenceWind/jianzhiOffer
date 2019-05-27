# coding = utf-8
# 单例模式


'''
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
'''
'''
# new方法
class Singleton(object):
    __instance = None
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
a = Singleton()
a.age = 8
print(a.age)
b = Singleton()
print(b.age)
'''
'''
# 装饰器
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class Myclass(object):
    a = 1
    def __init__(self, x=0):
        self.x = x


c = Myclass(1)
print(c.a)
print(c.x)
d = Myclass(2)
print(d.a)
print(c.x)
print(d.x)
'''
'''
# 多线程
import threading
class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        pass
    def __new__(cls):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance

obj1 = Singleton()
obj1.age = 100
obj2 = Singleton()
print(obj1.age,obj2.age)

def task(arg):
    obj = Singleton()
    print(obj.age)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
'''
