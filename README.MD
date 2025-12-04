Aqui está o `README.md` atualizado, incorporando a menção ao **Databricks Free Edition** e o contexto do **Streamlit** para futuros Databricks Apps.

-----

# 🌌 Aistro - Análise de Imagens Astronômicas com IA

O **Aistro** é uma ferramenta de reconhecimento e análise de imagens astronômicas que utiliza modelos de *Visual Question Answering* (VQA) para descrever automaticamente corpos celestes.

> 🎓 **Objetivo do Projeto:** Este projeto foi desenvolvido para **estudo de como funciona o Hugging Face**, experimentando ferramentas novas de IA e novas possibilidades e conceitos de processamento de imagens e MLOps.

-----

## 🚀 Funcionalidades

  * **VQA (Visual Question Answering):** Utiliza o modelo `dandelin/vilt-b32-finetuned-vqa` para responder perguntas em linguagem natural sobre as imagens.
  * **Processamento Híbrido:** Suporte para imagens locais (via Databricks Volumes) ou download direto via URL.
  * **Anotação Automática:** Gera versões anotadas das imagens com as inferências da IA sobrepostas.
  * **Rastreamento com MLflow:** Registra métricas, artefatos e logs de execução para monitoramento de experimentos.
  * **Logs Estruturados:** Salva arquivos JSON detalhados para persistência e auditoria dos dados.

-----

## 🛠️ Tecnologias Utilizadas

As principais bibliotecas utilizadas neste estudo incluem:

  * **Transformers (Hugging Face):** Pipeline de inferência de modelos pré-treinados.
  * **PyTorch (`torch`):** Framework de Deep Learning.
  * **MLflow:** Gestão do ciclo de vida de ML.
  * **Pillow (PIL):** Processamento de imagens.
  * **Streamlit:** Incluído nas dependências com a **possibilidade de desenvolver uma interface de usuário rica** e converter o projeto em um **Databricks App** no futuro.

-----

## ⚙️ Ambiente e Execução

### Ambiente de Desenvolvimento

Este projeto foi concebido e testado utilizando a **Databricks Free Edition**, aproveitando recursos como Unity Catalog (Volumes) e clusters básicos para o pipeline de MLOps.

### Estrutura do Projeto

```text
aistro/
├── Notebook.ipynb          # Pipeline principal de execução
├── requirements.txt        # Lista de dependências
└── src/
    └── gerenciador_logs.py # Módulo auxiliar para logs JSON e MLflow
```

### Como Executar

1.  **Instalação:** Instale as dependências listadas:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configuração:** No `Notebook.ipynb`, ajuste as variáveis do Unity Catalog (`CATALOG`, `SCHEMA`, `VOLUME`) para o seu ambiente Databricks.
3.  **Execução:** Escolha o modo de operação (`URL` ou `VOLUME`) e execute as células para processar as imagens e gerar os logs.

-----

## 📝 Licença

Este projeto está licenciado sob a **Licença MIT**.

```text
MIT License

Copyright (c) 2025 Larissa Leite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```