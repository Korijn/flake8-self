class Foo(object):
    def __init__(self):
        self.public_thing = "bar"
        self._private_thing = "quux"
        self.__really_private_thing = "quuz"


foo = Foo()
print(foo.public_thing)
print(foo._private_thing)  # SLF001 Private member access
print(foo.__really_private_thing)  # SLF001 Private member access
print(foo.__dict__)
