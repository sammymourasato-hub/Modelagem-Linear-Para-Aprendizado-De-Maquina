# Histograma
import matplotlib.pyplot as plt

dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 15, 18]
print(dados2)

plt.hist(dados2, bins=3, color="green")
plt.xlabel('Intervalos dos Dados')
plt.ylabel('Frequência')
plt.title('Histograma dos Dados')
plt.show()