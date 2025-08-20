from owlready2 import *

onto = get_ontology("/http://coffee_ontology.org/coffee.owl")

with onto:
       # Entities as classes
    class Coffee(Thing):
            pass


    # related information captured as classes
    class Roast(Thing):
            pass

    class Region(Thing):
            pass

    #Subclass ing -> inheriting from main classes
    class Dark_Roast(Roast):
            pass
    class Blonde_Roast(Roast):
            pass
    class Medium_Roast(Roast):
            pass

    class Latin_America(Region):
            pass
    class Asia_Pacific(Region):
            pass
    class Multi(Region):
            pass    


    # Modeling relationships
    class has_roast(ObjectProperty, FunctionalProperty):
        domain = [Coffee]
        range = [Roast]


    class from_region(Coffee >> Region, FunctionalProperty):
        pass

    #### defnining some onotology individuals i.e. coffee types

    class Verdana(Coffee):
        equivalent_to = [Coffee & has_roast.value(Medium_Roast) & from_region.some(Region) &
                        from_region.value(Latin_America)]


    #.some means it must be related to a Region
    #.only means if it's related to a region it must be the one defined
    class Pike(Coffee):
        equivalent_to = [Coffee & has_roast.value(Medium_Roast) & from_region.some(Region) &
                        from_region.only(Latin_America)]


#telling the ontology these are all different things
AllDifferent([Dark_Roast, Blonde_Roast, Medium_Roast])
AllDifferent([Latin_America, Asia_Pacific, Multi])

#### run

coffee1 = Coffee(has_roast = Blonde_Roast, from_region = Latin_America)
coffee2 = Coffee(has_roast = Medium_Roast, from_region = Latin_America)

print(coffee1.is_a)
print(coffee2.is_a)

close_world(Coffee)