from collections import Counter
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# Criando a base de dados

dados = [14]*6 + [15]*12 + [16]*9 + [17]*3
print(dados)

# Frequência Absoluta (fi):
fi = pd.Series(Counter(dados)).sort_index()
print(fi)

# Frequência Absoluta Acumulada (fia):
fia = fi.cumsum()
print(fia)

# Frequência Relatica (fr):
fr = fi / fi.sum() * 100
print(fr)

# Frequência Relatica Acumulada (fra):
fra = fr.cumsum ()
print(fra)

# Montando a tabela
tabela = pd.DataFrame({
    'Frequência_Absoluta' : fi,
    'Frequência_Absoluta_Acumulada ' : fia,
    'Frequência_Relatica' : fr,
    'Frequência_Relatica_Acumulada' : fra,
})

print(tabela)

# Nome "Total" na última linha:
tabela.loc['Total'] = [
    fi.sum(),
    '-',
    fr.sum(),
    '-'
]

