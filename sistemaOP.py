class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao
    
    def __str__(self):
        return f"Sistema Operacional: {self.nome} {self.versao}"

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema
    
    def __str__(self):
        return f"Computador contem {self.sistema}"

sistema_windows = SistemaOperacional("Windows", "11")
computador1 = Computador(sistema_windows)

sistema_linux = SistemaOperacional("Linux", "123.10")
computador2 = Computador(sistema_linux)

print(computador1)
print(computador2)