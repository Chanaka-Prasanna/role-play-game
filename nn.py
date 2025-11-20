import math
class Neuron:
    def __init__(self,weights,bias):
        self.__weights = weights
        self.__bias = bias

    def get_weight(self):
        return self.__weights

    def get_bias(self):
        return self.__bias

    def set_weight(self,weight):
        self.__weights = weight

    def set_bias(self,bias):
        self.__bias = bias

    def process(self,inputs_to_neuron):
        total = 0

        for input,weight in zip(inputs_to_neuron,self.__weights):
            total += input * weight

        row_value = total + self.__bias
        # apply sigmoid
        out = 1 / (1 + math.exp(-row_value))

        return out


class NeuralNetwork:
    def __init__(self,neurons):
        self.__neurons = neurons

    def feed_forward(self,inputs_to_network):
        results = []
        for neuron in self.__neurons:
            out = neuron.process(inputs_to_network)
            results.append(out)

        return results
