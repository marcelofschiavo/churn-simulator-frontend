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

3.  **[DASHBOARD (O BI)](https://public.tableau.com/app/profile/marcelo.schiavo/viz/ChurnAPI/Story1)**
    * **Tecnologia:** Tableau Public (ou Looker Studio).
    * **Função:** Lê os dados do Google Sheets *em tempo real* (o log que o Backend escreve), mostrando o diagnóstico histórico e o monitoramento das simulações da API..

4. **[APRESENTAÇÃO](https://gamma.app/docs/Turnover--e4hsixi19dpi66p)**
    * **Tecnologia:** Gamma AI
    * **Função:** Apresenta o projeto, detalhando o problema e as soluções adotadas. 
 
