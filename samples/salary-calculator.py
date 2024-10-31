# Constants for calculation

# Expected net salary
net_salary_target = 8000

# Fixed values for INSS and IRRF calculations
inss_teto = 877.24  # maximum INSS discount
irrf_deduction_per_dependant = 189.59  # per dependant deduction for IRRF (assumed as 0 here for simplicity)

# Approximate percentages for benefits and deductions
vt_percentage = 0.06  # 6% for Vale Transporte
vr_percentage = 0.02  # 2% for Vale Refeição, assuming symbolic value
co_participation_percentage = 0.05  # assumed average co-participation in health plan

# Placeholder function to calculate IRRF based on brackets (2024)
def calculate_irrf(salary_base):
    if salary_base <= 2259.20:
        return 0
    elif salary_base <= 2826.65:
        return (salary_base * 0.075) - 164.44
    elif salary_base <= 3751.05:
        return (salary_base * 0.15) - 381.44
    elif salary_base <= 4664.68:
        return (salary_base * 0.225) - 662.77
    else:
        return (salary_base * 0.275) - 884.96

# INSS rate brackets and limits for 2024
inss_brackets = [
    (0, 1320.00, 0.075),        # 7.5% up to 1,320.00
    (1320.01, 2571.29, 0.09),   # 9% from 1,320.01 to 2,571.29
    (2571.30, 3856.94, 0.12),   # 12% from 2,571.30 to 3,856.94
    (3856.95, 7507.49, 0.14)    # 14% from 3,856.95 to 7,507.49 (capped)
]

# Optimized INSS calculation based on progressive rates
def calculate_inss(salary):
    inss_discount = 0
    for lower, upper, rate in inss_brackets:
        if salary > lower and salary <= upper:
            inss_discount = salary * rate
    return inss_discount if inss_discount != 0 else inss_teto

# Optimized gross salary calculation with binary search
def calculate_optimized_gross_salary(net_target, tolerance=0.01):
    low, high = net_target, net_target * 1.5  # Start with a reasonable range
    gross_salary = (low + high) / 2  # Midpoint as initial guess

    while high - low > tolerance:
        # Calculate INSS dynamically based on the current gross salary estimate
        inss_discount = calculate_inss(gross_salary)
        
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
        
        # Adjust the binary search bounds
        if net_salary < net_target:
            low = gross_salary
        else:
            high = gross_salary
        
        # Update guess
        gross_salary = (low + high) / 2

    return gross_salary, net_salary, inss_discount, irrf_discount, vt_discount, vr_discount, co_participation_discount

# Run calculation
gross_salary, net_salary, inss_discount, irrf_discount, vt_discount, vr_discount, co_participation_discount = calculate_optimized_gross_salary(net_salary_target)

print(f'For the target compensation of: R${net_salary_target}')
print(f'Gross compensation should be: R${round(gross_salary, 2)}')
print('Applied discounts:')
print(f'INSS: R${round(inss_discount, 2)}')
print(f'IRRF: R${round(irrf_discount, 2)}')
print(f'VT: R${round(vt_discount, 2)}')
print(f'VR: R${round(vr_discount, 2)}')
print(f'Plano de Saúde: R${round(co_participation_discount, 2)}')
