.data
valor_0: .double 4.5
valor_1: .double 2.0
valor_2: .double 10
valor_3: .double 3
valor_4: .double 15.5
valor_5: .double 5.0
valor_6: .double 20
valor_7: .double 4
valor_8: .double 2
valor_9: .double 3
valor_10: .double 10
valor_11: .double 2
valor_12: .double 8
valor_13: .double 2
valor_14: .double 3.14
valor_15: .double 2.0
valor_16: .double 100
valor_17: .double 10
valor_18: .double 7
valor_19: .double 7
.text
.global _start
_start:
    @ Inicializando o programa
    @ Carregando numero 4.5
    LDR R0, =valor_0
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 2.0
    LDR R0, =valor_1
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: +
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VADD.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 10
    LDR R0, =valor_2
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 3
    LDR R0, =valor_3
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: *
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VMUL.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 15.5
    LDR R0, =valor_4
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 5.0
    LDR R0, =valor_5
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: -
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VSUB.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 20
    LDR R0, =valor_6
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 4
    LDR R0, =valor_7
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: /
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VDIV.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 2
    LDR R0, =valor_8
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 3
    LDR R0, =valor_9
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: ^
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
        @ ERRO: Op ^ desconhecida
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 10
    LDR R0, =valor_10
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 2
    LDR R0, =valor_11
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: %
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
        @ ERRO: Op % desconhecida
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 8
    LDR R0, =valor_12
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 2
    LDR R0, =valor_13
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: |
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
        @ ERRO: Op | desconhecida
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 3.14
    LDR R0, =valor_14
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 2.0
    LDR R0, =valor_15
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: *
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VMUL.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 100
    LDR R0, =valor_16
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 10
    LDR R0, =valor_17
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: /
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VDIV.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 7
    LDR R0, =valor_18
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 7
    LDR R0, =valor_19
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: +
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VADD.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Fim do programa
    .end