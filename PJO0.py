from owlready2 import *
# health ops ontology
hoo = get_ontology("http://test.org/healthops.owl#") 

with hoo:
    class Caregiver(Thing):
        pass
    Caregiver.label = ["A person who provides care to patients."]

    class staff(Caregiver):
        pass

    class AIAgent(Caregiver):
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
    class f2f_clinical_event(PatientInteraction):
        '''
        Patient centered event that focuses on clinical mngmnt in a f2f setting.'''
        pass

    class digital_clinical_event(PatientInteraction):
        '''
        An event that is carried out digitally.
        '''
        pass

##### ## Medication ontology



##### diagnostic tests    

    class diagnostic_test(Thing):
        '''
        A class for all diagnostic tests whatever they are
        '''
        pass
    
    class label(diagnostic_test>> str, DataProperty):
        '''
        A property to annotate the name of the test
        '''
        pass

    class orderedBy(diagnostic_test>>Caregiver, ObjectProperty):
        '''
        A property to annotate the caregiver that ordered the test
        '''
        pass

    class orderedTimeStamp(diagnostic_test>> str, DataProperty):
        '''
        A property to annotate the time the test was ordered
        '''
        pass
    

    class resultTimeStamp(diagnostic_test>> str, DataProperty):
        ''' 
        A property to annotate the time the test results were ready
        ''' 
        pass
    class result(diagnostic_test>> str, DataProperty):
        ''' 
        A property to annotate the results of the test
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
    
    class paymentModality(Thing):
        '''
        A class to model payment modalities
        '''
        pass
        
    class label(paymentModality >> str, DataProperty):
        '''
        A property to annotate the name of the payment modality
        '''
        pass

    class hasCashPayment(financial_event >> paymentModality, ObjectProperty):
        '''
        Indicates that the financial event involved a cash payment modality.
        '''
        pass

    class hasCreditPayment(financial_event >> paymentModality, ObjectProperty):
        '''
        Indicates that the financial event involved a credit payment modality.
        '''
        pass

    class hasCryptoPayment(financial_event >> paymentModality, ObjectProperty):
        '''
        Indicates that the financial event involved a crypto payment modality.
        '''
        pass


   

    