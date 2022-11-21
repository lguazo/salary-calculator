
def percentage(number, pct): return float(number) / 100 * float(pct)


def solidarity_fund_calc(salary, count_salary):

    solidarity_fund = 0

    if count_salary >= 4 and count_salary < 16:
        solidarity_fund = percentage(salary, 1)
    elif count_salary >= 16 and count_salary < 17:
        solidarity_fund = percentage(salary, 1, 2)
    elif count_salary >= 17 and count_salary < 18:
        solidarity_fund = percentage(salary, 1, 4)
    elif count_salary >= 18 and count_salary < 19:
        solidarity_fund = percentage(salary, 1, 6)
    elif count_salary >= 19 and count_salary < 20:
        solidarity_fund = percentage(salary, 1, 8)
    elif count_salary >= 20:
        solidarity_fund = percentage(salary, 2)

    return solidarity_fund


def calculate_salary(salary):
    
    format_money = lambda mount: "{:,}".format(mount)

    MIN_SALARY = 1000000
    float_salary = float(salary)
    TRANSPORT_ASSISTANT = 117.172

    health_and_pension = percentage(float_salary, 4)

    solidarity_fund_count = float_salary / MIN_SALARY
    if solidarity_fund_count > 2:
        TRANSPORT_ASSISTANT = 0
        
    solidarity_fund = solidarity_fund_calc(float_salary, solidarity_fund_count)
    net_payment = float_salary - health_and_pension * 2
    net_payment -= solidarity_fund

    data = {
        "salary": format_money(float_salary),
        "net_payment": format_money(net_payment),
        "pension": format_money(health_and_pension),
        "health": format_money(health_and_pension),
        "transport_assistant": format_money(TRANSPORT_ASSISTANT),
        "solidarity_fund": format_money(solidarity_fund)
    }

    return data
