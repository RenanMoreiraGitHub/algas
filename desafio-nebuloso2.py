class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def postVizinho(self, vizinho, peso=0):
        self.points_to[vizinho] = peso

    def getVizinho(self):
        return self.points_to.keys()

    def getPeso(self, vizinho):
        return self.points_to[vizinho]

    def isVizinho(self, vizinho):
        return vizinho in self.points_to


class Graph:
    def __init__(self):
        self.vertices = {}

    def postVertex(self, key):
        novoVertex = Vertex(key)
        self.vertices[key] = novoVertex
        return novoVertex

    def getVertex(self, key):
        return self.vertices.get(key)

    def __contains__(self, key):
        return key in self.vertices

    def postEdge(self, fromKey, toKey, peso):
        if fromKey not in self.vertices:
            self.postVertex(fromKey)
        if toKey not in self.vertices:
            self.postVertex(toKey)
        self.vertices[fromKey].postVizinho(self.vertices[toKey], peso)
        self.vertices[toKey].postVizinho(
            self.vertices[fromKey], peso)  # adiciona a aresta reversa

    def hasEdge(self, fromKey, toKey):
        if fromKey in self.vertices:
            return self.vertices[fromKey].isVizinho(self.vertices.get(toKey))
        else:
            return False

    def __iter__(self):
        return iter(self.vertices.values())


def main():
    graph = Graph()
    while True:
        print("\nO que você gostaria de fazer?")
        print("1 - Adicionar um vértice")
        print("2 - Adicionar uma aresta")
        print("3 - Mostrar Grafo")
        print("0 - Sair")
        resposta = int(input("Escolha: "))

        if resposta == 1:
            key = input("Digite a key do vértice: ")
            graph.postVertex(key)
            print("Vértice adicionado com sucesso!")
        elif resposta == 2:
            fromKey = input("Digite a key do vértice de origem: ")
            toKey = input("Digite a key do vértice de destino: ")
            pesoAresta = input("Digite o peso da aresta: ")
            peso = int(pesoAresta) if pesoAresta else 1
            graph.postEdge(fromKey, toKey, peso)
            print("Aresta adicionada com sucesso!")
        elif resposta == 3:
            print("\nVértices:")
            for vertex in graph:
                print(vertex.key)
            print("\nArestas:")
            for vertex in graph:
                for vizinho in vertex.getVizinho():
                    print(
                        f"{vertex.key} -> {vizinho.key} (peso {vertex.getPeso(vizinho)})")
        elif resposta == 0:
            break
        else:
            print("Operação inválida, escolha uma outra opção.")


if __name__ == '__main__':
    main()