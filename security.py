from argon2 import PasswordHasher


senha_hash = PasswordHasher()

def gerar_hash(inserir_senha):
    hash = senha_hash.hash(inserir_senha)
    return hash


def verificar_hash(inserir_senha, hash_salvo):
    senha = senha_hash.verify(hash_salvo, inserir_senha)
    return senha