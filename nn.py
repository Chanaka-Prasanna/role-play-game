import math
class Neuron:
    def __init__(self,weight,bias):
        self.__weight = weight
        self.__bias = bias

    def get_weight(self):
        return self.__weight

    def get_bias(self):
        return self.__bias

    def set_weight(self,weight):
        self.__weight = weight

    def set_bias(self,bias):
        self.__bias = bias

    def process(self,input_value):
        row_value = input_value * self.__weight + self.__bias
        # sigmoid
        out = 1 / (1 + math.exp(-row_value))
        return out


class NeuralNetwork:
    def __init__(self,neurons):
        self.__neurons = neurons

    def feed_forward(self,input_value):
        results = []
        for neuron in self.__neurons:
            out = neuron.process(input_value)
            results.append(out)

        return results

n1 = Neuron(0.5,0)
n2 = Neuron(1.0,5)

network = NeuralNetwork([n1,n2])

print(network.feed_forward(10))