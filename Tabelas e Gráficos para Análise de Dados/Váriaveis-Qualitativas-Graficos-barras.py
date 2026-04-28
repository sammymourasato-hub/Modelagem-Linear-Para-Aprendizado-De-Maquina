# Gráficos de barra

from collections import Counter
import matplotlib.pyplot as plt

dados1 = ["Sim"] * 20 + ["Não"] * 45
print(dados1)

respostas1 = Counter(dados1)
print(respostas1)

labels = list(respostas1.keys())
values = list(respostas1.values())

colors = ["skyblue"]

plt.bar(labels, values, color=colors)
plt.title('Respotas Entrevista')
plt.legend(labels, loc='upper right')
plt.show()