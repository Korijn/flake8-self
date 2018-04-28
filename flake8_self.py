import ast

__version__ = '0.2.2'

ERRORS_SF01 = 'SF01 Private member access'


def is_private_attribute(attr):
    return not attr.endswith('__') and (attr.startswith('_') or attr.startswith('__'))


class SelfVisitor(ast.NodeVisitor):
    def __init__(self):
        self.access_violations = []

    def visit_Attribute(self, node):
        if is_private_attribute(node.attr):
            if hasattr(node.value, 'id') and node.value.id != 'self':
                self.access_violations.append(node)
            elif hasattr(node.value, 'attr') and node.value.attr != 'self':
                self.access_violations.append(node)


class SelfLinter(object):
    name = 'flake8_self'
    version = __version__

    def __init__(self, tree, filename=None):
        self.tree = tree

    @classmethod
    def add_options(cls, parser):
        pass

    @classmethod
    def parse_options(cls, options):
        pass

    def run(self):
        visitor = SelfVisitor()
        visitor.visit(self.tree)
        for access_violation in visitor.access_violations:
            yield access_violation.lineno, 0, ERRORS_SF01, type(self)
