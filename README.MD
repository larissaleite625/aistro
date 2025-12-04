# 🌌 Aistro - Experimento de VQA & MLOps

> **Projeto de Portfólio & Estudo**
>
> Este repositório não é um produto final, mas sim um **experimento técnico**. O objetivo principal é explorar o ecossistema da **Hugging Face**, testar novos conceitos de **IA Generativa (VQA)** e praticar fluxos de **MLOps** utilizando recursos do Databricks.

O **Aistro** realiza a ingestão de imagens astronômicas e utiliza modelos de Inteligência Artificial para responder perguntas sobre elas (ex: "Isso é uma galáxia ou uma estrela?"), registrando todo o processo para auditoria.

## 🛠️ Tech Stack & Conceitos Explorados

Este projeto foi desenvolvido utilizando a **Databricks Free Edition**, demonstrando como criar pipelines robustos mesmo em ambientes acessíveis.

* **Hugging Face (Transformers):** Uso de modelos pré-treinados (`dandelin/vilt-b32-finetuned-vqa`) para tarefas de *Visual Question Answering*.
* **Databricks Volumes:** Gerenciamento de arquivos (imagens e logs) dentro do Unity Catalog (`/Volumes/AI/AISTROS/IMAGES`).
* **MLflow:** Rastreamento completo de experimentos, registrando métricas de confiança (`score`), artefatos (imagens processadas) e parâmetros de execução.
* **Streamlit:** Incluído nas dependências visando a **criação futura de um Databricks App**, permitindo transformar este notebook em uma aplicação interativa para usuários finais.
* **PyTorch & Pillow:** Backend de processamento tensorial e manipulação de imagens.

## 📂 Arquitetura do Código

A estrutura foi pensada para separar a lógica de experimentação da lógica de persistência de dados.

### 1. Pipeline Principal (`Notebook.ipynb`)
É o coração do experimento. Ele orquestra o fluxo de dados:
* **Ingestão Híbrida:** Aceita tanto URLs externas quanto arquivos locais no Volume.
* **Inferência:** Carrega o modelo VQA e submete perguntas padrão ("Describe the image", "Geometric patterns?", etc.).
* **Anotação Visual:** Desenha as respostas da IA diretamente na imagem original para fácil visualização.

### 2. Módulo de Logs (`src/gerenciador_logs.py`)
Script auxiliar focado em observabilidade e persistência:
* Gera arquivos **JSON** estruturados com metadados da execução (timestamp, caminhos, respostas).
* Integração direta com o MLflow Tracking para salvar históricos de "runs".

## 🚀 Como Reproduzir o Estudo

1.  **Instalação:** `pip install -r requirements.txt`.
2.  **Configuração:** Ajuste as variáveis `CATALOG`, `SCHEMA` e `VOLUME` no notebook para o seu ambiente Databricks.
3.  **Execução:** Rode o `Notebook.ipynb`. O sistema baixará a imagem, processará a inferência e salvará os resultados na pasta `processed/`.

## 📝 Licença

Este projeto é open-source sob a **Licença MIT**. Sinta-se livre para usar, modificar e aprender com o código.