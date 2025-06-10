# # Webscraping Emendas Saúde

Este projeto tem como objetivo coletar links que contenham a palavra "emenda" na página de execução orçamentária do Senado Federal.

## Script principal

O script `webscraping_emendas_saude.py` acessa a página, faz o scraping dos links e salva os resultados em um arquivo CSV.

## Como usar

- Instale as dependências com:  
  ```bash
  pip install requests beautifulsoup4 pandas
