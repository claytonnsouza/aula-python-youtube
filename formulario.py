import streamlit as st

st.title("Cadastro de Clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
dt_nasc = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo de Cliente", ["Pessoa Física", "Pessoa Jurídica"])

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("/Users/claytondealmeidasouza/Library/CloudStorage/OneDrive-Pessoal/Projeto2-python/cliente.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success("Cliente Cadastrado com Sucesso!")
    