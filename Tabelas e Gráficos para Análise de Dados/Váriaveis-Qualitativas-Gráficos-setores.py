# Gráficos Rstatisticos:
# Variáveis:
# Setores:
import matplotlib.pyplot as plt

dados1 = ["Sim"] * 20 + ["Não"] * 45
print(dados1)

print(45 + 20)
print(45 / 65)
print(20 / 65)

labels = ['Não', 'Sim']
sizes = [45, 20]
percent_labels = ['69,23%', "30,77%"]
colors = ['red', 'blue']

plt.pie(sizes, labels=percent_labels, colors=colors)
plt.title('Respotas Entrevista')
plt.legend(labels, loc='lower left')
plt.show()
