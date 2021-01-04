class MPNeuron:
    def __init__(self):
        self.n = 3
        self.inputs = [1, 1, 1]
        self.weights = [1, 1, 1]
        self.threshold = 2.5
    
    def MP_Neuron_Input(self, n, inputs, weights, threshold):
        self.n = n
        self.inputs = inputs
        self.weights = weights
        self.threshold = threshold
    
    def MP_Neuron_Evaluate(self):
        sum = 0
        for i in range(self.n):
            sum += self.inputs[i] * self.weights[i]
        if (sum >= self.threshold):
            return 1
        else:
            return 0
            
# input size
n = 3
# input matrix
inp = [1,1,1] 

# layer 1
n1 = MPNeuron()
n1.MP_Neuron_Input(1,[inp[0]],[-1],0)
n2 = MPNeuron()
n2.MP_Neuron_Input(1,[inp[1]],[-1],0)
n3 = MPNeuron()
n3.MP_Neuron_Input(1, [inp[2]], [-1], 0)


# layer 2
m = MPNeuron()
m.MP_Neuron_Input(3,
    [n1.MP_Neuron_Evaluate(), n2.MP_Neuron_Evaluate(), n3.MP_Neuron_Evaluate()],
    [1, 1, 1],
    1)
print(m.MP_Neuron_Evaluate())
