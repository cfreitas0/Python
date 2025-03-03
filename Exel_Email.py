import pandas as pd
import win32com.client as win32
from win32uiole import CreateOleClientItem

#importar a base de dados
tabela_Vendas = pd.read_excel('Tabela.xlsx')


#visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_Vendas)

# faturamento por loja
faturamento = tabela_Vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de produtos por loja
quantidade = tabela_Vendas[['ID Loja', 'Quantda']].groupby('ID Loja').sum()
print(quantidade)

# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantda']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:'Ticket Médio'})
print('-' *50,ticket_medio)

# enviar email com o relatório
outlook = win32.Dispatch('outlook.application')
mail  = outlook.CreateItem(0)
mail.to = 'rafaela.01desa@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja>'
mail.HTMLBody = f'''
<p>Prezados<p>

Segue o relaório de vendas por cada Loja.

<p>Faturamento:<p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:<p>
{quantidade.to_html()}

<p>Tiket Médio dos produtos por Loja:<p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer duvida Entre em contato por esse email.<p>

ATT..
César
'''

mail.Send()

print('Email Enviado Com Sucesso...')