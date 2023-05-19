import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights with random values
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        
        # Initialize biases with zeros
        self.biases1 = np.zeros((1, self.hidden_size))
        self.biases2 = np.zeros((1, self.output_size))
    
    def forward(self, inputs):
        # Compute the output of the neural network
        self.hidden_layer = np.dot(inputs, self.weights1) + self.biases1
        self.hidden_layer_activation = self.sigmoid(self.hidden_layer)
        self.output_layer = np.dot(self.hidden_layer_activation, self.weights2) + self.biases2
        self.output_layer_activation = self.sigmoid(self.output_layer)
        
        return self.output_layer_activation
    
    def backward(self, inputs, outputs, learning_rate):
        # Backpropagation
        delta_output = (outputs - self.output_layer_activation) * self.sigmoid_derivative(self.output_layer)
        delta_hidden = np.dot(delta_output, self.weights2.T) * self.sigmoid_derivative(self.hidden_layer)
        
        # Update weights and biases
        self.weights2 += np.dot(self.hidden_layer_activation.T, delta_output) * learning_rate
        self.biases2 += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
        self.weights1 += np.dot(inputs.T, delta_hidden) * learning_rate
        self.biases1 += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate
    
    def train(self, inputs, outputs, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward propagation
            predicted_outputs = self.forward(inputs)
            
            # Backward propagation
            self.backward(inputs, outputs, learning_rate)
            
            # Calculate and display the loss
            loss = np.mean(np.square(outputs - predicted_outputs))
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss}")
    
    def think(self, inputs):
        # Use the trained network to make predictions
        return self.forward(inputs)
    
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    @staticmethod
    def sigmoid_derivative(x):
        return x * (1 - x)
