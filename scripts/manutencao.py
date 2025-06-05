# manutencao.py
import sqlite3, shutil, os
from datetime import datetime

DB_PATH = os.path.join("..", "data", "zap.db")
BACKUP_DIR = os.path.join("..", "data", "backups")
LOG_PATH = os.path.join("..", "data", "logs.txt")

# 1. Cria diretório de backups se não existir
os.makedirs(BACKUP_DIR, exist_ok=True)

def backup_banco():
    if not os.path.exists(DB_PATH):
        print("[ERRO] Banco de dados não encontrado.")
        return
    data = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = os.path.join(BACKUP_DIR, f"zap_{data}.db")
    shutil.copy(DB_PATH, destino)
    print(f"[OK] Backup criado em: {destino}")

def verificar_integridade():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA integrity_check")
    result = cursor.fetchone()[0]
    conn.close()
    if result != "ok":
        raise Exception("Erro de integridade no banco de dados!")
    print("[OK] Integridade verificada com sucesso.")

def diagnostico_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    ativos = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM usuarios_inativos")
    inativos = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM exclusao_pendente")
    pendentes = cursor.fetchone()[0]
    conn.close()
    print(f"[INFO] Diagnóstico: Ativos: {ativos}, Inativos: {inativos}, Exclusão pendente: {pendentes}")

def registrar_log(acao):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        agora = datetime.now().isoformat()
        log.write(f"[{agora}] {acao}\n")

def executar_manutencao():
    print("🔧 Iniciando manutenção preventiva...")
    backup_banco()
    verificar_integridade()
    diagnostico_banco()
    registrar_log("Manutenção diária concluída")
    print("✅ Manutenção finalizada com sucesso.")

if __name__ == "__main__":
    executar_manutencao()
