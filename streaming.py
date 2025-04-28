class Filme:
 def __init__(self, nome, ano, duracao, genero, imdb):
    self.__nome = nome.title()
    self.__ano = ano
    self.__duracao = duracao
    self.__genero = genero 
    self.__imdb = imdb
    self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome

    @property
    def genero(self):
       return self.__genero

    @genero.setter
    def genero(self, genero):
       self.__genero = genero

    @property
    def imdb(self):
       return self.__imdb

    @imdb.setter
    def imdb(self, imdb):
        self.__imdb = imdb

    @nome.setter
    def nome(self, nome):
      self.__nome = nome

class Serie:
    def __init__(self, nome, ano, temporadas, genero, imdb):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__genero = genero
        self.__imdb = imdb
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def dar__like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def temporadas(self):
        return self.__temporadas
    
    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas

    @property
    def imdb(self):
        return self.__imdb
    
    @imdb.setter
    def imdb(self, imdb):
        self.__imdb = imdb

    @nome.setter
    def nome(self, nome):
        self.__nome = nome