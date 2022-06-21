# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
INT_MAX = 99999

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printPath(self, history, j):
		#print(j)
		if (history[j] == -1): 
			print(j, end=" ")
			return
		self.printPath(history , history[j])
		print(j, end=" ")

	def printSolution(self, dist, history, src, destiny):
		print("{} --> {}".format(src, destiny))
		self.printPath(history, destiny)
		print("\nCusto:", dist[destiny])
		#print("Vertex \tDistance from Source")
		#or node in range(self.V):
			#print(node, "\t", dist[node])

	# função de utilidade para encontrar o vértice com
	# valor da distância mínima, do conjunto de vértices
	# ainda não incluído na árvore do caminho mais curto
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = INT_MAX

		# Pesquisar não o vértice mais próximo que não esteja no
		# árvore do caminho mais curto
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	# Função que implementa a fonte única de Dijkstra
	# algoritmo de caminho mais curto para um gráfico representado
	# usando representação de matriz de adjacência
	def dijkstra(self, src, destiny): ############################### + destiny

		#inf inf inf inf
		dist = [INT_MAX] * self.V 
		dist[src] = 0
		#vetor de visitados é false, false, false
		sptSet = [False] * self.V

		#############################################
		history = [-1] * self.V
		###############################################

		for cout in range(self.V):

			# Escolha o vértice de distância mínima dentre o 
			# o conjunto de vértices ainda não processados.

			# x é sempre igual a src na primeira iteração
			x = self.minDistance(dist, sptSet)

			# Coloque o vértice de distância mínima na
			# árvore do caminho mais curto
			sptSet[x] = True

			# Atualiza o valor dist dos vértices adjacentes do vértice escolhido
			# somente se a atual distância é maior que a nova distância e
			# o vértice não está na árvore do caminho mais curto
			for y in range(self.V):
				if (self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]):
						dist[y] = dist[x] + self.graph[x][y]
						#####################
						#print(x)
						
						history[y] = x
						########################
		#print(history)
		self.printSolution(dist, history, src, destiny)

# Driver program
g = Graph(9)
g.graph =     [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		       [4, 0, 8, 0, 0, 0, 0, 11, 0],
		       [0, 8, 0, 7, 0, 4, 0, 0, 2],
		       [0, 0, 7, 0, 9, 14, 0, 0, 0],
		       [0, 0, 0, 9, 0, 10, 0, 0, 0],
		       [0, 0, 4, 14, 10, 0, 2, 0, 0],
		       [0, 0, 0, 0, 0, 2, 0, 1, 6],
		       [8, 11, 0, 0, 0, 0, 1, 0, 7],
		       [0, 0, 2, 0, 0, 0, 6, 7, 0]];


####################################################
#g.dijkstra(0);
src = int(input("Origem: "))
dst = int(input("Destino: "))

g.dijkstra(src, dst)
#################################################

# This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal
