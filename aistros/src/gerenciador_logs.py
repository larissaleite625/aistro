import mlflow
import json
import os
from datetime import datetime

def salvar_execucao(nome_imagem, caminho_completo_imagem, texto_resposta, volume_path):
    """
    Registra a execução no MLflow e salva um JSON no Volume.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # --- 1. MLflow Tracking ---
    # Ajuste o caminho do experimento para o seu usuário ou pasta compartilhada
    mlflow.set_experiment("/Users/seu_email@dominio.com/Observatorio_App_Logs")
    
    with mlflow.start_run(run_name=f"analise_{nome_imagem}"):
        # Registra parâmetros e métricas
        mlflow.log_param("imagem_input", nome_imagem)
        mlflow.log_param("data_execucao", timestamp)
        
        # Registra a resposta do modelo como um arquivo de texto dentro do run
        mlflow.log_text(texto_resposta, "resposta_modelo.txt")
        
        print(f"Log MLflow criado para: {nome_imagem}")

    # --- 2. Persistência no Volume (JSON) ---
    nome_log_json = f"log_{nome_imagem}_{timestamp}.json"
    caminho_salvar_json = os.path.join(volume_path, nome_log_json)
    
    dados_para_salvar = {
        "imagem": nome_imagem,
        "caminho_imagem_original": caminho_completo_imagem,
        "analise_ia": texto_resposta,
        "data_processamento": timestamp
    }
    
    try:
        with open(caminho_salvar_json, "w", encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
        return True, nome_log_json
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")
        return False, str(e)