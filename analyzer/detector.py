import ast

class DsaMistakeDetector:
    def __init__(self, source_code):
        self.tree = ast.parse(source_code)
        self.mistakes = []
        self._add_parents()

    def _add_parents(self):
        # Attach parent pointers to AST nodes
        for parent in ast.walk(self.tree):
            for child in ast.iter_child_nodes(parent):
                child.parent = parent

    def check_missing_return_in_recursion(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                is_recursive = False
                recursive_calls_not_returned = 0

                for sub_node in ast.walk(node):
                    if isinstance(sub_node, ast.Call) and isinstance(sub_node.func, ast.Name):
                        if sub_node.func.id == func_name:
                            is_recursive = True
                            # Is the recursive call inside a Return node?
                            if not isinstance(sub_node.parent, ast.Return):
                                recursive_calls_not_returned += 1

                if is_recursive and recursive_calls_not_returned > 0:
                    self.mistakes.append(
                        f"Function '{func_name}' calls itself recursively but does not return the result."
                    )

        return self.mistakes
