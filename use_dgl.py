import dgl
import warnings
import networkx as nx
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
# create a petersen grpah
g_nx = nx.petersen_graph()
# input networkx grpah ,return DGL graph
g_dgl = dgl.DGLGraph(g_nx)  # add direction,bidirectional

plt.figure(figsize=(20, 6))
plt.subplot(121)
plt.title('Undirected graph ,networkx',fontsize=20)
nx.draw(g_nx, with_labels=True)
plt.subplot(122)
plt.title('Directed graph ,DGL', fontsize=20)
nx.draw(g_dgl.to_networkx(), with_labels=True)
plt.show()