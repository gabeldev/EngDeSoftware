# Cálculo de frete — Ciclo Vermelho–Verde–Refatorar

Componente novo desenvolvido em Python com pytest para a atividade de Engenharia de Software.

## Requisitos

| Modalidade | Custo em reais para a distância em km | Exemplo: 10 km |
| --- | --- | --- |
| `retirada` | Gratuito | R$ 0 |
| `economica` | 10 + distância | R$ 20 |
| `expressa` | 20 + 2 × distância | R$ 40 |

A interface pública é `calcular_frete(modalidade, distancia)`.
O protótipo considera distâncias não negativas e modalidades válidas.

## Execução

Na pasta desta atividade, com Python 3.9 ou superior:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

## Fases do TDD

- `red`: três testes escritos primeiro; o contrato lança `NotImplementedError`.
- `green`: implementação mínima com condicionais.
- `refactor`: aplicação de Strategy, preservando a interface pública e os testes.

As saídas reais das fases ficam em `evidencias/red.txt`, `evidencias/green.txt` e `evidencias/refactor.txt`.
Para conferir os commits, execute `git log --oneline --reverse -- .` nesta pasta.

## Entrega

O plano está no topo dos testes, e a autoavaliação está no final do código de produção.
Houve uso de IA para organização, implementação, revisão dos testes e execução dos comandos.
Os PDFs são materiais locais de estudo e estão excluídos do Git e da pasta de entrega.
