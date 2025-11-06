from owlready2 import get_ontology, onto_path
do_ontology = get_ontology(".\\Assets\\DocumentOntologyRDF.owl").load() 

for c in  do_ontology.classes():
    print(c, c.label, c.name)



