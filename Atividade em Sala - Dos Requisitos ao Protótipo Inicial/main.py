from requisitos_usuario import consultar_notas
from requisitos_sistema import verificar_autenticacao
from requisitos_eticos import verificar_acesso


# PLANO
# R1 - Requisito de usuário: o aluno deve poder consultar suas notas.
# R2 - Requisito de sistema: somente usuários autenticados podem consultar notas.
# R3 - Requisito ético: um aluno não pode consultar as notas de outro aluno.
#
# Ordem e tempo planejado:
# 1. R1 - Consulta de notas: 15 minutos.
# 2. R2 - Verificação de autenticação: 15 minutos.
# 3. R3 - Restrição de acesso: 15 minutos.
# 4. Documentação e autoavaliação: 5 minutos.
#
# Uso de IA: apoio na organização do código, implementação e revisão dos
# cenários usados para comprovar cada requisito. 


def executar_consulta(usuario, aluno):
    verificar_autenticacao(usuario)
    verificar_acesso(usuario, aluno)
    return consultar_notas(aluno["notas"])


def main():
    usuario_rodolfo = {
        "id": 1,
        "nome": "Rodolfo",
        "autenticado": True,
    }
    usuario_nao_autenticado = {
        "id": 2,
        "nome": "Visitante",
        "autenticado": False,
    }
    aluno_rodolfo = {
        "id": 1,
        "nome": "Rodolfo",
        "notas": {
            "Matemática": 8.5,
            "Física": 9.0,
        },
    }
    aluno_joao = {
        "id": 2,
        "nome": "João",
        "notas": {
            "Matemática": 9.5,
            "Física": 8.0,
        },
    }

    print("Cenário 1 - R1: aluno autenticado consulta as próprias notas")
    print(executar_consulta(usuario_rodolfo, aluno_rodolfo))
    print("Resultado: consulta autorizada pelos requisitos R2 e R3.")

    print("\nCenário 2 - R2: usuário não autenticado tenta consultar notas")
    try:
        executar_consulta(usuario_nao_autenticado, aluno_rodolfo)
    except PermissionError as erro:
        print(f"Consulta bloqueada: {erro}")

    print("\nCenário 3 - R3: aluno tenta consultar as notas de outro aluno")
    try:
        executar_consulta(usuario_rodolfo, aluno_joao)
    except PermissionError as erro:
        print(f"Consulta bloqueada: {erro}")


if __name__ == "__main__":
    main()


# AUTOAVALIAÇÃO
# Critérios atingidos: os critérios 1 a 6 foram atendidos.
# Critérios não atingidos: nenhum.
# O requisito mais difícil foi o R3, pois a consulta precisava distinguir o
# próprio aluno de outro aluno. A solução foi comparar os identificadores antes
# de liberar o acesso às notas.
# A IA ajudou a organizar os módulos, implementar as validações e revisar os
# cenários. A sugestão inicial da IA precisou ser ajustada para representar os
# requisitos escolhidos como comportamentos verificáveis no terminal.
