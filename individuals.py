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
rpp.procedurePerformedOn.append(patient1)
# Define an interaction type and link it to the patient
f2f = InteractionType("f2f")

patient1.hasPatientInteraction = f2f
rpp.hasTimestamp = "2023-10-01T10:00:00"
patient1.hasProcedureDoneDatetime = rpp.hasTimestamp



import networkx as nx
import matplotlib.pyplot as plt

# get the classes (types) of the individual
get_class  = lambda x: [(x.name,'rdf:type',cls.name) for cls in x.is_a]


  
# get properties for a given individual it return a tuple of a triplet.
get_properties = lambda x: [(x.name, prop.name, getattr(x, prop.name)) for prop in x.get_properties()]



def get_properties(individual):
    '''
    A method to return triplets of the form (subject, predicate, object) for the classes of the individual
    '''
    triples = []
    for prop in individual.get_properties():
        value = getattr(individual, prop.name)
        if isinstance(value, list):
            for v in value:
                triples.append((individual.name, prop.name, v.name if hasattr(v, 'name') else v))
        else:
            triples.append((individual.name, prop.name, value.name if hasattr(value, 'name') else value))   
    return triples


def get_triples(individual):
    return get_class(individual) + get_properties(individual)

# Example RDF triples

def draw_k_graph(triples):
    '''
    A method to draw a knowledge graph from a list of triples representing the encounter the patient had
    '''
    plt.figure(figsize=(10, 8))
    G = nx.DiGraph()
    for s, p, o in triples:
        G.add_edge(s, o, label=p)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)

    # Draw edge labels (properties)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.show()
    #plt.savefig("knowledge_graph.png")  # Save the graph as a PNG file
'''
patient1.get_properties()
Out[105]: {healthops.hasId, healthops.hasName}

In [106]: list(patient1.get_properties())
Out[106]: [healthops.hasName, healthops.hasId]

'''



