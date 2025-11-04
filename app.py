import gradio as gr
import requests
import json
import os
import google.generativeai as genai

# --- 🧠 DEBUG: IMPRIMIR TODOS OS SECRETS DISPONÍVEIS ---
# Vamos verificar se o HFS está injetando a chave corretamente.
print("--- INICIANDO APP: Verificando Variáveis de Ambiente ---")
print("O HFS vê os seguintes Secrets (variáveis de ambiente):")
# Filtra para mostrar apenas as chaves que nos interessam (ou todas)
relevant_keys = [key for key in os.environ if "GEMINI" in key or "API_KEY" in key]
if not relevant_keys:
    print("Nenhum Secret com 'GEMINI' ou 'API_KEY' encontrado.")
else:
    for key in relevant_keys:
        print(f"Encontrado: {key}")
print("-----------------------------------------------------")
# --- FIM DO DEBUG ---


# 1. URL da sua API FastAPI (o Backend)
API_URL = "https://marcelofschiavo-churn-api-v1.hf.space/predict" 

def get_churn_prediction_and_advice(salario, tempo_dias, dias_login, media_logado, chamados, departamento):
    
    # ... (O código da ETAPA 1: CHAMAR A API FASTAPI permanece o mesmo) ...
    try:
        payload = {
            "salario_mensal": salario, "tempo_empresa_dias": tempo_dias,
            "dias_desde_ultimo_login": dias_login, "media_tempo_logado_min": media_logado,
            "total_chamados_suporte": chamados, "departamento": departamento
        }
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status() 
        resultado_api = response.json()
        probabilidade = resultado_api.get("probabilidade_de_churn", 0.0)
        status = "ALTO RISCO" if probabilidade > 0.5 else "BAIXO RISCO"
        resultado_previsao = f"PREVISÃO DO MODELO: {status} ({probabilidade:.2%})"
        
    except requests.exceptions.RequestException as e:
        return f"ERRO CRÍTICO: A API FastAPI (Backend) não respondeu. Detalhes: {e}"

    # --- ETAPA 2: CHAMAR O LLM (NÍVEL 5) ---
    recomendacoes_llm = ""
    # 🧠 DEBUG: Usamos a chave exata que o log vai nos mostrar
    GEMINI_KEY = os.environ.get("GEMINI_API_KEY") 

    if GEMINI_KEY and probabilidade > 0.3:
        try:
            genai.configure(api_key=GEMINI_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"..." # (Seu prompt)
            
            response_llm = model.generate_content(prompt)
            recomendacoes_llm = response_llm.text
            
        except Exception as e:
            recomendacoes_llm = f"ERRO ao gerar IA: {e}"
    else:
        recomendacoes_llm = "Recomendações da IA desabilitadas (Chave não configurada ou Risco Baixo)."

    # --- ETAPA 3: RETORNO FINAL ---
    return (
        f"{resultado_previsao}\n\n"
        f"--- RECOMENDAÇÕES DE INTERVENÇÃO (IA) ---\n"
        f"{recomendacoes_llm}"
    )

# --- Configuração da Interface Gradio ---
# (O restante do código gr.Interface permanece o MESMO)
inputs = [
    gr.Number(label="Salário Mensal (R$)", value=5000),
    gr.Number(label="Tempo de Empresa (dias)", value=700),
    gr.Number(label="Dias desde Último Login", value=10),
    gr.Number(label="Média de Tempo Logado (min)", value=60),
    gr.Number(label="Total de Chamados Suporte", value=2),
    gr.Dropdown(label="Departamento", choices=['TI', 'Vendas', 'RH', 'Marketing'], value='Vendas')
]

gr.Interface(
    fn=get_churn_prediction_and_advice,
    inputs=inputs,
    outputs=gr.Textbox(label="Análise Preditiva e Prescritiva", lines=10),
    title="Simulador de Risco de Churn (Nível 5)",
    description="Interface Gradio (Frontend) que consome a API FastAPI (Backend) e gera recomendações com IA (Gemini)."
).launch()