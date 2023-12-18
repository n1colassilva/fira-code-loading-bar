
[🇺🇸/🇬🇧 version](../README.MD)
# O que é isto?

Este projeto providencia um modulo para criar barras de carregamento usando os símbolos especiais da fonte [fira code](https://github.com/tonsky/FiraCode).

![[../images/fira_symbols.png]]


## Overview

este projeto providencia uma função para gerar barras de carregamento:

```
generate_loading_bar(
    current_value = 50, # How much progress
    total_value = 100,  # Of how much
    bar_length = 100    # Optional, default is 100
    )
```

este código irá gerar uma bela barra de carregamento:
![[..images/loading_bar_example.png]]
Para melhores resultados ative ligaturas de fonte.

## Como usar

Caso você tenha menos experiência, é assim que você faz a barra ser atualizada ao invéz de escrever uma nova linha, isto é um exemplo de uso:
```
for i in range(1, 100000):

    print(f'\r{generate_loading_bar(i, 100000, 100)}', end='')

```
O \r é chamado de retorno de carruagem (carriage return) ele retorna o "cursor" da escrita de volta ao início da linha, o nome é em referência à maquinas de escrever.

No fim do print o padrão é o python adicinar um simbolo de nova linha (\n) ao final da linha, alterando este comportamento padrão e usando o returno de carruagem podemos fazer este loop escrever uma linha, voltar para o início e escrever novamente.
