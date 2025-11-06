# A running example of how to use the ontology
from PJO1 import  *
import json
import networkx as nx
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import networkx as nx
import matplotlib.pyplot as plt

#

### Scenario Scheduling
def destroy():
    destroy_entity(patient1)
    destroy_entity(schedule)
    destroy_entity(call_center)
    destroy_entity(encounter)
    hoo.save
#


patient1 = Patient("patient1")
patient1.hasAge = 45  # Assigning an age to the patient
patient1.hasName = "John Adams" # Assigning a name to the patient
patient1.hasId = "A12345" # Assigning an ID to the patient
#
encounter = Encounter('encntr')
encounter.hasPurpose = 'Scheduleing'
encounter.hasModalityType = "Phone"

# Scheduling Interaction
schedule = InteractionType('schedule')
schedule.hasPurpose = "Scheduling"
schedule.hasTimestamp = "2025-09-09 12:00:00"
patient1.hasPatientInteraction = schedule




call_center = ModalityType('Call_Center')
call_center.modalityAppliedToPatient.append(patient1)


scheduling_encounter = Encounter('scheduling_encounter')


#####



<<<<<<< HEAD
=======
import networkx as nx
import matplotlib.pyplot as plt


def destroy():
    destroy_entity(patient1)
    destroy_entity(schedule)
    destroy_entity(call_center)
    destroy_entity(encounter)
    hoo.save
#

>>>>>>> 37ce7bcc7ffe1ec446df68ecda619358f0366a54
# get the classes (types) of the individual
get_class  = lambda x: [(x.name,'rdf:type',cls.name) for cls in x.is_a]


  
# get properties for a given individual it return a tuple of a triplet.
get_properties_rdf = lambda x: [(x.name, prop.name, getattr(x, prop.name)) for prop in x.get_properties()]



def get_properties2RDF(individual):
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
    return get_class(individual) + get_properties2RDF(individual)

def return_hash(transtion_triples,previous_hash,nonce):
    '''
    A method to return a simple hash representation of the transaction triples
    '''
    import hashlib
    data_string = json.dumps(transtion_triples, sort_keys=True) + previous_hash + str(nonce)
    return hashlib.sha256(data_string.encode()).hexdigest()


def get_keys():
    '''
    A method to return a public/private key pair
    '''
    from Crypto.PublicKey import RSA
    private_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = 2048,
        backend = default_backend()
    )
    
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_keys(private_key, public_key):
    '''
    A method to serialize the public/private key pair, and wite them to files
    '''
    from cryptography.hazmat.primitives import serialization
    pem_private = private_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.PKCS8,
        encryption_algorithm = serialization.NoEncryption()
    )
    pem_public = public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('private_key.pem', 'wb') as f:
        f.write(pem_private)

    with open('public_key.pem', 'wb') as f:
        f.write(pem_public)

    
def read_keys():
    with open('private_key.pem', 'rb') as f:
        private_key = serialization.load_pem_private_key(
        f.read(),
        password = None,
        backend = default_backend()
)
    with open('public_key.pem', 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend = default_backend()
        )
    return private_key, public_key



def public_encrypt(public_key, message):
    '''
    A method to encrypt a message using the public key
    '''
   
    plaintext = message.encode('utf-8')
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )
    return ciphertext



def private_decrypt_message(private_key, ciphertext):
    '''
    A method to decrypt a message using the private key
    '''
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )
    return plaintext.decode('utf-8')

# Example RDF triples

def draw_k_graph(triples):
    '''
    A method to draw a knowledge graph from a list of triples representing the encounter the patient had
    '''
    plt.figure(figsize=(10, 8))
    G = nx.DiGraph()
    for s, p, o in triples:
        G.add_edge(s, o, label=p)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=6)

    # Draw edge labels (properties)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.show()
    #plt.savefig("knowledge_graph.png")  # Save the graph as a PNG file


## payment time.
payment = InteractionType('payment')
payment.hasPurpose = "Payment"
payment.hasTimestamp = "2025-09-10 15:30:00"
patient1.hasPatientInteraction = payment

financial = financial_event()
stable_coin = paymentModality('stable_coin')
financial.hasCryptoPayment = [stable_coin]
stable_coin.hasPaymentAmount = 150.00
stable_coin.hasPaymentCurrency = "USDC"