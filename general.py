class A:
    '''Класс A'''

    def set_a(self, value):
        self.a = value

    def get_a(self):
        return self.a

class B:
    '''Класс B'''

    def __init__(self, b):
        self.b = b

    def get_b(self):
        return self.b

class C(A, B):
    '''Класс C = A + B'''

    def __init__(self, a, b, c):
        super().__init__(b)
        self.set_a(a)
        self.c = c

    def set_b(self, value):
        self.b = value

    def set_c(self, value):
        self.c = value

    def get_c(self):
        return self.c

class D:
    @staticmethod
    def stat_print_dict(obj):
        print(obj.__dict__)

    @classmethod
    def cls_print_dict(cls):
        print(cls.__dict__)