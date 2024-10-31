# Constants for calculation

# Expected net salary
net_salary_target = 8500

# Fixed values for INSS and IRRF calculations
inss_teto = 877.24  # maximum INSS discount
irrf_deduction_per_dependant = 189.59  # per dependant deduction for IRRF (assumed as 0 here for simplicity)

# Approximate percentages for benefits and deductions
vt_percentage = 0.06  # 6% for Vale Transporte
vr_percentage = 0.02  # 2% for Vale Refeição, assuming symbolic value
co_participation_percentage = 0.05  # assumed average co-participation in health plan

# Placeholder function to calculate IRRF based on brackets (2024)
def calculate_irrf(salary_base):
    if salary_base <= 2112:
        return 0
    elif salary_base <= 2826.65:
        return (salary_base * 0.075) - 158.4
    elif salary_base <= 3751.05:
        return (salary_base * 0.15) - 370.4
    elif salary_base <= 4664.68:
        return (salary_base * 0.225) - 651.73
    else:
        return (salary_base * 0.275) - 884.96

# Iterative approach to estimate the gross salary
def calculate_gross_salary(net_target, tolerance=0.01):
    gross_salary = net_target / 0.7  # Start with an approximate multiplier
    
    while True:
        # INSS calculation (capped at maximum discount if gross salary is higher than the INSS cap)
        inss_discount = inss_teto if gross_salary > 7507.49 else gross_salary * 0.14
        
        # Base salary for IRRF after INSS
        irrf_base_salary = gross_salary - inss_discount
        
        # IRRF calculation
        irrf_discount = calculate_irrf(irrf_base_salary)
        
        # Other deductions
        vt_discount = gross_salary * vt_percentage
        vr_discount = gross_salary * vr_percentage
        co_participation_discount = gross_salary * co_participation_percentage
        
        # Calculate net salary
        net_salary = gross_salary - (inss_discount + irrf_discount + vt_discount + vr_discount + co_participation_discount)
        
        # Check if the calculated net salary meets the target within tolerance
        if abs(net_salary - net_target) < tolerance:
            break
        elif net_salary < net_target:
            gross_salary *= 1.01  # Increment gross salary if net is below target
        else:
            gross_salary *= 0.99  # Decrement gross salary if net is above target

    return gross_salary, net_salary, inss_discount, irrf_discount, vt_discount, vr_discount, co_participation_discount


gross_salary, net_salary, inss_discount, irrf_discount, vt_discount, vr_discount, co_participation_discount = calculate_gross_salary(net_salary_target)
# gross_salary, net_salary, inss_discount, irrf_discount, vt_discount, vr_discount, co_participation_discount
# Run calculation
print(f'For the target compensation of: R${net_salary_target}')
print(f'Gross compensation should be: R${round(gross_salary, 2)}')
print('Applied discounts:')
print(f'INSS: R${round(inss_discount,2)}')
print(f'IRRF: R${round(irrf_discount, 2)}')
print(f'VT: R${round(vt_discount, 2)}')
print(f'VR: R${round(vr_discount, 2)}')
print(f'Plano de Saúde: R${round(co_participation_discount, 2)}')
