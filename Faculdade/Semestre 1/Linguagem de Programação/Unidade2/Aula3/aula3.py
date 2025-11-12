# CLASSES E MÉTODOS EM PYTHON

# Python é uma linguagem de programação orientada a objetos
# Uma linguagem de programação é orientada a objetos quando incorpora os princípios de abstração e suporta o uso de encapsulamento, herança e polimorfismo
# Abstração -> capacidade de representar conceitos do mundo real em código / são os dados que representam o estado do objeto, como nome e idade.
# Encapsulamento -> capacidade de esconder detalhes internos e expor apenas o necessário / combina atributos e métodos em uma entidade, permitindo controlar o acesso a atributos por meio de métodos.
# Herança -> capacidade de criar novas classes com base em classes existentes / permite que uma classe herde atributos e métodos de outra, promovendo a reutilização de código.
# Polimorfismo -> capacidade de usar uma interface comum para diferentes tipos de dados / permite que diferentes classes implementem métodos com o mesmo nome, mas com comportamentos diferentes.

# Uma classe atua como um modelo para um objeto.
# A classe organiza os dados e comportamentos que os objetos de uma classe específica terão.

# Exemplo de classe:
'''
Classe: Pessoa
Atributos (dados):
Nome:
Idade:
Gênero:
Métodos (comportamentos):
Cumprimentar: saúda como “Olá, meu nome é”.
Aniversário: aumenta a idade em 1.

Objeto 1: Pessoa1
Atributos (dados):
Nome: João
Idade: 30
Gênero: Masculino
Métodos (comportamentos):
Cumprimentar: saúda como “Olá, meu nome é João”.
Aniversário: aumenta a idade em 1.
'''

# Nesse exemplo, a classe “Pessoa” define os atributos (nome, idade, gênero) e métodos (cumprimentar, aniversário) que o objeto “Pessoa1” pode usar.
# Cada objeto tem seus próprios atributos, mas compartilha os mesmos métodos da classe.
# A criação de uma classe em Python é feita com a palavra-chave class, seguida do nome da classe e dois pontos.
# Por convenção, o nome da classe começa com letra maiúscula e usa a notação CamelCase (sem espaços, cada palavra começa com letra maiúscula).

# Define uma classe chamada Pessoa
class Pessoa:
    # Método construtor (__init__) -> inicializa os atributos do objeto
    def __init__(self, nome, idade, genero):
# Self -> referência ao próprio objeto
# Os parâmetros nome, idade e genero são passados quando um objeto é criado
# Eles são usados para inicializar os atributos da instância.
        self.nome = nome # Atribui o valor do parâmetro nome ao atributo nome do objeto
        self.idade = idade # Atribui o valor do parâmetro idade ao atributo idade do objeto
        self.genero = genero # Atribui o valor do parâmetro genero ao atributo genero do objeto
# O método cumprimentar retorna uma saudação personalizada usando o nome do objeto
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."
# O método aniversario incrementa a idade do objeto em 1
    def aniversario(self):
        self.idade += 1

# Cria uma instância da classe Pessoa com os valores "João", 30 e "Masculino" para os atributos nome, idade e genero, respectivamente
pessoa1 = Pessoa("João", 30, "Masculino")
# Chama o método cumprimentar do objeto pessoa1 e imprime a saudação
print(pessoa1.cumprimentar()) # Saída: Olá, meu nome é João.
# Acessa o atributo idade do objeto pessoa1 e imprime o valor
print(f"Idade: {pessoa1.idade}") # Saída: Idade: 30
# Chama o método aniversario do objeto pessoa1, que incrementa a idade em 1
pessoa1.aniversario()
# Acessa novamente o atributo idade do objeto pessoa1 e imprime o novo valor
print(f"Nova idade: {pessoa1.idade}") # Saída: Nova idade: 31

# --------------------------------------------------------------------------

# HERANÇA EM PYTHON
# A herança permite que uma classe (classe filha ou subclasse) herde atributos e métodos de outra classe (classe pai ou superclasse)
# Isso promove a reutilização de código e a criação de hierarquias de classes
# A classe filha pode adicionar novos atributos e métodos ou sobrescrever os existentes da classe pai
# A herança é definida colocando o nome da classe pai entre parênteses após o nome da classe filha

# Exemplo de herança:
'''
class ClasseFilha(ClassePai):
# Definição da classe-filha

class ClasseFilha(ClassePai1, ClassePai2, ClassePai3):
# Definição da classe-filha
'''

# Benefícios da herança:
# Reutilização de código: a herança permite que você reutilize o código existente, aproveitando a estrutura e a funcionalidade de classes-pai em suas subclasses.
# Extensibilidade: você pode estender ou adicionar comportamentos específicos às classes-filhas sem modificar as classes-pai, mantendo a coesão e a organização do código.
# Hierarquia de classes: é possível criar uma hierarquia de classes na qual classes-filhas podem herdar características comuns de classes-pai e, por sua vez, serem herdadas por outras classes.

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_barulho(self):
        pass # Método abstrato, deve ser implementado pelas subclasses

class Cachorro(Animal): # Classe Cachorro herda da classe Animal
    def fazer_barulho(self): # Sobrescreve o método fazer_barulho da classe pai
        return "Au Au!"
    
class Gato(Animal): # Classe Gato herda da classe Animal
    def fazer_barulho(self): # Sobrescreve o método fazer_barulho da classe pai
        return "Miau!"
    
# Criando objetos das classes-filhas
cachorro = Cachorro("Rex")
gato = Gato("Whiskers")

# Chamando o método fazer_barulho de cada objeto
print(f"{cachorro.nome} faz: {cachorro.fazer_barulho()}") # Saída: Rex faz: Au Au!
print(f"{gato.nome} faz: {gato.fazer_barulho()}") # Saída: Whiskers faz: Miau!