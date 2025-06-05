import os

MAX_TAMANHO_ARQUIVO = 500 * 1024  # 500 KB
EXTENSOES = [".py", ".sql", ".json", ".yml", ".yaml"]
PASTA_SAIDA = "export_zap"  # Você pode trocar por outro nome, ex: "dump_analise"

def listar_estrutura(caminho_base, destino):
    saida = os.path.join(destino, "estrutura_projeto.txt")
    with open(saida, "w", encoding="utf-8") as f:
        for raiz, dirs, arquivos in os.walk(caminho_base):
            nivel = raiz.replace(caminho_base, "").count(os.sep)
            indent = " " * 2 * nivel
            f.write(f"{indent}{os.path.basename(raiz)}/\n")
            sub_indent = " " * 2 * (nivel + 1)
            for arquivo in arquivos:
                f.write(f"{sub_indent}{arquivo}\n")
    print(f"📁 Estrutura salva em: {saida}")

def extrair_conteudo_por_tamanho(caminho_base, destino, prefixo_saida):
    contador_global = 1
    buffer = ""
    tamanho_atual = 0

    for raiz, dirs, arquivos in os.walk(caminho_base):
        for arquivo in arquivos:
            if not any(arquivo.endswith(ext) for ext in EXTENSOES):
                continue

            caminho_arquivo = os.path.join(raiz, arquivo)
            try:
                with open(caminho_arquivo, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                    header = f"\n\n### Arquivo: {os.path.relpath(caminho_arquivo, caminho_base)} ###\n\n"
                    trecho = header + conteudo

                    if tamanho_atual + len(trecho.encode("utf-8")) > MAX_TAMANHO_ARQUIVO:
                        nome_saida = os.path.join(destino, f"{prefixo_saida}_parte_{contador_global}.txt")
                        with open(nome_saida, "w", encoding="utf-8") as out:
                            out.write(buffer)
                        print(f"📦 Criado: {nome_saida}")
                        contador_global += 1
                        buffer = ""
                        tamanho_atual = 0

                    buffer += trecho
                    tamanho_atual += len(trecho.encode("utf-8"))

            except Exception as e:
                print(f"❌ Erro ao ler {caminho_arquivo}: {e}")

    if buffer:
        nome_saida = os.path.join(destino, f"{prefixo_saida}_parte_{contador_global}.txt")
        with open(nome_saida, "w", encoding="utf-8") as out:
            out.write(buffer)
        print(f"📦 Criado: {nome_saida} (final)")
    else:
        print("⚠️ Nenhum conteúdo foi extraído.")

# USO:
if __name__ == "__main__":
    base_dir = "app"  # Pasta que você deseja analisar
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    listar_estrutura(base_dir, PASTA_SAIDA)
    extrair_conteudo_por_tamanho(base_dir, PASTA_SAIDA, "conteudo_zapagendamentos")
