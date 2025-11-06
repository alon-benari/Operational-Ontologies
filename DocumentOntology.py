<<<<<<< HEAD
from owlready2 import get_ontology, onto_path
do_ontology = get_ontology(".\\Assets\\DocumentOntologyRDF.owl").load() 

for c in  do_ontology.classes():
    print(c, c.label, c.name)



=======
from owlready2 import get_ontology, onto_path
do_ontology = get_ontology(".\\Assets\\DocumentOntologyRDF.owl").load() 

for c in  do_ontology.classes():
    print(c, c.label, c.name)



>>>>>>> 37ce7bcc7ffe1ec446df68ecda619358f0366a54
