class SuperClass:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self._b = b
        self.__c = c


class SubClass(SuperClass):
    def __init__(self, a, b, c, d, e) -> None:
        super().__init__(a, b, c)
        self.d = d
        self.__e = e

    def __str__(self) -> str:
        return f"{self.a}, {self._b}, {self.__c}, {self.d}, {self.__e}"


ins = SubClass(1, 2, 3, 4, 5)
# print(ins)

print(ins.a)
print(ins._b)
# print(ins.__c)
print(ins.d)
print(ins.__e)
