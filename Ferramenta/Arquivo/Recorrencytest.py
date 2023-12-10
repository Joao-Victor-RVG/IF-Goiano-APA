import ast

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_name = ""
        self.recurrence_equation = ""
        self.has_recursion = False

    def analyze_function(self, node):
        print(f"Analyzing function '{self.function_name}'")
        self.recurrence_equation = ""
        self.has_recursion = False
        self.visit(node)
        if self.has_recursion:
            print(f"T(n) = {self.recurrence_equation}")
        else:
            print(f"The function '{self.function_name}' is not recursive.")

    def visit_FunctionDef(self, node):
        self.function_name = node.name
        for statement in node.body:
            self.visit(statement)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if self.recurrence_equation:
                self.recurrence_equation += " + "
            self.recurrence_equation += "T(n - 1)"
            self.has_recursion = True

def analyze_recurrence(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        tree = ast.parse(content)

        function_visitor = FunctionVisitor()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_visitor.analyze_function(node)

if __name__ == "__main__":
    path = "code.py"
    analyze_recurrence(path)
