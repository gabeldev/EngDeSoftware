def verificar_autenticacao(usuario):
    """Impede a consulta de notas por usuários não autenticados."""
    if not usuario.get("autenticado", False):
        raise PermissionError("usuário não autenticado.")

    return True
