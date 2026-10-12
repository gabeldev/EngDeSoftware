"""Componente de cálculo de frete — etapa REFACTOR (padrão Strategy)."""

from abc import ABC, abstractmethod


# PADRÃO DE PROJETO: Strategy
# Participantes nomeados conforme o domínio de fretes:
# - Strategy: EstrategiaFrete
# - ConcreteStrategy: FreteRetirada, FreteEconomico, FreteExpresso
# - Context: CalculadoraFrete


class EstrategiaFrete(ABC):
    """Contrato das diferentes modalidades de cálculo de frete."""

    @abstractmethod
    def calcular(self, distancia: float) -> float:
        """Retorna o custo do frete para a distância informada."""


class FreteRetirada(EstrategiaFrete):
    """Retirada no local: sem custo de frete."""

    def calcular(self, distancia: float) -> float:
        return 0


class FreteEconomico(EstrategiaFrete):
    """Entrega econômica: taxa fixa de 10, mais 1 por quilômetro."""

    def calcular(self, distancia: float) -> float:
        return 10 + distancia


class FreteExpresso(EstrategiaFrete):
    """Entrega expressa: taxa fixa de 20, mais 2 por quilômetro."""

    def calcular(self, distancia: float) -> float:
        return 20 + 2 * distancia


class CalculadoraFrete:
    """Context: delega o cálculo à estratégia recebida."""

    def __init__(self, estrategia: EstrategiaFrete) -> None:
        self.estrategia = estrategia

    def calcular(self, distancia: float) -> float:
        return self.estrategia.calcular(distancia)


_ESTRATEGIAS: dict[str, type[EstrategiaFrete]] = {
    "retirada": FreteRetirada,
    "economica": FreteEconomico,
    "expressa": FreteExpresso,
}


def calcular_frete(modalidade: str, distancia: float) -> float:
    """API pública preservada: mesma assinatura e regras das fases anteriores."""
    try:
        classe_estrategia = _ESTRATEGIAS[modalidade]
    except KeyError as erro:
        raise ValueError(f"Modalidade desconhecida: {modalidade}") from erro

    return CalculadoraFrete(classe_estrategia()).calcular(distancia)


# AUTOAVALIAÇÃO
# Critério 1: atendido; os testes ficam em arquivo separado, um por modalidade.
# Critério 2: as fases RED, GREEN e REFACTOR são registradas em commits próprios.
# Critério 3: atendido; em RED, a função apenas lançava NotImplementedError,
# e a execução registrada em evidencias/red.txt contém três testes falhando.
# Critério 4: Strategy foi aplicado e seus participantes foram nomeados conforme
# o domínio.
# Critério 5: atendido; a suíte final passou nos três testes, e a saída real está
# registrada em evidencias/refactor.txt.
# Critérios técnicos não atingidos: nenhum.
# Mudança GREEN -> REFACTOR: os cálculos antes selecionados por condicionais
# passaram a ser encapsulados em estratégias, chamadas por CalculadoraFrete.
# A função pública e o arquivo de testes foram preservados entre as fases.
# Ponto que exigiu maior atenção: preservar a interface pública ao introduzir
# Strategy, para que os mesmos testes comprovassem o comportamento anterior.
# IA: auxiliou na organização, implementação, execução e revisão dos testes.
# A proposta inicial de tempos precisou ser corrigida, pois RED e GREEN não
# cabiam no checkpoint de 25 minutos. As evidências foram geradas por execuções
# reais; resultados esperados do pacote não foram tratados como execuções locais.
