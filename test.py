import numpy as np
from neural_network import NeuralNetwork
from utils import db, encoder


mdb = db.setup_from_cfg('config.json')
c = mdb.get_collection('protein')
raw_protein = []
raw_protein.extend(c.find({'valid': False}, limit=70))
raw_protein.extend(c.find({'valid': True}, limit=70))
unmodified_encoded_input = []
output = []

for p in raw_protein:
    unmodified_encoded_input.append(encoder.paired_method(p['data']))
    output.append(1 if p['valid'] else 0)

max_len = len(max(unmodified_encoded_input, key=lambda x: len(x)))

encoded_input = []
for p in unmodified_encoded_input:
    encoded_input.append(p + [0] * (max_len - len(p)))

# Create an instance of the neural network
input_size = max_len  # Number of input neurons
hidden_size = 140  # Number of neurons in the hidden layer
output_size = 1  # Number of output neurons

nn = NeuralNetwork(input_size, hidden_size, output_size)

inputs = encoded_input
outputs = output

# Train the neural network
epochs = 1000
learning_rate = 0.1
nn.train(inputs, outputs, epochs, learning_rate)

# Make predictions using the trained network
test_inputs = encoder.paired_method('MKLFKVFPIVVDHIQIIPLQQVITCKKCMKGVKKVDAKSRVAFRFRSELEVLDDGFKWRKYGKKMVKNSSNPREIFMNGNYYKCSSGGCNVKKRVERDNEDSSYVITTYEGIHNHESPYVFHYTQFPPNNIALHNLCL')
# result: 1
predictions = nn.think(test_inputs)
print("Predictions:", predictions)