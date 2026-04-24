# Integrantes do grupo (ordem alfabética):
# Lucas de Souza Vieira = Lucas-deV-Souza
# Nome do grupo no Canvas: [RA2 11]

import sys

#Onde a analise textual comeca
def estado_inicial(caractere,acumula):
    if caractere.isdigit():
        return estado_inteiro, acumula + caractere
    if caractere == " ":
        return estado_inicial, acumula
    if caractere in "+-*%^><=!|":
        return estado_operacao, acumula + caractere
    if caractere in "/":
        return estado_duasbarra, acumula + caractere
    if caractere in "()":
        return estado_parenteses, acumula + caractere
    if caractere.isalpha():
        return estado_palavra, acumula + caractere
    if caractere in "{}": 
        return estado_chaves, acumula + caractere
    return estado_erro, acumula


#inteiros e ponto
def estado_inteiro(caractere, acumula):
    if caractere.isdigit():
        return estado_inteiro, acumula + caractere
    if caractere == ".":
        return estado_decimal, acumula + caractere
    if caractere == " ":
        token.append(('Numero',acumula))
#        print(f"token salvo de Numero {acumula}")
        return estado_inicial, ""
    return estado_erro, acumula


#decimal
def estado_decimal(caractere, acumula):
    if caractere == ".":
        return estado_erro, acumula
    if caractere.isdigit():
        return estado_decimal, acumula + caractere
    if caractere == " ":
        token.append(('Numero',acumula))
#        print(f"token salvo de Numero {acumula}")
        return estado_inicial, ""
    return estado_erro, acumula

#Algum sinal de operacao
def estado_operacao(caractere, acumula):
    # trata operadores compostos (==, !=, etc)
    if caractere == "=" and acumula in [">", "<", "=", "!"]:
        token.append(("Operacao", acumula + caractere)) 
        return estado_inicial, "" 
        
    # Se for um sinal normal de operacao, salva ele sozinho mesmo
    token.append(("Operacao", acumula))
    return estado_inicial(caractere, "")

#detecta parenteses
def estado_parenteses(caractere,acumula):
    token.append(("Parenteses", acumula))
#    print(f"Parenteses salvo {acumula}")
    return estado_inicial(caractere, "")

#detecta parlavra
def estado_palavra(caractere,acumula):
    if caractere.isalpha():
        return estado_palavra,acumula + caractere
    if caractere == " ":
        if acumula.isupper():
            token.append(("Palavra", acumula))
            return estado_inicial(caractere, "")
        else:
            return estado_erro, acumula
    return estado_erro, acumula

#detecta a se possui duas barras para o inteiro
def estado_duasbarra(caractere,acumula):
    if caractere == "/":
        token.append(("Divisao inteira", acumula + caractere))
        return estado_inicial, ""
    
    token.append(("Operacao", acumula))
    return estado_inicial(caractere, "")

#para ler colchetes
def estado_chaves(caractere,acumula):
    token.append(("Chaves", acumula))
    return estado_inicial(caractere, "")




# PRA CASO ALGUM VALOR SEJA ERRADO
def estado_erro(caractere,acumula):
    print(f"ESTADO INVALIDO QUEBROU TUDO {caractere}")
    return estado_erro, acumula




#defs para registrar a gramatica feita

def calcularFirst():
    return {
        "programa": ["START"],
        "lista_comandos": ["("],
        "lista_cauda": ["(", "Epsilon"],
        "comando": ["("],
        "corpo": ["NUMERO", "PALAVRA", "("],
        "pos_num": ["NUMERO", "PALAVRA", "(", "RES"],
        "pos_pal": ["NUMERO", "PALAVRA", "(", "Epsilon"],
        "pos_mem": ["MEM", "+", "-", "*", "|", "/", "%", "^"],
        "pos_cmd": ["NUMERO", "PALAVRA", "(", "{"],
        "fator": ["NUMERO", "PALAVRA", "("],
        "controle": ["IF", "WHILE"],
        "operador": ["+", "-", "*", "|", "/", "%", "^"],
        "bloco_comandos": ["{"]
    }

