def verificar_acesso(usuario_logado, aluno_consultado):
    """Impede que um aluno consulte dados acadêmicos de outro aluno."""
    usuario_id = usuario_logado.get("id")
    aluno_id = aluno_consultado.get("id")

    if usuario_id is None or aluno_id is None:
        raise ValueError("usuário e aluno devem possuir um identificador.")

    if usuario_id != aluno_id:
        raise PermissionError(
            "não é permitido acessar as notas de outro aluno."
        )

    return True
