class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def get_vertices(self):
        return self.vertices

    def set_vertices(self, vertices):
        self.vertices = vertices

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def remove_vertex(self, vertex):
        self.vertices.remove(vertex)

    def perimeter(self):
        perimeter = 0
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[j]
            perimeter += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return perimeter

    def area(self):
        area = 0
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[j]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2

vertices = [(0, 0), (0, 1), (1, 1), (1, 0)]
polygon = Polygon(vertices)

print("Vertices:", polygon.get_vertices())
print("Perimeter:", polygon.perimeter())
print("Area:", polygon.area())

polygon.add_vertex((2, 0))
print("Vertices:", polygon.get_vertices())
print("Perimeter:", polygon.perimeter())
print("Area:", polygon.area())