def calcularFollow():
    return {
        "programa": ["$"],
        "lista_comandos": ["END", "}"],
        "lista_cauda": ["END", "}"],
        "comando": ["(", "END", "}", "NUMERO", "PALAVRA", "{", "+", "-", "*", "|", "/", "%", "^"],
        "corpo": [")"],
        "pos_num": [")"],
        "pos_pal": [")"],
        "pos_mem": [")"],
        "pos_cmd": [")"],
        "fator": ["+", "-", "*", "|", "/", "%", "^"],
        "controle": [")"],
        "operador": [")"],
        "bloco_comandos": ["IF", "WHILE"]
    }

def construirTabelaLL1():
    return {
        "programa": {
            "START": ["START", "lista_comandos", "END"]
        },
        "lista_comandos": {
            "(": ["comando", "lista_cauda"]
        },
        "lista_cauda": {
            "(": ["comando", "lista_cauda"],
            "END": ["Epsilon"],
            "}": ["Epsilon"]
        },
        "comando": {
            "(": ["(", "corpo", ")"]
        },
        "corpo": {
            "NUMERO": ["NUMERO", "pos_num"],
            "PALAVRA": ["PALAVRA", "pos_pal"],
            "(": ["comando", "pos_cmd"]
        },
        "pos_num": {
            "NUMERO": ["NUMERO", "operador"],
            "PALAVRA": ["PALAVRA", "pos_mem"],
            "(": ["comando", "operador"],
            "RES": ["RES"]
        },
        "pos_pal": {
            "NUMERO": ["NUMERO", "operador"],
            "PALAVRA": ["PALAVRA", "operador"],
            "(": ["comando", "operador"],
            ")": ["Epsilon"]
        },
        "pos_mem": {
            "MEM": ["MEM"],
            "+": ["operador"], "-": ["operador"], "*": ["operador"], 
            "|": ["operador"], "/": ["operador"], "%": ["operador"], "^": ["operador"]
        },
        "pos_cmd": {
            "NUMERO": ["fator", "operador"],
            "PALAVRA": ["fator", "operador"],
            "(": ["fator", "operador"],
            "{": ["bloco_comandos", "controle"]
        },
        "fator": {
            "NUMERO": ["NUMERO"],
            "PALAVRA": ["PALAVRA"],
            "(": ["comando"]
        },
        "controle": {
            "IF": ["IF"],
            "WHILE": ["WHILE"]
        },
        "operador": {
            "+": ["+"], "-": ["-"], "*": ["*"], "|": ["|"], 
            "/": ["/"], "%": ["%"], "^": ["^"]
        },
        "bloco_comandos": {
            "{": ["{", "lista_comandos", "}"]
        }
    }

def exibir_resumo_gramatica():
    print("\n" + "="*50)
    print("ESTRUTURAS DA GRAMÁTICA LL(1) - ALUNO 1")
    print("="*50)
    
    firsts = calcularFirst()
    print("\n[CONJUNTOS FIRST]:")
    for nt, tokens in firsts.items():
        print(f"  FIRST({nt:15}) = {{ {', '.join(tokens)} }}")
        
    follows = calcularFollow()
    print("\n[CONJUNTOS FOLLOW]:")
    for nt, tokens in follows.items():
        print(f"  FOLLOW({nt:15}) = {{ {', '.join(tokens)} }}")
        
    # AQUI ESTÁ A MÁGICA DE PRINTAR A TABELA!
    tabela = construirTabelaLL1()
    print("\n[TABELA DE ANÁLISE LL(1)]:")
    for nt, transicoes in tabela.items():
        print(f"\n  Regra '{nt.upper()}':")
        for token, producao in transicoes.items():
            regra_texto = " ".join(producao) if producao != ["Epsilon"] else "Epsilon"
            print(f"    -> Lendo '{token}' | Produz: {regra_texto}")
            
    print("\n" + "="*50 + "\n")


#if __name__ == "__main__":
#    exibir_resumo_gramatica()








def lerArquivo(nomeArquivo):
    linhas = []
    try:
        with open(nomeArquivo, "r") as arquivo:
            for linha_orig in arquivo:
                linha_limpa = linha_orig.strip()
                if linha_limpa != "": 
                    linhas.append(linha_limpa + " ") 
        return linhas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nomeArquivo}' não foi encontrado.")
        sys.exit()


def parseExpressao(linha):
    global token # pra puxar do main
    token = []
    num_atual = estado_inicial
    bolso = ""

    for letra in linha:
        num_atual, bolso = num_atual(letra, bolso)

    return token












