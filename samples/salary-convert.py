def calcular_inss(salario_bruto):
    """
    Calcula o desconto do INSS com base nas faixas de contribuição atualizadas.
    """
    if salario_bruto <= 1320.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2571.29:
        return (1320.00 * 0.075) + ((salario_bruto - 1320.00) * 0.09)
    elif salario_bruto <= 3856.94:
        return (1320.00 * 0.075) + ((2571.29 - 1320.00) * 0.09) + ((salario_bruto - 2571.29) * 0.12)
    elif salario_bruto <= 7507.49:
        return (1320.00 * 0.075) + ((2571.29 - 1320.00) * 0.09) + ((3856.94 - 2571.29) * 0.12) + ((salario_bruto - 3856.94) * 0.14)
    else:
        return 877.24  # Teto máximo para o INSS


def calcular_irpf(salario_bruto, inss):
    """
    Calcula o desconto do IRPF com base nas faixas e deduções atualizadas.
    """
    base_calculo = salario_bruto - inss
    if base_calculo <= 2112.00:
        return 0  # Isento
    elif base_calculo <= 2826.65:
        return (base_calculo * 0.075) - 158.40
    elif base_calculo <= 3751.05:
        return (base_calculo * 0.15) - 370.40
    elif base_calculo <= 4664.68:
        return (base_calculo * 0.225) - 651.73
    else:
        return (base_calculo * 0.275) - 884.96


def calcular_remuneracao_liquida(salario_bruto, outros_descontos=0):
    """
    Calcula a remuneração líquida considerando INSS, IRPF e outros descontos.
    """
    inss = calcular_inss(salario_bruto)
    irpf = calcular_irpf(salario_bruto, inss)
    salario_liquido = salario_bruto - inss - irpf - outros_descontos
    return {
        "salario_bruto": salario_bruto,
        "inss": inss,
        "irpf": irpf,
        "outros_descontos": outros_descontos,
        "salario_liquido": salario_liquido,
    }


# Exemplo de uso:
if __name__ == "__main__":
    salario_bruto = float(input("Informe o salário bruto: R$ "))
    outros_descontos = float(input("Informe o total de outros descontos (ex: VT, plano de saúde, etc.): R$ "))
    
    resultado = calcular_remuneracao_liquida(salario_bruto, outros_descontos)
    
    print("\nResumo da Remuneração:")
    print(f"Salário Bruto: R$ {resultado['salario_bruto']:.2f}")
    print(f"Desconto INSS: R$ {resultado['inss']:.2f}")
    print(f"Desconto IRPF: R$ {resultado['irpf']:.2f}")
    print(f"Outros Descontos: R$ {resultado['outros_descontos']:.2f}")
    print(f"Salário Líquido: R$ {resultado['salario_liquido']:.2f}")
