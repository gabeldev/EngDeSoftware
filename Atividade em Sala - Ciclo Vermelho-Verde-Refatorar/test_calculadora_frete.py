# PLANO DA ATIVIDADE — CICLO VERMELHO / VERDE / REFATORAR
#
# Componente: cálculo de frete de um pedido.
# Casos escolhidos (distância = 10 km):
# 1. Retirada no local: frete gratuito (esperado: 0).
# 2. Entrega econômica: 10 + distância (esperado: 20).
# 3. Entrega expressa: 20 + 2 * distância (esperado: 40).
#
# Padrão de projeto planejado: Strategy.
# Justificativa: encapsular cada regra de cálculo em uma estratégia, evitando
# condicionais na lógica de cálculo e facilitando novas modalidades.
#
# Planejamento estimado para 120 minutos:
# - Plano: 10 min.
# - RED (escrever e executar testes falhando): 10 min.
# - GREEN (implementação mínima): 5 min.
# - REFACTOR (aplicar Strategy, verificar e documentar): 85 min.
# - Autoavaliação: 10 min.
# O tempo de GREEN foi ajustado no planejamento para concluir RED e GREEN
# até o checkpoint de 25 minutos, sem reduzir as três variações.
#
# Uso planejado de IA: auxílio na organização, escrita/revisão dos testes,
# implementação e execução dos comandos.

from calculadora_frete import calcular_frete


def test_retirada_gratuita():
    assert calcular_frete("retirada", 10) == 0


def test_entrega_economica():
    assert calcular_frete("economica", 10) == 20


def test_entrega_expressa():
    assert calcular_frete("expressa", 10) == 40
