import matplotlib.pyplot as plt

dados2 = [15, 17, 15, 15, 17, 14, 18, 15, 15, 17, 15, 12, 15, 15, 18]
print(dados2)

plt.boxplot(dados2, patch_artist=True, boxprops=dict(facecolor="green"),)
plt.xlabel('Fonte de pesquisa')
plt.ylabel('Dados')
plt.title('Boxplot dos Dados')
plt.show()