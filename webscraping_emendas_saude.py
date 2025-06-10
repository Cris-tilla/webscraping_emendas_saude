import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página que será feita a raspagem (exemplo: execução orçamentária do Senado)
url = "https://www12.senado.leg.br/orcamento/sigabrasil"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar todos os links que contenham a palavra "emenda" no texto
    links = soup.find_all("a", href=True)
    data = [
        {"texto": link.text.strip(), "url": link["href"]}
        for link in links if "emenda" in link.text.lower()
    ]

    df = pd.DataFrame(data)
    df.to_csv("links_emendas.csv", index=False)
    print("Arquivo links_emendas.csv salvo com sucesso!")
else:
    print(f"Erro ao acessar a página: {response.status_code}")
