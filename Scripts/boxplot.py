import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    num_aleatorio = random.randint(0,5)
    vetor.append(num_aleatorio)
    
plt.boxplot(vetor)
plt.title("boxplot")
plt.show()
