def consultar_notas(notas):
    """Formata as notas do aluno para exibição no terminal."""
    if not notas:
        return "Nenhuma nota cadastrada."

    linhas = ["=== Minhas notas ==="]
    for disciplina, nota in notas.items():
        linhas.append(f"{disciplina}: {nota:.1f}")

    return "\n".join(linhas)
