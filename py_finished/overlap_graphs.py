from rosalind_resources import unpack_fasta

# O^3 overlap graph matching 3 characters of either prefix or suffix
# Each string is a node and a connection is a edge.

nodes = unpack_fasta('rosalind_grph.txt')
edges = []

for node, string in nodes.items():
  node = node.strip('>')
  prefix = string[0:3]
  suffix = string[-3:]
  # print(prefix, suffix)
  for node2, string2 in nodes.items():
    node2 = node2.strip('>')
    if node2 != node:
      if prefix == string2[-3:] and ((node2, node) not in edges):
        edges.append((node2, node))
      if suffix == string2[0:3] and (node, node2) not in edges:
        edges.append((node, node2))

[print(edge[0], edge[1]) for edge in edges]


# Desired Output
# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323