class No:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo       
        self.valor = valor     
        self.filhos = []       

    def adicionar_filho(self, no_filho):
        self.filhos.append(no_filho)

    def imprimir(self, nivel=0):
        indentacao = "  " * nivel
        texto = f"{indentacao}[{self.tipo}]"
        if self.valor is not None: texto += f" : {self.valor}"
        print(texto)
        for filho in self.filhos:
            filho.imprimir(nivel + 1)

    def gerar_texto_arvore(self, nivel=0):
        espacos = "  " * nivel
        texto = f"{espacos}[{self.tipo}]"
        
       
        if self.valor:
            texto += f" : {self.valor}"
        
        texto += "\n"
        

        for filho in self.filhos:
            texto += filho.gerar_texto_arvore(nivel + 1)
            
        return texto

    def salvar_arquivo(self, nome_arquivo="arvore_sintatica.txt"):
        conteudo = self.gerar_texto_arvore()
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"\n[INFO] Árvore sintática salva com sucesso em: {nome_arquivo}")

#parser para regras da gramatica
class ParserLL1:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao = 0 
        self.token_atual = self.tokens[self.posicao] if tokens else None

    def avancar(self):
        self.posicao += 1
        if self.posicao < len(self.tokens):
            self.token_atual = self.tokens[self.posicao]
        else:
            self.token_atual = ('EOF', 'EOF') 

    def erro(self, esperado):
        tipo_atual, valor_atual = self.token_atual if self.token_atual else ('Nada', 'Nada')
        print(f"Erro Sintático! Esperava '{esperado}', mas encontrou '{valor_atual}' na posição {self.posicao}.")
        sys.exit()

    def match(self, valor_esperado):
        if self.token_atual and self.token_atual[1] == valor_esperado:
            self.avancar()
        else:
            self.erro(valor_esperado)

    # verifica se o token e do tipo esperado no token
    def match_tipo(self, tipo_esperado):
        if self.token_atual and self.token_atual[0] == tipo_esperado:
            valor = self.token_atual[1] 
            self.avancar()
            return valor
        else:
            self.erro(f"Tipo {tipo_esperado}")








    #COMECO DA MINHA LINGUAGEM
    def rprograma(self):
            no = No("programa")
            
            # um teste para ver se a primeira palavra se encaixa na regra
            self.match("START")
            
            # define um objeto para o a regra
            filho_lista = self.rlista_comandos()
            
            # armazena na regra entre parentes
            no.adicionar_filho(filho_lista)
            
            # um teste para ver se a utlima palavra se encaixa na regra, mesmo esquema pros outros
            self.match("END")
            
            return no

    def rlista_comandos(self):
        no = No("lista_comandos")
        
        filho_coman = self.rcomando()
        no.adicionar_filho(filho_coman)

        filho_lcauda = self.rlista_cauda()
        no.adicionar_filho(filho_lcauda)

        return no

    def rlista_cauda(self):
            no = No("lista_cauda")
            
            if self.token_atual is None:
                return no

            valor_atual = self.token_atual[1]

            
            if valor_atual == "(":
                filho_coman = self.rcomando()
                no.adicionar_filho(filho_coman)
                
                filho_cauda = self.rlista_cauda()
                no.adicionar_filho(filho_cauda)
                
           
            else:
                # Para evitar usar o simbolo ou dar conflito no caractere, represento ε como Epsilon
                no.valor = "Epsilon" 

            return no

    def rcomando(self):
        no = No("comando")

        self.match('(')

        filho_corpo = self.rcorpo()
        no.adicionar_filho(filho_corpo)

        self.match(')')

        return no

    def rcorpo(self):
        no = No("corpo")
            
        tipo_atual = self.token_atual[0]   
        valor_atual = self.token_atual[1]  
            
       
        if tipo_atual == "Numero":
            valor_num = self.match_tipo("Numero")
            no.adicionar_filho(No("Numero", valor_num))

            no.adicionar_filho(self.rpos_num())    

                
        
        elif tipo_atual == "Palavra":
            valor_pal = self.match_tipo("Palavra")
            no.adicionar_filho(No("Palavra", valor_pal))
                
            no.adicionar_filho(self.rpos_pal()) 
                
        
        elif valor_atual == "(":
            no.adicionar_filho(self.rcomando()) 
            no.adicionar_filho(self.rpos_cmd()) 
                
        else:
            self.erro("Numero, Palavra ou '('")
                
        return no

    def rpos_num(self):
            no = No("pos_num")
            
            tipo_atual = self.token_atual[0]
            valor_atual = self.token_atual[1]
            
            
            if tipo_atual == "Numero":
                valor_num = self.match_tipo("Numero")
                no.adicionar_filho(No("Numero", valor_num))
                no.adicionar_filho(self.roperador())
                
            
            elif tipo_atual == "Palavra":
                if valor_atual == "RES":
                    self.match("RES")
                    no.adicionar_filho(No("ComandoEspecial", "RES"))
                else:
                    valor_pal = self.match_tipo("Palavra")
                    no.adicionar_filho(No("Palavra", valor_pal))
                    no.adicionar_filho(self.rpos_mem())
                    
            
            elif valor_atual == "(":
                no.adicionar_filho(self.rcomando())
                no.adicionar_filho(self.roperador())
                
            else:
                self.erro("Numero, Palavra, '(' ou 'RES'")
                
            return no

    def rpos_pal(self):
            no = No("pos_pal")
            
            tipo_atual = self.token_atual[0]
            valor_atual = self.token_atual[1]
            
            
            if tipo_atual == "Numero":
                valor_num = self.match_tipo("Numero")
                no.adicionar_filho(No("Numero", valor_num))
                no.adicionar_filho(self.roperador())
                
            
            elif tipo_atual == "Palavra":
                valor_pal = self.match_tipo("Palavra")
                no.adicionar_filho(No("Palavra", valor_pal))
                no.adicionar_filho(self.roperador())
                    
            
            elif valor_atual == "(":
                no.adicionar_filho(self.rcomando())
                no.adicionar_filho(self.roperador())

                
            else:
                no.valor = "Epsilon"
                
            return no

    def rpos_mem(self):
        no = No("pos_mem")

        tipo_atual = self.token_atual[0]
        valor_atual = self.token_atual[1]

        if valor_atual == "MEM":
            self.match("MEM")
            no.adicionar_filho(No("ComandoEspecial", "MEM"))
                
        else:
            no.adicionar_filho(self.roperador())

        return no

    def rpos_cmd(self):
            no = No("pos_cmd")
            valor_atual = self.token_atual[1]

            
            if valor_atual == "{":
                no.adicionar_filho(self.rbloco_comandos())
                no.adicionar_filho(self.rcontrole())
                
            
            else:
                no.adicionar_filho(self.rfator())
                no.adicionar_filho(self.roperador())

            return no

    def rfator(self):
        no = No("fator")

        tipo_atual = self.token_atual[0]
        valor_atual = self.token_atual[1]

        if tipo_atual == "Numero":
            valor_num = self.match_tipo("Numero")
            no.adicionar_filho(No("Numero", valor_num))


        elif tipo_atual == "Palavra":
            valor_pal = self.match_tipo("Palavra")
            no.adicionar_filho(No("Palavra", valor_pal))

            
        elif valor_atual == "(":
            no.adicionar_filho(self.rcomando())

        return no

    def roperador(self):
        no = No("operador")
        valor_atual = self.token_atual[1]
            
        
        if valor_atual in ["+", "-", "*", "/", "|", "%", "^", ">", "<", "=", "==", "!="]:
            valor_op = self.match_tipo("Operacao") 
            no.adicionar_filho(No("Sinal", valor_op))
        else:
            self.erro("Operador Matemático (+, -, *, etc)")
                
        return no

    def rcontrole(self):
        no = No("controle")
        valor_atual = self.token_atual[1]
            
        if valor_atual == "IF":
            self.match("IF")
            no.adicionar_filho(No("Condicional", "IF"))
        elif valor_atual == "WHILE":
            self.match("WHILE")
            no.adicionar_filho(No("Laco", "WHILE"))
        else:
            self.erro("'IF' ou 'WHILE'")
                
        return no

    def rbloco_comandos(self):
        no = No("bloco_comandos")
        self.match("{")

        no.adicionar_filho(self.rlista_comandos())
        self.match("}")
            
        return no










