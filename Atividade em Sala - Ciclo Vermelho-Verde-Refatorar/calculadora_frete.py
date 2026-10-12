"""Componente de cálculo de frete — etapa GREEN."""


def calcular_frete(modalidade: str, distancia: float) -> float:
    """Calcula o custo do frete conforme a modalidade."""
    if modalidade == "retirada":
        return 0

    if modalidade == "economica":
        return 10 + distancia

    if modalidade == "expressa":
        return 20 + 2 * distancia

    raise ValueError(f"Modalidade desconhecida: {modalidade}")
