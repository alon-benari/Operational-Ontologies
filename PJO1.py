from owlready2 import *
# health ops ontology
hoo = get_ontology("http://test.org/healthops.owl#") 

with hoo:


### Shared auxiliary attributes to be shared by many classes
    class Name(Thing):
        pass
    Name.label = ["A name attribute to be used by many classes."]

    class Location(Thing):
        pass
    Location.label = ["A location attribute to be used by many classes."]   

    class Id(Thing):
        pass
    Id.label = ["An identifier attribute to be used by many classes."]
    
    class Version(Thing):
        '''
        A class to denote a version of entities in the ontology ie software, machines etc.
        '''

    class Timestamp(Thing):
        pass
    Timestamp.label = ["A timestamp attribute to be used by many classes."]

    class InteractionType(Thing):
        '''
        A class to denote the type of interaction.
        '''
        pass
    InteractionType.label = ["A type of interaction that can occur."]
    

    class hasTimestamp(InteractionType >> str, DataProperty, FunctionalProperty):
        '''
        Associate a timestamp with the interaction type.
        str -  datetime format time stamp.
        '''
        pass

#### Infrastructure
## All things hardware used in the organization from building, to servers   and their attributes.

    class Infrastructure(Thing):
        ''''
        All things hardware used in the organization from building, to servers and their attributes.    
        '''
        pass

    class hasLocation(FunctionalProperty):
        '''physical location in the organizartion'''
        
        domain = [Infrastructure]
        range = [str] # bascially the address of the location
        pass





###Caregiver
    class Caregiver(Thing):
        pass
    Caregiver.label = ["A person who provides care to patients."]
        

    class hasName(Caregiver >> str, DataProperty, FunctionalProperty):
        '''
        Associate the name of the caregiver.
        '''
        pass


###Caregiver types.
    class Person(Thing):
        '''A person in the organization.  '''
        pass
    class hasName(Caregiver >> str, DataProperty, FunctionalProperty):
        '''
        Associate the name of the caregiver'''
        pass
    class hasId(Caregiver >> str, DataProperty, FunctionalProperty):
        '''
        Associate an identifier with the caregiver.
        '''
        pass

    

    class hasDegree(Caregiver >> str, DataProperty, FunctionalProperty):
        '''
        List of degrees associated with the caregiver.
        '''
        pass

    class Staff(Person):
        pass

    class AIAgent(Caregiver):
        pass

    class hasVersion(AIAgent >> Version, ObjectProperty):
        '''
        Associate a version with the caregiver.
        '''
        pass

    class Patient(Thing):
        pass
    class hasAge(Patient >> int, DataProperty, FunctionalProperty):
        '''
        Associate the age of the patient.
        '''
        pass        


    class hasName(Patient >> str, DataProperty, FunctionalProperty):
        '''
        Associate the name of the patient'''
        pass

    class hasId(Patient >> str, DataProperty, FunctionalProperty):
        '''
        Associate an identifier with the patient.
        '''
        pass




#### Actions

    class Action(Thing):
        '''
        Modelling activities that are effeected on the patient
        '''
        pass

    class hasTimestamp(Action >> str, DataProperty, FunctionalProperty):
        '''  
        timestamp an action
        '''
        pass

    
##   Patient Centered Events.
    '''
        Patient are type of Action.  There are several types:
        f2f_encounter:
        TH_encounter:
        digital_encoutner : if at some point in the future there will be a bot to manage this encounter
        procedure: Is a type of an interaction where any procedure is effected on the patient.
        

    '''
    class PatientInteraction(Action):
        '''
        A key node for interaction with patients.
        having an encounter, a procedure
        '''
        pass

    class hasType(PatientInteraction >> InteractionType(), DataProperty):
        '''
        Associate a type with the patient interaction.
        '''
        pass

    class hasInteractionType():
        '''
        A class to define the interaction type'''
        domain = [InteractionType]
        range = [str]



    class f2f_encounter(InteractionType):
        '''
        The equivalent of an f2f encounter
        Patient centered event that focuses on clinical mngmnt in a f2f setting.'''
        pass

    class telehealth_encounter(InteractionType):
        '''
        An encounter that is carried out digitally, either telehalth
        '''
        pass

    class digital_encounter(InteractionType):
        '''
        An encounter that is carried out digitally, bot lead.
        '''
        pass

    class digital_encounter(InteractionType):
        '''
        An encounter that is carried out digitally, either telehealth
        '''
        pass
    

    class Admin_action(InteractionType):
        '''
        A class for administrative interaction, scheduling, cancellation, payments'''
        pass


    class Procedure(InteractionType):
        '''
        A medical procedure performed on the patient.
        '''
        pass

    class procedurePerformedOn(ObjectProperty):
        '''
        A property to annotate the procedure performed on the patient.
        '''
        domain = [Procedure]
        range = [Patient]
        #inverse_property = hasUndergoneProcedure()

    class hasUndergoneProcedure(ObjectProperty): 
        '''
        A property to annotate the procedure the patient has undergone.
        This is the inverse of procedurePerformedOn
        '''
        domain = [Patient]
        range = [Procedure]
        inverse_property = procedurePerformedOn()
        

    class scheduling(Admin_action):
        '''
        The process of scheduling an appointment or procedure ( therapeutic /diagnostic/both) for the patient.
        '''
        pass


