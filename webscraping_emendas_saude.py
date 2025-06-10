import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da execução orçamentária
url = "https://www12.senado.leg.br/orcamento/execucao/orcamento-2024"

# Requisição HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Coleta de links com "emenda"
links = soup.find_all("a")
emendas_links = []

for link in links:
    href = link.get("href")
    if href and "emenda" in href.lower():
        emendas_links.append(href)

# Exporta para CSV
df = pd.DataFrame(emendas_links, columns=["Links com 'emenda'"])
df.to_csv("links_emendas.csv", index=False)

print("✔ Arquivo links_emendas.csv salvo com sucesso!")
