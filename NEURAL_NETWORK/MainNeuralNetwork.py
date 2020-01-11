import Siec_neuronowa.NEURAL_NETWORK.NeuralNetwork as NeuralNetwork
import torch
import matplotlib.pyplot as plt
import matplotlib

if __name__ == '__main__':
    print("Hello world!")
    n = NeuralNetwork.SineNet(50, 'Tanh')