##### ## Medication ontology obo -  how to leverage it



#####e data ( labs, imaging, other test,  etc.)   

    class ObjectiveData(Thing):
        '''
        A class to model all objective data related to patient care not generated/diagnosed by humans.
        Labs, imaging, vital signs, wearable data, any objective test.
        '''
        pass
    class hasName(ObjectiveData >> str, DataProperty, FunctionalProperty):
        '''
        Associate a name with the objective data.
        '''
        pass
    class hasCreatedTimestamp(ObjectiveData >> str, DataProperty, FunctionalProperty):
        '''
        Associate a timestamp with the creatued objective data, .
        '''
        pass



    class orderedBy(ObjectiveData>>Caregiver, ObjectProperty):
        '''
        A property to annotate the caregiver that ordered the test
        '''
        pass
    orderedBy.comment = ["The caregiver who ordered the diagnostic test."]

    class orderedTimeStamp(ObjectiveData>> str, DataProperty):
        '''
        A property to annotate the time the test was ordered
        '''
        pass
    orderedTimeStamp.comment = ["The time the test was ordered."]

    class resultTimeStamp(ObjectiveData>> str, DataProperty):
        ''' 
        A property to annotate the time the test results were ready
        ''' 
        pass
    resultTimeStamp.comment = ["The time the test results were ready."]

    class result(ObjectiveData>> str, DataProperty):
        ''' 
        A property to annotate the results of the test
        '''
        pass
    result.comment = ["The results of the diagnostic test."]


#### Careplan, the plan in the raw test clinical note.

    class Careplan(Thing):
        '''
        A human created and human readable care plan. The equivalent of  the  basic medical record --> create entities from text.
        '''
    class hasTimestamp(Careplan >> str, DataProperty, FunctionalProperty):
        '''
        Associate a timestamp with the care plan.
        '''
        pass
    class hasCareplanText(Careplan >> str, DataProperty, FunctionalProperty):
        '''
        Associate a text description with the care plan. The raw text of the note.
        '''
        pass
    class hasCareplanCreator(Careplan >> Caregiver, ObjectProperty):
        '''
        Associate a caregiver with the care plan.
        '''
        pass




     ## financial patient centeredevents
    class financial_event(PatientInteraction):
        '''
        Patient centered event that focuses on financials
        '''
        pass

    class hasInteraction(Patient>>PatientInteraction, ObjectProperty):
        '''
        A property to annotate the type of interaction the patient had
        '''
        pass
    hasInteraction.comment = ["The type of interaction the patient had."]



    class paymentModality(Thing):
        '''
        A class to model payment modalities
        '''
        pass

    class hasCashPayment(financial_event >> paymentModality, ObjectProperty):
        '''
        Indicates that the financial event involved a cash payment modality.
        '''
        pass
    hasCashPayment.comment = ["Indicates a cash payment modality."]


    class hasCreditPayment(financial_event >> paymentModality, ObjectProperty):
        '''
        Indicates that the financial event involved a credit payment modality.
        '''
        pass
    hasCreditPayment.comment = ["Indicates a credit payment modality."]

    class hasCryptoPayment(financial_event >> paymentModality, ObjectProperty):
        '''
        Indicates that the financial event involved a crypto payment modality.
        '''
        pass
    hasCryptoPayment.comment = ["Indicates a crypto payment modality."]




    
