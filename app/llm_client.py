
import requests

def perguntar_llm(prompt: str, historico: list = []) -> str:
    try:
        historico_texto = "\n".join(historico[-10:])  # últimos 10 itens de histórico
        prompt_modificado = (
            f"{historico_texto}\nUsuário: {prompt}"
        )

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt_modificado,
                "temperature": 0.2,
                "stream": False
            },
            timeout=15
        )

        data = response.json()
        return data.get("response", "[Sem resposta]")
    except Exception as e:
        return f"[Erro na requisição: {e}]"
