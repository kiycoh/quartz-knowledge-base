---
last modified: 24/10/2025 14:02
related: null
tags:
  - machine-learning
  - intelligenza-artificiale
  - perceptron
---

> [!IMPORTANT] [The math in the Rosenblatt Perceptron](https://sergedesmedt.github.io/MathOfNeuralNetworks/RosenblattPerceptronArticle.html)
> È possibile utilizzare il percettrone senza comprenderne realmente i fondamenti matematici, ma è altrettanto divertente vedere come tutta la matematica che hai imparato a scuola può aiutarti a comprendere il percettrone e, per estensione, le reti neurali.
# Definizione di percettrone
Nel percettrone di Rosenblatt, la decisione se un punto si trova al di sopra o al di sotto di una linea è basata su una funzione di attivazione applicata a una combinazione lineare degli ingressi.

La formula generale per un percettrone binario è:

$y = f\left( w_1 x_1 + w_2 x_2 + b \right)$

![[Pasted image 20250312160326.png#left|300]]

![[Pasted image 20250312160751.png]]



> [!example] [Basic Rosenblatt Perceptron implementation](https://github.com/christianversloot/machine-learning-articles/blob/main/linking-maths-and-intuition-rosenblatts-perceptron-in-python.md)
> 
> ```Python
> import numpy as np
> 
> class RBPerceptron:
> 
>   # Constructor
>   def __init__(self, number_of_epochs = 100, learning_rate = 0.1):
>     self.number_of_epochs = number_of_epochs
>     self.learning_rate = learning_rate
> 
>   # Train perceptron
>   def train(self, X, D):
>     # Initialize weights vector with zeroes
>     num_features = X.shape[1]
>     self.w = np.zeros(num_features + 1)
>     # Perform the epochs
>     for i in range(self.number_of_epochs):
>       # For every combination of (X_i, D_i)
>       for sample, desired_outcome in zip(X, D):
>         # Generate prediction and compare with desired outcome
>         prediction    = self.predict(sample)
>         difference    = (desired_outcome - prediction)
>         # Compute weight update via Perceptron Learning Rule
>         weight_update = self.learning_rate * difference
>         self.w[1:]    += weight_update * sample
>         self.w[0]     += weight_update
>     return self
> 
>   # Generate prediction
>   def predict(self, sample):
>     outcome = np.dot(sample, self.w[1:]) + self.w[0]
>     return np.where(outcome > 0, 1, 0)
> ```

## Differenze con percettrone moderno
Il **percettrone di Rosenblatt** si differenzia dei *neuroni artificiali moderni*:
* Presenta una funzione di attivazione *a soglia* (o *gradino*, o  *[[Funzione di Heaviside]]*) per cui noteremo un output del tipo:
$$
f(z) =
\begin{cases}
1, & \text{se } w_i \cdot x_i + b \geq 0 \\
0, & \text{altrimenti}
\end{cases} \quad;
$$
* Può apprendere solo funzioni *linearmente separabili*;
	* [[#Problema dello XOR]];
* Non supporta *probabilità*;
* Non sono presenti *strati nascosti*, ha un solo strato;
* Regole di aggiornamento dei pesi semplici (no [[Backpropagation]]).
$$
\begin{aligned}
w_i \leftarrow w_i + \Delta w_i \\
\Delta w_i = \eta (y - \hat{y}) x_i
\end{aligned}
$$
## Problema dello XOR
lo XOR non è linearmente separabile