from requisitos_usuario import consultar_notas
from requisitos_sistema import verificar_autenticacao


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


def main():
    usuario_autenticado = {
        "id": 1,
        "nome": "Gabriel",
        "autenticado": True,
    }
    usuario_nao_autenticado = {
        "id": 2,
        "nome": "Visitante",
        "autenticado": False,
    }
    notas = {
        "Engenharia de Software": 8.5,
        "Compiladores": 9.0,
    }

    print("R1 - Consulta das próprias notas:")
    print(consultar_notas(notas))

    print("\nR2 - Verificação de usuário autenticado:")
    verificar_autenticacao(usuario_autenticado)
    print("Consulta autorizada para Gabriel.")

    print("\nR2 - Tentativa de usuário não autenticado:")
    try:
        verificar_autenticacao(usuario_nao_autenticado)
    except PermissionError as erro:
        print(f"Consulta bloqueada: {erro}")


if __name__ == "__main__":
    main()
