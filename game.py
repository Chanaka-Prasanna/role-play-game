from nn import NeuralNetwork,Neuron



n1 = Neuron([0.5, 0.5, 0.5], 0)
n2 = Neuron([0.3, 1.0, 0.1],5)

network = NeuralNetwork([n1,n2])

print(network.feed_forward([10, 20, 30]))