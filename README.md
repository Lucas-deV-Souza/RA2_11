# Compilador Sintático LL(1) e Gerador RPN para ARMv7

**Instituição:** PUCPR - Pontifícia Universidade Católica do Paraná
**Disciplina:** Linguagens Formais e Compiladores
**Professor:** Frank Coelho de Alcantara
**Aluno:** Lucas de Souza Vieira
**GitHub:** Lucas-deV-Souza
**Grupo:** RA2_11

## Sobre o Projeto

Este projeto expande o analisador léxico da fase anterior, implementando um analisador sintático preditivo LL(1) e um gerador de Árvore Sintática Abstrata (AST) construídos em Python. Ele processa expressões matemáticas, operações relacionais e estruturas de controle de fluxo (IF/WHILE) em Notação Polonesa Reversa (RPN), convertendo-as para linguagem Assembly compatível com a arquitetura ARMv7 (utilizando a FPU para ponto flutuante), para execução no emulador CPulator.

## Como Executar

O projeto não possui menus interativos, sendo executado diretamente via linha de comando.
* Abra o terminal no diretório do projeto.
* Execute o comando passando o arquivo de teste como argumento: `python AnalisadorSintatico.py teste1.txt`
* O programa irá gerar automaticamente três arquivos de saída nomeados de acordo com o número do teste executado: o registro léxico (`tokens1.txt`), a estrutura gerada (`arvore_sintatica1.txt`) e o código final (`programa_final1.asm`).

## Testes e Validação

Os arquivos de teste contêm todas as operações matemáticas exigidas (aninhadas e com decimais), além da validação das estruturas de controle (`IF` e `WHILE`). A robustez sintática é validada em testes de falha proposital. Os resultados numéricos das operações (no padrão IEEE 754) podem ser conferidos verificando os registradores de ponto flutuante (`d0`, `d1`, `d2`) do emulador CPulator configurado para a placa DE1-SoC.