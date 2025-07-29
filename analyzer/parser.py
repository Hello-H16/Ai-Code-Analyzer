# analyzer/parser.py
import ast

class CodeParser:
    def __init__(self, source_code):
        self.tree = ast.parse(source_code)
        self.functions = []
        self.recursions = []

    def extract_functions(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self.functions.append(node.name)
        return self.functions

    def detect_recursion(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                for sub_node in ast.walk(node):
                    if isinstance(sub_node, ast.Call) and isinstance(sub_node.func, ast.Name):
                        if sub_node.func.id == func_name:
                            self.recursions.append(func_name)
        return list(set(self.recursions))
