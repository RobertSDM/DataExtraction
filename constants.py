from dotenv import load_dotenv

load_dotenv()

table_columns_and_types = [
    ("Loja", "str"),
    ("Fabricante", "str"),
    ("Produto", "int"),
    ("Quantidade Pedida", "int"),
    ("Quantidade Recebida", "int"),
    ("Quantidade Corte", "int"),
    ("Data", "str"),
    ("Hora", "str"),
    ("Usuário", "str"),
]

whitespace_limit = 12
column_line_position = 5
