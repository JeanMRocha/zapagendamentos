
import re
from datetime import datetime

def telefone_valido(numero: str) -> bool:
    numero = re.sub(r'\D', '', numero)
    return len(numero) == 11 and numero.isdigit()

def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        dig = (soma * 10 % 11) % 10
        if dig != int(cpf[i]):
            return False
    return True

def validar_data(data_str: str) -> bool:
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
