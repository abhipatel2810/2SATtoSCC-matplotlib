import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class TwoSAT:
    def __init__(self, num_variables):
        self.num_variables = num_variables
        self.graph = defaultdict(list)
        self.reversed_graph = defaultdict(list)
        self.visited = set()
        self.stack = []
        self.scc_result = []

    def add_clause(self, i, j):
        self.graph[-i].append(j)
        self.graph[-j].append(i)
        self.reversed_graph[j].append(-i)
        self.reversed_graph[i].append(-j)

    def dfs_fill_order(self, node, graph):
        self.visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in self.visited:
                self.dfs_fill_order(neighbor, graph)
        self.stack.append(node)

    def fill_order(self):
        for i in range(1, 2 * self.num_variables + 1):
            if i not in self.visited:
                self.dfs_fill_order(i, self.graph)

    def dfs_get_scc(self, node):
        self.visited.add(node)
        for neighbor in self.reversed_graph[node]:
            if neighbor not in self.visited:
                self.dfs_get_scc(neighbor)
        self.scc_result[-1].append(node)

    def get_scc(self):
        self.visited.clear()
        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                self.scc_result.append([])
                self.dfs_get_scc(node)

    def solve_2sat(self):
        self.fill_order()
        self.get_scc()

        assignment = {}
        for scc in self.scc_result:
            for variable in scc:
                if -variable in scc:
                    return None  # Not satisfiable
                if variable not in assignment:
                    assignment[variable] = True

        return assignment

    def visualize_2sat(self):
        G = nx.DiGraph()
        for i in range(1, self.num_variables + 1):
            G.add_edge(-i, i)
            G.add_edge(i, -i)
        for clause in self.graph:
            G.add_edge(clause, self.graph[clause][0])
            G.add_edge(clause, self.graph[clause][1])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_color='black', node_size=800)
        plt.title("2-SAT Graph")
        plt.show()

    def visualize_scc(self):
        G = nx.DiGraph()
        for i in range(1, self.num_variables + 1):
            G.add_edge(-i, i)
            G.add_edge(i, -i)
        for clause in self.scc_result:
            for i in range(len(clause) - 1):
                G.add_edge(clause[i], clause[i + 1])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_color='black', node_size=800)
        plt.title("Strongly Connected Components (SCCs) in 2-SAT Graph")
        plt.show()

# Generate random 2-SAT instance
num_variables = 10
two_sat_solver = TwoSAT(num_variables)

for _ in range(20):  # Adding 20 random 2-SAT clauses
    i, j = random.randint(1, num_variables), random.randint(1, num_variables)
    two_sat_solver.add_clause(i, j)

# Visualize 2-SAT graph
two_sat_solver.visualize_2sat()

# Solve 2-SAT and visualize SCCs
result = two_sat_solver.solve_2sat()
if result:
    print("Satisfiable")
    print("Variable assignments:", result)
    two_sat_solver.visualize_scc()
else:
    print("Not satisfiable")
