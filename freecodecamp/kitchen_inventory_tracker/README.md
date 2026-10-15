# Build a Kitchen Inventory Tracker

Laboratório de Python do freeCodeCamp focado no uso de funções para consultar e atualizar o inventário de uma cozinha.

## Objetivo

Praticar a criação e a chamada de funções, o uso de parâmetros e valores de retorno, além de aplicar estruturas condicionais para controlar o consumo de ingredientes disponíveis.

## Conceitos praticados

- **Variáveis:** armazenamento das quantidades de ingredientes.
- **Funções:** organização do código em blocos reutilizáveis.
- **Parâmetros e argumentos:** passagem de valores para funções.
- **Retorno de valores:** utilização de `return` para devolver a quantidade atualizada de ingredientes.
- **Condicionais:** uso de `if/else` para verificar a disponibilidade de ovos.
- **Operadores de comparação:** verificação da quantidade de ingredientes disponíveis.
- **Operadores aritméticos:** cálculo do total de itens e da quantidade restante.
- **f-strings:** formatação de mensagens com valores dinâmicos.
- **Escopo de variáveis:** compreensão da diferença entre parâmetros locais e variáveis globais.

## Funcionalidades desenvolvidas

- Consulta do estoque de ingredientes da cozinha.
- Cálculo e exibição da quantidade total de itens.
- Verificação da disponibilidade de ovos antes do consumo.
- Atualização da quantidade de ovos por meio do valor retornado por uma função.
- Simulação do preparo de um ovo frito.
- Exibição de mensagens de sucesso ou de falta de ingredientes.

## Funções implementadas

### `check_kitchen_stock()`

Exibe as quantidades disponíveis de ovos, farinha e açúcar, além do total de itens no inventário.

### `use_eggs(available_eggs, eggs_to_use)`

Verifica se há ovos suficientes para atender à quantidade solicitada. Se houver, retorna a quantidade restante; caso contrário, informa que o estoque é insuficiente e retorna a quantidade original.

### `make_fried_egg(available_eggs)`

Verifica se há pelo menos um ovo disponível. Quando possível, simula o preparo de um ovo frito, utiliza a função `use_eggs()` e retorna a quantidade restante de ovos.

## Aprendizados

O laboratório reforçou a importância de dividir um programa em funções e de utilizar valores de retorno para transportar resultados entre diferentes partes do código.

Também demonstrou como estruturas condicionais podem controlar o comportamento de um programa de acordo com os recursos disponíveis.

## Tecnologias

- Python 3
- freeCodeCamp

## Status

Concluído.
