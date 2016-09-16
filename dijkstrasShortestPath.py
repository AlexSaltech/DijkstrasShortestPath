processedVertices = [1]


def load_file():
    with open('/home/alejandro/Documents/Stanford Algorithms 1/Week 5/dijkstraData.txt') as f:  # dijkstraData.txt
        graph = {}
        shortestPaths = {}
        number_of_vertices = 0
        for line in f:
            if line:
                number_of_vertices += 1
                line = line.split()
                node = int(line[0])
                graph[node] = []
                shortestPaths[node] = 0
                for x in range(1, len(line)):
                    connection = line[x].split(",")
                    graph[node].append((int(connection[0]), int(connection[1])))
    return graph, number_of_vertices, shortestPaths


def dijkstras_shortest_path(graph, number_of_vertices, processedVertices, shortestPaths):
    while len(processedVertices) < number_of_vertices:
        dijkstras = -1
        next_node = 0
        for v in processedVertices:
            for w in graph[v]:
                if w[0] not in processedVertices:
                    if shortestPaths[v] + w[1] < dijkstras or dijkstras == -1:
                        next_node = w[0]
                        dijkstras = shortestPaths[v] + w[1]
        processedVertices.append(next_node)
        if dijkstras >= 0:
            shortestPaths[next_node] = dijkstras

inp = load_file()
graph = inp[0]
number_of_vertices = inp[1]
shortestPaths = inp[2]
dijkstras_shortest_path(graph, number_of_vertices, processedVertices, shortestPaths)

print load_file()
for k, v in shortestPaths.iteritems():
    print str(k) + " : " + str(v)
