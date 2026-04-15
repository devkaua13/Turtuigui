meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7070),
]

for vendedor, qtd in vendas:
    if qtd >= meta:
        print("{} bateu a meta, vendeu {} unidade" .format(vendedor, qtd))