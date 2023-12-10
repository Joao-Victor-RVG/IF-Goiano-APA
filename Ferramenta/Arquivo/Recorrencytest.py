import ast
from sympy import symbols, Eq, solve

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self, function_name):
        self.function_name = function_name
        self.has_recursion = False

    def visit_FunctionDef(self, node):
        if node.name == self.function_name:
            for child_node in ast.walk(node):
                if isinstance(child_node, ast.Call) and isinstance(child_node.func, ast.Name):
                    if child_node.func.id == self.function_name:
                        self.has_recursion = True
        self.generic_visit(node)

class MasterMethodAnalyzer:
    @staticmethod
    def analyze_master_method(file_path, function_name):
        with open(file_path, 'r') as file:
            content = file.read()
            tree = ast.parse(content)
            visitor = FunctionVisitor(function_name)
            visitor.visit(tree)
            if visitor.has_recursion:
                print(f"The function '{function_name}' appears to be recursive.")
                MasterMethodAnalyzer.analyze_recurrence(file_path, function_name)

    @staticmethod
    def analyze_recurrence(file_path, function_name):
        with open(file_path, 'r') as file:
            content = file.read()
            tree = ast.parse(content)
            function_node = next((node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == function_name), None)

            if function_node:
                a, b = symbols('a b')
                recurrence_equation = Eq(len(list(function_node.body)), a * len(list(function_node.body[0].body)) / b)
                solution = solve(recurrence_equation, len(list(function_node.body)))
                print(f"Solving recurrence for '{function_name}': T(n) = {solution[0]}")

def check_recursion(file_path, function_name):
    with open(file_path, 'r') as file:
        content = file.read()
        tree = ast.parse(content)
        visitor = FunctionVisitor(function_name)
        visitor.visit(tree)
        if visitor.has_recursion:
            print(f"The function '{function_name}' appears to be recursive.")
            MasterMethodAnalyzer.analyze_recurrence(file_path, function_name)
        else:
            print(f"The function '{function_name}' does not appear to be recursive.")

def extract_function_names(filename):
    with open(filename, "r") as source_code:
        tree = ast.parse(source_code.read())
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return functions

if __name__ == "__main__":
    path = "code.py"
    function_list = extract_function_names(path)

    for function_name in function_list:
        check_recursion(path, function_name)
