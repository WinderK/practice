class OrderedUnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.elements_order = {}
        self.element_index = {}  # Mapping from element to its index in the set

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.elements_order[x] = [x]
            self.element_index[x] = 0

    def find(self, x):
        if x not in self.element_index:
            self.add(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.elements_order[rootX].extend(self.elements_order[rootY])
            self.update_indices(rootY, rootX)

    def update_indices(self, old_root, new_root):
        for element, index in self.element_index.copy().items():
            if self.find(element) == old_root:
                self.element_index[element] = self.elements_order[new_root].index(element) + len(self.elements_order[new_root]) - len(self.elements_order[old_root]) + self.element_index[old_root]

    def get_index(self, x):
        root = self.find(x)
        if x not in self.element_index or self.find(x) != root:
            self.add(x)
        return self.element_index[x]

# Example usage:
uf = OrderedUnionFind()
uf.add(1)
uf.add(4)
uf.add(7)
uf.add(9)
uf.add(3)
uf.add(6)

uf.union(1, 9)
uf.union(1, 4)
uf.union(1, 7)
uf.union(9, 3)
uf.union(9, 6)

print(uf.get_index(3))  # Output should be the index of 3 in the set with root 1
