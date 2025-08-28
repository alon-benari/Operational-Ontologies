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
    
    

    class orderedBy(diagnostic_test>>Caregiver, ObjectProperty):
        '''
        A property to annotate the caregiver that ordered the test
        '''
        pass
    orderedBy.comment = ["The caregiver who ordered the diagnostic test."]

    class orderedTimeStamp(diagnostic_test>> str, DataProperty):
        '''
        A property to annotate the time the test was ordered
        '''
        pass
    orderedTimeStamp.comment = ["The time the test was ordered."]

    class resultTimeStamp(diagnostic_test>> str, DataProperty):
        ''' 
        A property to annotate the time the test results were ready
        ''' 
        pass
    resultTimeStamp.comment = ["The time the test results were ready."]

    class result(diagnostic_test>> str, DataProperty):
        ''' 
        A property to annotate the results of the test
        '''
        pass
    result.comment = ["The results of the diagnostic test."]

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


   

    