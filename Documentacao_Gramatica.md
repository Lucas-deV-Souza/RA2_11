# Relatório de Engenharia - Gramática e Análise LL(1)
**Grupo:** RA2_11

## 1. Regras de Produção (Gramática Formal)
Abaixo está a gramática numerada. Os números servem como legenda para a Tabela de Análise LL(1).

1. `programa ::= 'START' lista_comandos 'END'`
2. `lista_comandos ::= comando lista_cauda`
3. `lista_cauda ::= comando lista_cauda`
4. `lista_cauda ::= ε`
5. `comando ::= '(' corpo ')'`
6. `corpo ::= NUMERO pos_num`
7. `corpo ::= PALAVRA pos_pal`
8. `corpo ::= comando pos_cmd`
9. `pos_num ::= NUMERO operador`
10. `pos_num ::= PALAVRA pos_mem`
11. `pos_num ::= comando operador`
12. `pos_num ::= 'RES'`
13. `pos_pal ::= NUMERO operador`
14. `pos_pal ::= PALAVRA operador`
15. `pos_pal ::= comando operador`
16. `pos_pal ::= ε`
17. `pos_mem ::= 'MEM'`
18. `pos_mem ::= operador`
19. `pos_cmd ::= fator operador`
20. `pos_cmd ::= bloco_comandos controle`
21. `fator ::= NUMERO`
22. `fator ::= PALAVRA`
23. `fator ::= comando`
24. `controle ::= 'IF'`
25. `controle ::= 'WHILE'`
26. `operador ::= '+' | '-' | '*' | '|' | '/' | '%' | '^' | '>' | '<' | '=' | '==' | '!='`
27. `bloco_comandos ::= '{' lista_comandos '}'`

> **Nota Técnica:** O símbolo **ε** representa o vazio. No código Python, ele é tratado pela string `"Epsilon"` para garantir que o programa funcione sem erros de caracteres especiais de encoding.

## 2. Conjuntos FIRST e FOLLOW

**FIRST:**
* FIRST(programa) = { 'START' }
* FIRST(lista_comandos) = { '(' }
* FIRST(lista_cauda) = { '(', ε }
* FIRST(comando) = { '(' }
* FIRST(corpo) = { NUMERO, PALAVRA, '(' }
* FIRST(pos_num) = { NUMERO, PALAVRA, '(', 'RES' }
* FIRST(pos_pal) = { NUMERO, PALAVRA, '(', ε }
* FIRST(pos_mem) = { 'MEM', '+', '-', '*', '|', '/', '%', '^', '>', '<', '=', '==', '!=' }
* FIRST(pos_cmd) = { NUMERO, PALAVRA, '(', '{' }
* FIRST(fator) = { NUMERO, PALAVRA, '(' }
* FIRST(controle) = { 'IF', 'WHILE' }
* FIRST(operador) = { '+', '-', '*', '|', '/', '%', '^', '>', '<', '=', '==', '!=' }
* FIRST(bloco_comandos) = { '{' }

**FOLLOW:**
* FOLLOW(programa) = { $ }
* FOLLOW(lista_comandos) = { 'END', '}' }
* FOLLOW(lista_cauda) = { 'END', '}' }
* FOLLOW(comando) = { '(', 'END', '}', NUMERO, PALAVRA, '{', '+', '-', '*', '|', '/', '%', '^', '>', '<', '=', '==', '!=', ')' }
* FOLLOW(corpo) = { ')' }
* FOLLOW(pos_num) = { ')' }
* FOLLOW(pos_pal) = { ')' }
* FOLLOW(pos_mem) = { ')' }
* FOLLOW(pos_cmd) = { ')' }
* FOLLOW(fator) = { '+', '-', '*', '|', '/', '%', '^', '>', '<', '=', '==', '!=' }
* FOLLOW(operador) = { ')' }
* FOLLOW(bloco_comandos) = { 'IF', 'WHILE' }

## 3. Tabela de Análise LL(1)

| Não-Terminal | START | END | ( | ) | { | } | NUMERO | PALAVRA | Operador | RES | MEM | IF/WHILE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **programa** | 1 | | | | | | | | | | | |
| **lista_com.** | | | 2 | | | | | | | | | |
| **lista_cauda** | | 4 | 3 | | | 4 | | | | | | |
| **comando** | | | 5 | | | | | | | | | |
| **corpo** | | | 8 | | | | 6 | 7 | | | | |
| **pos_num** | | | 11 | | | | 9 | 10 | | 12 | | |
| **pos_pal** | | | 15 | 16 | | | 13 | 14 | | | | |
| **pos_mem** | | | | | | | | | 18 | | 17 | |
| **pos_cmd** | | | 19 | | 20 | | 19 | 19 | | | | |
| **fator** | | | 23 | | | | 21 | 22 | | | | |
| **controle** | | | | | | | | | | | | 24, 25 |
| **operador** | | | | | | | | | 26 | | | |
| **bloco_com.** | | | | | 27 | | | | | | | |

## 4. Árvore Sintática (Resultado da Última Execução)
Abaixo está a estrutura gerada pelo compilador ao ler o arquivo `teste2.txt`:

```text
[programa]
  [lista_comandos]
    [comando]
      [corpo]
        [comando]
          [corpo]
            [Numero] : 10
            [pos_num]
              [Numero] : 5
              [operador]
                [Sinal] : >
        [pos_cmd]
          [bloco_comandos]
            [lista_comandos]
              [comando]
                [corpo]
                  [Numero] : 2
                  [pos_num]
                    [Numero] : 3
                    [operador]
                      [Sinal] : *
              [lista_cauda]
                [comando]
                  [corpo]
                    [Numero] : 4
                    [pos_num]
                      [Numero] : 2
                      [operador]
                        [Sinal] : +
                [lista_cauda] : Epsilon
          [controle]
            [Condicional] : IF
    [lista_cauda]
      [comando]
        [corpo]
          [comando]
            [corpo]
              [Numero] : 5
              [pos_num]
                [Numero] : 5
                [operador]
                  [Sinal] : ==
          [pos_cmd]
            [bloco_comandos]
              [lista_comandos]
                [comando]
                  [corpo]
                    [Numero] : 10
                    [pos_num]
                      [Numero] : 2
                      [operador]
                        [Sinal] : /
                [lista_cauda] : Epsilon
            [controle]
              [Condicional] : IF
      [lista_cauda]
        [comando]
          [corpo]
            [comando]
              [corpo]
                [Numero] : 1
                [pos_num]
                  [Numero] : 10
                  [operador]
                    [Sinal] : <
            [pos_cmd]
              [bloco_comandos]
                [lista_comandos]
                  [comando]
                    [corpo]
                      [Numero] : 1
                      [pos_num]
                        [Numero] : 1
                        [operador]
                          [Sinal] : +
                  [lista_cauda] : Epsilon
              [controle]
                [Laco] : WHILE
        [lista_cauda]
          [comando]
            [corpo]
              [Numero] : 100
              [pos_num]
                [Numero] : 10
                [operador]
                  [Sinal] : /
          [lista_cauda] : Epsilon
