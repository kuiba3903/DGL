import dgl
import torch as th
import networkx as nx
import matplotlib.pyplot as plt

g = dgl.DGLGraph()
g.add_nodes(10)
# 逐条往图中添加边
for i in range(1, 4):
    g.add_edge(i, 0)
# 批添加
src = list(range(5, 8))
dst = [0]*3
g.add_edges(src, dst)

src = th.tensor([8, 9])
dst = th.tensor([0, 0])
g.add_edges(src, dst)

plt.figure(figsize=(14, 6))
nx.draw(g.to_networkx(), with_labels=True)
plt.show()
