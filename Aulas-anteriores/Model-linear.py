import pandas as pd
import numpy as np

# Dados para cumprir os requisitos de 100 linhas e 15 colunas (FIAP Checkpoint)
np.random.seed(42)
n = 100
data = {
    "ID_Pedido": [f"LOG{i+1000}" for i in range(n)],
    "Data_Envio": pd.to_datetime(np.random.choice(pd.date_range("2024-01-01", "2024-06-30"), n)).strftime("%d/%m/%Y"),
    "Cliente": np.random.choice(["TechSul", "VarejoGlobal", "IndústriaNorte", "TransLog", "E-CommerceBR"], n),
    "Cidade_Origem": np.random.choice(["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre"], n),
    "Cidade_Destino": np.random.choice(["Manaus", "Salvador", "Fortaleza", "Brasília", "Recife"], n),
    "Tipo_Carga": np.random.choice(["Eletrônicos", "Alimentos", "Automotivo", "Vestuário", "Farmacêutico"], n),
    "Modal": np.random.choice(["Rodoviário", "Aéreo", "Ferroviário"], n),
    "Peso_kg": np.round(np.random.uniform(10, 5000, n), 2),
    "Volume_m3": np.round(np.random.uniform(0.5, 20, n), 2),
    "Valor_NF_RS": np.round(np.random.uniform(1000, 150000, n), 2),
    "Custo_Frete_RS": np.round(np.random.uniform(200, 15000, n), 2),
    "Distancia_km": np.random.randint(200, 4000, n),
    "Tempo_Estimado_Dias": np.random.randint(2, 15, n),
    "Status": np.random.choice(["Entregue", "Em Trânsito", "Atrasado", "Pendente"], n),
    "Emissao_CO2_kg": np.round(np.random.uniform(5, 500, n), 2)
}

df = pd.DataFrame(data)
df.to_excel("Base_Logistica_FIAP.xlsx", index=False)
print("Arquivo 'Base_Logistica_FIAP.xlsx' criado com sucesso!")



