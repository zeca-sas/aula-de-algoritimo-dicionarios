biblioteca = {
    "Dom Casmurro": {"usuario": "Ana", "dias": 5},
    "1984": {"usuario": "Carlos", "dias": 12},
    "O Hobbit": {"usuario": "Marina", "dias": 3}
}

atrasados = {titulo: dados for titulo, dados in biblioteca.items() if dados["dias"] > 7}
print("\n📚 Livros emprestados há mais de 7 dias:")
if atrasados:
    for titulo, dados in atrasados.items():
        print(f"- {titulo} ({dados['usuario']}, {dados['dias']} dias)")
else:
    print("Nenhum livro atrasado.")

livro = max(biblioteca, key=lambda x: biblioteca[x]["dias"])
dias = biblioteca[livro]["dias"]
usuario = biblioteca[livro]["usuario"]
print(f"\n📖 O livro emprestado há mais tempo é '{livro}' ({usuario}), com {dias} dias.")


usuarios = [dados["usuario"] for dados in biblioteca.values()]
print("\n👤 Usuários com livros emprestados:", ", ".join(usuarios))

media = sum(dados["dias"] for dados in biblioteca.values()) / len(biblioteca)
print(f"\n📊 Média de dias de empréstimo: {media:.2f}")