class GeradorAssembly:
    def __init__(self):
        self.codigo = []
        self.data = []  # secao .data para alocar os floats na memoria
        self.contador_num = 0
        
        # operacoes para comandos do Cpulator ARMv7
        self.operacoes = {
            "+": "VADD.F64 D2, D1, D0",
            "-": "VSUB.F64 D2, D1, D0",
            "*": "VMUL.F64 D2, D1, D0",
            "/": "VDIV.F64 D2, D1, D0",
            ">": "VCMP.F64 D1, D0",
            "<": "VCMP.F64 D1, D0",
            "=": "VCMP.F64 D1, D0"
        } #Alias, o v serve para lidar com numeros decimais e o .f64 e para jogar os valores no registrador double d0,d1,d2...


    def gerar(self, no_raiz):
        self.codigo.append("    @ Inicializando o programa") #@ para comentarios no asm
        
        # pra percorrer a arvora
        self.visitar(no_raiz)
        
        self.codigo.append("    @ Fim do programa")
        
        #liga .data ao ,text
        texto_final = [".data"] + self.data
        texto_final += [".text", ".global _start", "_start:"] + self.codigo
        texto_final.append("    .end")
        
        return "\n".join(texto_final)

    def visitar(self, no):
        # Condição de parada de segurança
        if no is None or no.valor == "Epsilon":
            return

        # ve as folhas/filhos
        for filho in no.filhos:
            self.visitar(filho)

        
        nome = no.tipo
        valor = no.valor

        
        if nome == "Numero":
            nome_var = f"valor_{self.contador_num}"
            self.contador_num += 1
            
            # float no .data
            self.data.append(f"{nome_var}: .double {valor}")
            
            # da memoria pro regs
            self.codigo.append(f"    @ Carregando numero {valor}")
            self.codigo.append(f"    LDR R0, ={nome_var}")
            self.codigo.append(f"    VLDR D7, [R0]")
            self.codigo.append(f"    VPUSH {{D7}}")
            

        elif nome == "Palavra":
            self.codigo.append(f"    @ Carregando variavel {valor}")
            self.codigo.append(f"    LDR R0, ={valor}")
            self.codigo.append(f"    VPUSH {{R0}}")


        elif nome == "Sinal":
            op_asm = self.operacoes.get(valor, f"    @ ERRO: Op {valor} desconhecida")
            self.codigo.append(f"    @ Operacao: {valor}")
            self.codigo.append("    VPOP {D0}  @ Desempilha 2o operando")
            self.codigo.append("    VPOP {D1}  @ Desempilha 1o operando")
            self.codigo.append(f"    {op_asm}")
            self.codigo.append("    VPUSH {D2} @ Empilha o resultado")



