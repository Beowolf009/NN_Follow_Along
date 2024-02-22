# Description: This file contains the input and weight values for the perceptron model.

inputs = [1.2, 5.1, 2.1, 3]
#leaving these to show where I started
#modeling three nuerons with 4 inputs, each neuron has its own weights and bias
# weights1 = [0.3, 0.2, -0.5, 1.0]
# weights2 = [0.5, 0.26, -0.91, -0.5]
# weights3 = [-0.3, 0.2, -0.5, 1.0]
#leaving these to show where I started
# bias1 = 2.0
# bias2 = 3.0
# bias3 = 0.5
# output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
#           inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
#           inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]
# print(output)

#some_value = 0.5
#weight = -0.7
#bias = 0.7

#print(some_value * weight)  # -0.35
#print(some_value + bias)   # 1.2 this offsets the value of the weight*input


weights = [[0.3, 0.2, -0.5, 1.0],
           [0.5, 0.26, -0.91, -0.5],
           [-0.3, 0.2, -0.5, 1.0]]

biases = [2.0, 3.0, 0.5]
#zip function is used to iterate over two lists in parallel
layer_outputs = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 #Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)


