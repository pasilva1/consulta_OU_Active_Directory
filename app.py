import os
import pandas as pd
from ldap3 import Server, Connection, ALL, SUBTREE
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Variáveis de conexão
AD_SERVER = os.getenv("AD_SERVER")
AD_USER = os.getenv("AD_USER")
AD_PASSWORD = os.getenv("AD_PASSWORD")
BASE_DN = os.getenv("BASE_DN")

# Ler o CSV
csv_file = 'resultado.csv' # Esse arquivo precisa ter, no mínimo, uma coluna chamada LoginRede que representa o sAMAccountName do AD (o login do usuário).
df = pd.read_csv(csv_file)

# Conectar ao AD
server = Server(AD_SERVER, get_info=ALL)
conn = Connection(server, user=AD_USER, password=AD_PASSWORD, auto_bind=True)

# Loop pelos usuários do CSV
for index, row in df.iterrows():
    login = row['LoginRede'] # Esse arquivo precisa ter, no mínimo, uma coluna chamada LoginRede que representa o sAMAccountName do AD (o login do usuário).

    # Buscar distinguishedName do usuário
    search_filter = f'(sAMAccountName={login})'

    conn.search(
        search_base=BASE_DN,
        search_filter=search_filter,
        search_scope=SUBTREE,
        attributes=['distinguishedName']
    )

    if conn.entries:
        user_dn = conn.entries[0].distinguishedName.value

        # Extrair as OUs do DN
        ou_parts = [part for part in user_dn.split(',') if part.startswith('OU=')]
        ou_path = ' / '.join(part.replace('OU=', '') for part in ou_parts)

        print("")
        print(f"Usuário {login} está na OU: {ou_path}")
        print(f"DN completo: {user_dn}")

    else:
        print(f"Usuário {login} não encontrado no AD.")

# Desconectar
conn.unbind()
