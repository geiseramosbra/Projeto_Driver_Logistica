import pandas as pd

# PASSO 1: Carregar o arquivo bruto

print("⏳ Carregando dados... Isso pode levar alguns segundos.")
df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding='ISO-8859-1')

# PASSO 2: Selecionar apenas o que importa 
mercados_foco = ['LATAM', 'USCA']
df_filtrado = df[df['Market'].isin(mercados_foco)].copy()

# PASSO 3: Limpeza de Colunas (Nomes corrigidos com 'D' maiúsculo)
colunas_uteis = [
    'Order Country', 
    'Order City', 
    'Market', 
    'Delivery Status', 
    'Late_delivery_risk', 
    'Category Name', 
    'Sales',
    'Days for shipment (scheduled)', 
    'Days for shipping (real)'
]
df_final = df_filtrado[colunas_uteis].copy()

# PASSO 4: Criar inteligência (Cálculo de Atraso Logístico)
# Dias reais menos dias agendados = Atraso
df_final['Diferenca_Entrega'] = df_final['Days for shipping (real)'] - df_final['Days for shipment (scheduled)']

# PASSO 5: Exportar o arquivo pronto para o Power BI
df_final.to_csv('data/draiver_market_health.csv', index=False)

print("-" * 30)
print("✅ SUCESSO! O arquivo 'draiver_market_health.csv' foi gerado.")
print(f"📊 Total de linhas processadas: {len(df_final)}")
print("-" * 30)
