from owlready2 import *

onto = get_ontology("http://test.org/onto.owl#") 

set_log_level(9)

with onto:
    class Bacterium(Thing):
        pass
    class Shape(Thing):
        pass    
    class Group(Thing):
        pass    

    ## subclasses

    class RodShape(Shape):
        pass

    class Isolated(Group):
        pass

    class InPair(Group):
        pass

    class has_shape(ObjectProperty, FunctionalProperty):
        domain = [Bacterium]
        range = [Shape] 

    class has_grouping(Bacterium >> Group, ObjectProperty):
        pass

    class gram_positive(Bacterium >> bool, FunctionalProperty):
        pass    

    ## creating a sub property
    class has_rare_property(has_shape): 
        pass

obo = onto.get_namespace("http://purl.obolibrary.org/obo/")

## creating individuals

my_bacterium = Bacterium()


## Instantiating a more complex individual
my_bacterium2 = Bacterium ( "complexBacterium",
                           gram_positive = True,
                           has_shape = RodShape(),
                           has_grouping = [Isolated()]
)


