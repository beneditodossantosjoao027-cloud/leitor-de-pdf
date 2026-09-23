import requests
import json
import os
import time
import threading
import pdfplumber

# --- Configuração (igual ao Indianos Remaster) ---
CHAVES_API = [
    v for v in (os.environ.get(f"GEMINI_KEY_{i}") for i in range(1, 11))
    if v
]
if not CHAVES_API:
    print("[AVISO] Nenhuma chave Gemini encontrada em GEMINI_KEY_1..GEMINI_KEY_10.")

MODELOS = [
    "gemini-3.1-flash-lite",
    "gemini-3.1-pro-preview",
]

COMBOS = [(chave, modelo) for chave in CHAVES_API for modelo in MODELOS]

lock_api = threading.Lock()
indice_combo_atual = 0

def montar_url(modelo):
    return f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"

def chamar_gemini(payload, timeout=40, max_tentativas=None):
    global indice_combo_atual
    tentativas = max_tentativas or (len(COMBOS) * 2)

    for _ in range(tentativas):
        with lock_api:
            chave_atual, modelo_atual = COMBOS[indice_combo_atual]
        url = montar_url(modelo_atual)

        try:
            resposta = requests.post(
                url,
                headers={'Content-Type': 'application/json', 'x-goog-api-key': chave_atual},
                data=json.dumps(payload), timeout=timeout
            )
        except requests.exceptions.RequestException as e:
            print(f"[API] Falha de conexão: {e}. Tentando de novo em 2s...")
            time.sleep(2)
            continue

        if resposta.status_code == 429:
            with lock_api:
                indice_combo_atual = (indice_combo_atual + 1) % len(COMBOS)
            print(f"[COTA] '{modelo_atual}' esgotou. Trocando pro próximo modelo/chave...")
            continue

        if resposta.status_code in (500, 502, 503, 504):
            print(f"[API] '{modelo_atual}' indisponível (HTTP {resposta.status_code}). Tentando de novo...")
            time.sleep(2)
            with lock_api:
                indice_combo_atual = (indice_combo_atual + 1) % len(COMBOS)
            continue

        if resposta.status_code != 200:
            print(f"[API] Erro HTTP {resposta.status_code}: {resposta.text[:200]}")
            return None

        try:
            dados = resposta.json()
            return dados['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            print(f"[API] Resposta em formato inesperado: {e}")
            return None

    print("[COTA] Todos os combos chave+modelo esgotaram por agora.")
    return None
caminho =r"caminho.pdf"
txt=""
with pdfplumber.open(caminho) as pdf:
    for i, pg in enumerate(pdf.pages):
        texto=pg.extract_text()
        if texto:
            txt+=texto

pergunta = f"Aqui está o conteúdo de um documento:\n\n{txt}\n\npergunte oque quiser?"
payload = {"contents": [{"parts": [{"text": pergunta}]}]}
resposta = chamar_gemini(payload)
print(resposta)