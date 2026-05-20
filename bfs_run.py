from collections import deque

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = 'white'

    def __repr__(self):
        return f"{self.name}({self.color})"


def BFS(vertices, startVert):
    # Initialize
    for v in vertices:
        v.color = 'white'

    startVert.color = 'gray'
    queue = deque()
    queue.append(startVert)

    visit_order = []

    while queue:
        u = queue[0]  # peek
        # process neighbors
        for v in u.neighbors:
            if v.color == 'white':
                v.color = 'gray'
                queue.append(v)
        queue.popleft()
        u.color = 'black'
        visit_order.append(u.name)

    return visit_order


if __name__ == '__main__':
    # build example graph
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')

    A.neighbors = [B, C]
    B.neighbors = [D]
    C.neighbors = [E]
    D.neighbors = []
    E.neighbors = []

    vertices = [A, B, C, D, E]

    order = BFS(vertices, A)
    print('Visit order:', order)
    print('Final colors:')
    for v in vertices:
        print(f'  {v.name}: {v.color}')
