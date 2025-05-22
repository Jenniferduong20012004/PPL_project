
class TreeToArrayVisitor():
    def __init__ (self):
        self.result =[]
    def getRequirementFromUser (self, parse_str):
        self.extract_keys(parse_str)
        filtered = [item for item in self.result if item[1] is not None]
        return filtered
    def extract_keys(self,parse_str):
        tokens = parse_str.replace('(', ' ( ').replace(')', ' ) ').split()
        stack = []

        i = 0
        while i < len(tokens):
            if tokens[i] == '(':
                i += 1
                key = tokens[i]
                stack.append(key)
                i += 1

                # Check for nested expression or value
                if tokens[i] != '(':
                    # This is a value node
                    value_parts = []
                    while i < len(tokens) and tokens[i] not in ('(', ')'):
                        value_parts.append(tokens[i])
                        i += 1
                    value = ' '.join(value_parts)
                    self.result.append((key, value))
                else:
                    # Nested, value will be handled in deeper level
                    self.result.append((key, None))
            elif tokens[i] == ')':
                if stack:
                    stack.pop()
                i += 1
            else:
                i += 1
        return self.result



    