# A running example of how to use the ontology
from PJO1 import  *

import networkx as nx

patient1 = Patient("patient1")
patient1.hasName = "John Adams" # Assigning a name to the patient
patient1.hasId = "A12345" # Assigning an ID to the patient

import networkx as nx
import matplotlib.pyplot as plt

# Example RDF triples
triples = [
    ("patient1", "hasName", "John Doe"),
    ("patient1", "rdf:type", "Patient"),
    ("patient1", "hasId", "12345")
]

''''''
G = nx.DiGraph()
for s, p, o in triples:
    G.add_edge(s, o, label=p)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)

# Draw edge labels (properties)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()

'''
patient1.get_properties()
Out[105]: {healthops.hasId, healthops.hasName}

In [106]: list(patient1.get_properties())
Out[106]: [healthops.hasName, healthops.hasId]

'''
