import os
import subprocess
from datetime import datetime

def exportar_e_versionar():
    print("🔧 Iniciando exportação interativa de trecho de código...")

    nome_arquivo = input("📝 Nome do arquivo (sem extensão): ").strip()
    tipo = input("📂 Extensão do arquivo (ex: py, sql, yml, md): ").strip()
    mensagem_commit = input("💬 Mensagem de commit: ").strip()
    
    print("✏️ Cole o conteúdo do trecho (finalize com uma linha contendo apenas 'EOF'):")
    linhas = []
    while True:
        linha = input()
        if linha.strip().upper() == "EOF":
            break
        linhas.append(linha)
    conteudo = "\n".join(linhas)

    data = datetime.now().strftime("%Y-%m-%d")
    pasta = os.path.join("revisoes", data)
    os.makedirs(pasta, exist_ok=True)

    caminho_completo = os.path.join(pasta, f"{nome_arquivo}.{tipo}")
    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"✅ Trecho salvo em: {caminho_completo}")

    try:
        subprocess.run(["git", "add", caminho_completo], check=True)
        subprocess.run(["git", "commit", "-m", mensagem_commit], check=True)
        subprocess.run(["git", "push"], check=True)
        print("🚀 Commit e push realizados com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar Git: {e}")

if __name__ == "__main__":
    exportar_e_versionar()
