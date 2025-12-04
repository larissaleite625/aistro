# 🌌 Observatório AI - Streamlit App

Este aplicativo utiliza Inteligência Artificial para analisar imagens astronômicas armazenadas no Databricks Unity Catalog.

## Funcionalidades
1. Leitura de imagens do volume `/Volumes/AI/AISTROS/IMAGES`.
2. Análise de imagem usando modelo Hugging Face (`Salesforce/blip-image-captioning-large`).
3. Registro de experimentos e logs no **MLflow**.
4. Salvamento dos resultados em formato JSON no mesmo volume das imagens.

## Estrutura de Arquivos
- `app.py`: Aplicação principal (Frontend e lógica de IA).
- `requirements.txt`: Dependências do Python.
- `src/gerenciador_logs.py`: Módulo responsável por salvar dados no MLflow e Volume.

## Como Rodar no Databricks

1. **Instalar Dependências:**
   Certifique-se de que o `requirements.txt` foi instalado no ambiente.
   ```bash
   pip install -r requirements.txt