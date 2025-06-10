# Webscraping Emendas Saúde

Este projeto tem como objetivo coletar e organizar informações sobre as emendas parlamentares na execução orçamentária do Senado Federal. Ele foi desenvolvido no contexto de avaliação de políticas públicas e ciência de dados, alinhado com os Objetivos Estratégicos do Instituto de Pesquisa Econômica Aplicada (IPEA).

## Objetivo Geral

Desenvolver uma ferramenta automatizada para coletar e organizar dados públicos sobre emendas parlamentares no Senado Federal, facilitando análises que subsidiem pesquisas e formulação de políticas públicas.

## Objetivos Específicos

- Realizar web scraping dos links com a palavra "emenda" na página de execução orçamentária do Senado.
- Estruturar os dados coletados em formato CSV.
- Identificar padrões e tendências nas alocações orçamentárias.
- Apoiar estudos nas áreas de saúde, educação e trabalho.

## Justificativa

Muitos dados públicos estão em formato não estruturado, dificultando sua análise. Este projeto usa técnicas de web scraping para tornar essas informações acessíveis e úteis para análises quantitativas baseadas em evidências.

## Como usar

Instale as dependências com:

```bash
pip install requests beautifulsoup4 pandas
