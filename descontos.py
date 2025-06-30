# Sistema de Verificação de Elegibilidade para Desconto em Cursos

def verificar_elegibilidade(idade, profissao):
    
    if idade < 18:
        return "Você não é elegível para desconto, pois é menor de idade."
    
    if 18 <= idade <= 25:
        return "Você é elegível para desconto (Apresente Críterios De idade)."
    
    if idade > 25:
        return "Vôce é elegível para desconto, atendendo certos críterios."
    
    if profissao.lower() == 'estudante ativo':
        return "Você é estudante ativo, receberá desconto de 10% no curso."
    
    if profissao.lower() == 'desempregado':
        return "Você é desempregado, receberá desconto de 15% no curso."
    
    if profissao.lower() == 'empregado':
        return "Nao séra aceito desconto, pois nao esta adepto a situaçao profissional."
    
    conhecimento = input("Você possui conhecimento prévio na área do curso? (sim/não): ").strip().lower()
    if conhecimento == 'sim':
        return "Você possui conhecimento prévio, receberá desconto de 5% no curso."
    elif conhecimento == 'não':
        return "Você não possui conhecimento prévio, não receberá desconto."
    
    participaçao = input("Você participa ativamente de comunidades ou grupos relacionados ao curso? (sim/não): ").strip().lower()
    if participaçao  == 'sim':
        return "Você participa ativamente de comunidades, receberá desconto de 20% no curso."
    elif participaçao == 'não':
        return "Você não participa ativamente de comunidades, não receberá desconto."
    
def calcular_desconto(idade, profissao, conhecimento, participaçao):
    desconto = 0
    
    if 18 <= idade <= 25:
        desconto += 0.10
    elif idade > 25:
        desconto += 0.05
    
    if profissao == 'estudante ativo':
        desconto += 0.10
    elif profissao == 'desempregado':
        desconto += 0.15
    
    if conhecimento == 'sim':
        desconto += 0.05

    if participaçao == 'sim':
        desconto += 0.20

    return desconto

def main():
    idade = int(input("Digite sua idade: "))
    profissao = input("Digite sua profissão (estudante ativo, desempregado, empregado): ").strip()
    conhecimento = input("Você possui conhecimento prévio na área do curso? (sim/não): ").strip().lower()
    participaçao = input("Você participa ativamente de comunidades ou grupos relacionados ao curso? (sim/não): ").strip().lower()

    if idade < 18:
        print("Você não é elegível para desconto por ser menor de idade.")
        return
    if profissao == 'empregado':
        print("Você não é elegível para desconto deviado à sua situação profissional.")
        return
    
    desconto = calcular_desconto(idade, profissao, conhecimento, participaçao)
    print(f"Você é elegível para um desconto de {desconto * 100:.0f}% no curso.")

if __name__ == "__main__":
    main()
