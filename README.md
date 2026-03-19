# Sistema de Clientes - Tkinter + PostgreSQL

## Descrição

Este projeto é um **sistema de gerenciamento de clientes** desenvolvido com **Python**, usando:

- **Tkinter** para a interface gráfica  
- **PostgreSQL** como banco de dados  

O sistema permite:

- Cadastrar clientes (CREATE)  
- Listar clientes (READ)  
- Atualizar informações (UPDATE)  
- Deletar clientes (DELETE)  

Além disso, possui **mensagens visuais**, **confirmação de exclusão** e **layout profissional** com `grid()` e lista com scroll.

---

## Funcionalidades

1. Inserção de novos clientes com validação de campos.  
2. Listagem completa de clientes em uma lista com barra de rolagem.  
3. Atualização de clientes selecionados na lista.  
4. Exclusão de clientes com confirmação via popup.  
5. Interface limpa e profissional, centralizada na tela.

---

## Pré-requisitos

- Python 3.x  
- Biblioteca `psycopg2`  
- PostgreSQL instalado e configurado  
- Tkinter (já incluído no Python)

### Instalação das dependências

```bash
pip install psycopg2
