---
title: Simulador de Risco de Churn (Nível 5)
emoji: 🚀
sdk: gradio
app_file: app.py
pinned: true
---

# 🚀 Simulador de Risco de Churn (Nível 5 - MLOps)

Este é o **Frontend** (Interface de Usuário) de um projeto de MLOps de People Analytics de ponta-a-ponta. 

Esta interface não é apenas uma demo:
1.  Ela consome uma API Backend (FastAPI) para **previsão de risco** (Nível 3).
2.  Ela chama uma IA Generativa (Google Gemini) para **recomendações prescritivas** (Nível 5).
3.  Ela aciona um log de persistência em um banco de dados na nuvem (Google Sheets).

---

## 🔗 Arquitetura Completa (Os 3 Links do Projeto)

Este projeto é desacoplado em três serviços na nuvem:

1.  **[INTERFACE (Esta Demo)](https://huggingface.co/spaces/marcelofschiavo/churn-simulator)**
    * **Tecnologia:** Gradio (SDK do Hugging Face).
    * **Função:** Coleta os dados do RH, chama a API (Backend) e o LLM (Gemini).

2.  **[BACKEND (A API)](https://huggingface.co/spaces/marcelofschiavo/churn-api-v1)**
    * **Tecnologia:** FastAPI (em um container Docker).
    * **Função:** Carrega o modelo (`.pkl`) treinado, calcula o risco e salva o log da simulação no Google Sheets (via `gspread`).

3.  **[DASHBOARD (O BI)](https://SEU-LINK-DO-TABLEAU-PUBLIC-AQUI)**
    * **Tecnologia:** Tableau Public (ou Looker Studio).
    * **Função:** Lê os dados do Google Sheets *em tempo real* (o log que o Backend escreve), mostrando o diagnóstico histórico e o monitoramento das simulações da API.

## 🛠️ Desafio de Engenharia Superado

O desafio deste projeto foi a **incompatibilidade de artefatos (Nível 4)**. O modelo (`.pkl`) treinado localmente (Python 3.13 / NumPy 2.x) era incompatível com o ambiente de produção (Python 3.10 / NumPy 1.x), causando o erro `No module named 'numpy._core'`.

**Solução:** Usei o **Google Colab** como uma "sala limpa" (ambiente 3.10) para **recriar o artefato (`.pkl`) compatível**, garantindo que a "chave" (servidor) e o "cadeado" (modelo) fossem da mesma versão.