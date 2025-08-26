from owlready2 import *
# health ops ontology
hoo = get_ontology("http://test.org/healthops.owl#") 

with hoo:
    class Caregiver(Thing):
        pass
    class staff(Caregiver):
        pass

    class AIAgent(CareGiver):
        pass
    class Patient(Thing):
        pass

    class Action(Thing):
        '''
        Modelling activities that are effeected on the patient
        '''
        pass
        #Patient Centered Events.
    class PatientInteraction(Action):
        '''
        A key node for interaction with patients.
        having an encounter, a procedure
        '''
    class clinical_event(PatientInteraction):
        '''
        Patient centered event that focuses on clinical mngmnt.'''
        pass

    class digital_event(PatientInteraction):
        '''
        An event that is carried out digitally.
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

    class event_component(Thing):
        '''
        Components that go into the event
        Like, symptoms, histroy, physical exam diagnostics is going to be another class
        '''
        pass



   

    class payment_modality(Thing):
        pass
    


    class personal_event():
        '''
        an event that is carried out with the patients
        '''
        pass

    class procedure(PatientInteraction):
        '''
        Any invasive procedure effeting apatient
        '''
        pass




    