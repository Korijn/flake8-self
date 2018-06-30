import ast
import flake8_self


def test_all():
    source_code = """class Foo(object):
    def __init__(self):
        self.public_thing = "bar"
        self._private_thing = "quux"
        self.__really_private_thing = "quuz"

foo = Foo()
print(foo.public_thing)
print(foo._private_thing)
print(foo.__really_private_thing)
print(foo.__dict__)"""
    tree = ast.parse(source_code)

    violations = list(flake8_self.SelfLinter(tree).run())
    assert len(violations) == 2
    assert violations[0][0] == 9
    assert violations[0][2] == flake8_self.ERRORS_SLF001
    assert violations[1][0] == 10
    assert violations[1][2] == flake8_self.ERRORS_SLF001
