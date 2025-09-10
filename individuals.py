# A running example of how to use the ontology
from PJO1 import  *

import networkx as nx

patient1 = Patient("patient1")
patient1.hasAge = 45  # Assigning an age to the patient
patient1.hasName = "John Adams" # Assigning a name to the patient
patient1.hasId = "A12345" # Assigning an ID to the patient
# Define a procedure and link it to the patient
rpp = Procedure("rpp")
#patient1.hasUndergoneProcedure.append(rpp)
#
f2f = InteractionType("f2f")
rpp.hasInteractionType = f2f
rpp.hasTimestamp = "2023-10-01T10:00:00"



import networkx as nx
import matplotlib.pyplot as plt

# get the classes (types) of the individual
get_class  = lambda x: [(x.name,'rdf:type',cls.name) for cls in x.is_a]
# get properties for a given individual it return a tuple of a triplet.
get_properties = lambda x: [(x.name, prop.name, getattr(x, prop.name)) for prop in x.get_properties()]

triples = get_class(patient1) + get_properties(patient1)


# Example RDF triples

'''
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




'''
patient1.get_properties()
Out[105]: {healthops.hasId, healthops.hasName}

In [106]: list(patient1.get_properties())
Out[106]: [healthops.hasName, healthops.hasId]

'''



