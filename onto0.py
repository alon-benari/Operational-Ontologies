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

    class has_grouping(Bacterium >> Group, FunctionalProperty):
        pass

    class gram_positive(Bacterium >> bool, FunctionalProperty):
        pass    

    ## creating a sub property
    class has_rare_property(has_shape): 
        pass


## creating individuals

my_bacterium = Bacterium()