# o principal
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Erro: faltou o arquivo de texto!\nExemplo: python AnalisadorSintatico.py teste1.txt")
        sys.exit()
    
    nome_arquivo = sys.argv[1]
    
    numero_teste = nome_arquivo.replace("teste", "").replace(".txt", "")

    linhas = lerArquivo(nome_arquivo)
    
    # analisador.py da fase 1
    tokens_completos = []
    for linha in linhas:
        tokens_linha = parseExpressao(linha)
        tokens_completos.extend(tokens_linha)

    print("\nTokens gerados:")
    for t in tokens_completos:
        print(t)


    nome_arquivo_tokens = f"tokens{numero_teste}.txt"
    with open(nome_arquivo_tokens, "w") as f:
        for t in tokens_completos:
            f.write(f"{t}\n")
    print(f"Tokens salvos em '{nome_arquivo_tokens}'")

    # analisadorsintatico.py da fase 2
    print("\nIniciando parser...")
    parser = ParserLL1(tokens_completos)
    arvore_sintatica = parser.rprograma()
    

    print("\nArvore Sintatica:")
    arvore_sintatica.imprimir()

    nome_arquivo_arvore = f"arvore_sintatica{numero_teste}.txt"
    arvore_sintatica.salvar_arquivo(nome_arquivo_arvore)

    # assembly arquivo em asm
    print("\nGerando assembly: ")
    gerador = GeradorAssembly()
    codigo_asm = gerador.gerar(arvore_sintatica)
    
    nome_arquivo_asm = f"programa_final{numero_teste}.asm"
    with open(nome_arquivo_asm, "w", encoding="utf-8") as f:
        f.write(codigo_asm)
        
    print(f"Salvo no arquivo '{nome_arquivo_asm}'!")

    #Lembrar de colocar no terminal: python AnalisadorSintatico.py teste1.txt

