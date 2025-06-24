# Consulta de Usuários no Active Directory via CSV

## Descrição

Este script realiza uma consulta no Active Directory (AD) utilizando como base um arquivo CSV que contém a lista de usuários. Para cada usuário listado, o script consulta no AD se o usuário existe, obtém o Distinguished Name (DN) e informa em qual Unidade Organizacional (OU) o usuário está localizado.

## Requisitos do Arquivo resultado.csv

O arquivo `resultado.csv` deve conter obrigatoriamente uma coluna com o nome **`LoginRede`**, que corresponde ao **sAMAccountName** do Active Directory.

### Estrutura mínima do CSV

```csv
LoginRede
joao.silva
maria.souza
pedro.lima

### A coluna LoginRede deve conter o login de rede dos usuários exatamente como estão cadastrados no AD.

Não é necessário incluir outras colunas, mas o script pode ser adaptado caso precise de mais informações.
