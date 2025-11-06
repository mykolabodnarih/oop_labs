def make_vat(rate: float) -> float:
    """
    Повертає функцію, яка додає ПДВ (rate %) до суми покупки.
    """

    def apply(amount: float) -> float:
        """
        Обчислює ціну з урахуванням ПДВ.
        """
        return amount * (1 + rate / 100)

    return apply

vat20 = make_vat(20)   
vat7 = make_vat(7)     
vat0 = make_vat(0)     

print(vat20(100))  
print(vat7(500))   
print(vat0(250))   