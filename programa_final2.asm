.data
valor_0: .double 10
valor_1: .double 5
valor_2: .double 2
valor_3: .double 3
valor_4: .double 4
valor_5: .double 2
valor_6: .double 5
valor_7: .double 5
valor_8: .double 10
valor_9: .double 2
valor_10: .double 1
valor_11: .double 10
valor_12: .double 1
valor_13: .double 1
valor_14: .double 100
valor_15: .double 10
.text
.global _start
_start:
    @ Inicializando o programa
    @ Carregando numero 10
    LDR R0, =valor_0
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 5
    LDR R0, =valor_1
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: >
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VCMP.F64 D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 2
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
    @ Carregando numero 4
    LDR R0, =valor_4
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 2
    LDR R0, =valor_5
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: +
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VADD.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 5
    LDR R0, =valor_6
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 5
    LDR R0, =valor_7
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: ==
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
        @ ERRO: Op == desconhecida
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 10
    LDR R0, =valor_8
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 2
    LDR R0, =valor_9
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: /
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VDIV.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 1
    LDR R0, =valor_10
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 10
    LDR R0, =valor_11
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: <
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VCMP.F64 D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 1
    LDR R0, =valor_12
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 1
    LDR R0, =valor_13
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: +
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VADD.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Carregando numero 100
    LDR R0, =valor_14
    VLDR D7, [R0]
    VPUSH {D7}
    @ Carregando numero 10
    LDR R0, =valor_15
    VLDR D7, [R0]
    VPUSH {D7}
    @ Operacao: /
    VPOP {D0}  @ Desempilha 2o operando
    VPOP {D1}  @ Desempilha 1o operando
    VDIV.F64 D2, D1, D0
    VPUSH {D2} @ Empilha o resultado
    @ Fim do programa
    .end