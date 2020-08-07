import numpy as np # import Numpy library to generate


# simple one node neural network
def single_node_network():
    weights = np.around(np.random.uniform(size=6), decimals=2) # initialize the weights
    biases = np.around(np.random.uniform(size=3), decimals=2) # initialize the biases

    print(weights)
    print(biases)

    x_1 = 0.5 # input 1
    x_2 = 0.85 # input 2

    print('x1 is {} and x2 is {}'.format(x_1, x_2))
    z_11 = x_1 * weights[0] + x_2 * weights[1] + biases[0]

    print('The weighted sum of the inputs at the first node in the hidden layer is {}'.format(z_11))

    z_12 = x_1 * weights[2] + x_2* weights[3] + biases[1]

    print('The weighted sum of the inputs at the second node in the hidden layer is {}'.format(np.around(z_12, decimals=4)))

    a_11 = 1.0 / (1.0 + np.exp(-z_11))

    print('The activation of the first node in the hidden layer is {}'.format(np.around(a_11, decimals=4)))

    a_12 = 1.0 / (1.0 + np.exp(-z_12))

    print('The activation of the second node in the hidden layer is {}'.format(np.around(a_12, decimals=4)))

    z_2 = a_11*weights[4] + a_12*weights[5] + biases[2]

    print('The weighted sum of the inputs at the node in the output layer is {}'.format(np.around(z_2, decimals=4)))

    a_2 = 1.0 / (1.0 + np.exp(-z_2))


    print('The output of the network for x1 = 0.5 and x2 = 0.85 is {}'.format(np.around(a_2, decimals=4)))

# simple many node neural network
def many_nodes_network():
    n = 5  # number of inputs
    num_hidden_layers = 3  # number of hidden layers
    m = [3, 2, 3]  # number of nodes in each hidden layer
    num_nodes_output = 1  # number of nodes in the output layer
    small_network = initialize_network(n, num_hidden_layers, m, num_nodes_output)


def initialize_network(num_inputs, num_hidden_layers, num_nodes_hidden, num_nodes_output):
    num_nodes_previous = num_inputs  # number of nodes in the previous layer

    network = {}

    # loop through each layer and randomly initialize the weights and biases associated with each layer
    for layer in range(num_hidden_layers + 1):

        if layer == num_hidden_layers:
            layer_name = 'output'  # name last layer in the network output
            num_nodes = num_nodes_output
        else:
            layer_name = 'layer_{}'.format(layer + 1)  # otherwise give the layer a number
            num_nodes = num_nodes_hidden[layer]

            # initialize weights and bias for each node
        network[layer_name] = {}
        for node in range(num_nodes):
            node_name = 'node_{}'.format(node + 1)
            network[layer_name][node_name] = {
                'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
                'bias': np.around(np.random.uniform(size=1), decimals=2),
            }

        num_nodes_previous = num_nodes

    return network  # return the network

# many_nodes_network()

def compute_weighted_sum(inputs, weights, bias):
    return np.sum(inputs * weights) + bias

def node_activation(weighted_sum):
    return 1.0 / (1.0 + np.exp(-1 * weighted_sum))


def forward_propagate(network, inputs):
    layer_inputs = list(inputs)  # start with the input layer as the input to the first hidden layer

    for layer in network:

        layer_data = network[layer]

        layer_outputs = []
        for layer_node in layer_data:
            node_data = layer_data[layer_node]

            # compute the weighted sum and the output of each node at the same time
            node_output = node_activation(compute_weighted_sum(layer_inputs, node_data['weights'], node_data['bias']))
            layer_outputs.append(np.around(node_output[0], decimals=4))

        if layer != 'output':
            print('The outputs of the nodes in hidden layer number {} is {}'.format(layer.split('_')[1], layer_outputs))

        layer_inputs = layer_outputs  # set the output of this layer to be the input to next layer

    network_predictions = layer_outputs
    return network_predictions

n = 5  # number of inputs
num_hidden_layers = 3  # number of hidden layers
m = [3, 2, 3]  # number of nodes in each hidden layer
num_nodes_output = 1  # number of nodes in the output layer
small_network = initialize_network(n, num_hidden_layers, m, num_nodes_output)

np.random.seed(12)
inputs = np.around(np.random.uniform(size=5), decimals=2)

print('The inputs to the network are {}'.format(inputs))

node_weights = small_network['layer_1']['node_1']['weights']
node_bias = small_network['layer_1']['node_1']['bias']

weighted_sum = compute_weighted_sum(inputs, node_weights, node_bias)
print('The weighted sum at the first node in the hidden layer is {}'.format(np.around(weighted_sum[0], decimals=4)))

node_output  = node_activation(weighted_sum)
print('The output of the first node in the hidden layer is {}'.format(np.around(node_output[0], decimals=4)))

sigm = node_activation(0.268)
print(sigm)

