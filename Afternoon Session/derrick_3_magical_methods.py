class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(v1, v2):
        if isinstance(v2, Vector):
            return Vector(v1.x - v2.x, v1.y - v2.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(5, 7)
v2 = Vector(3, 2)
# v3 = Vector(2,5)

v3 = v1 - v2  # Implicit
print(f"Using the operator: {v3}")

v4 = v1.__sub__(v2)  # explicit
print(v4)
