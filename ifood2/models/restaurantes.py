from ifood2.models.avaliacoes import Avaliacoes
from ifood2.models.cardapio.itemcardapio import ItemCardapio    
from ifood2.models.avaliacoes import Avaliacoes

class Restaurante:
    restaurantes = []
    avaliacoes = []
    
    def __init__(self, nome, localizacao, tipo_de_comida, quantidade_funcionarios):
            self.nome_restaurante = nome
            self.localizacao = localizacao
            self.tipo_de_comida = tipo_de_comida
            self.quantidade_funcionarios = quantidade_funcionarios
            self._status = False
            self._avaliacoes = []
            self._cardapio = []
            Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome_restaurante}\n - Rua: {self.localizacao}\n Tipo de Comida: {self.tipo_de_comida}\n - Quantidade de Funcionários: {str(self.quantidade_funcionarios)}"
    
    
    @classmethod
    
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f"Nome: {restaurante.nome_restaurante} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.tipo_de_comida} \n|Avaliações:{restaurante.media_avaliacoes} \n|Quantidade de Funcionários: {str(restaurante.quantidade_funcionarios)} \n|Status: {restaurante.ativo}")

    @property
    def ativo(self):
        return 'ativo' if self._status else 'inativo'

    @property
    def media_avaliacoes(self):
        if not self.avaliacoes:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(notas_somadas/quantidade_avaliacoes, 1) 
        return media
    
    @property
    def exibir_cardapio(self):
            print(f"Cardapio do Restaurante{self.nome_restaurante}:")
            
            for i,item in enumerate(self._cardapio, start=1):
                if hasattr(item, 'descricao'):
                    mensagem_prato = f"{i}. Nome: {item._nome} |  preço: {item._preco} |  Descrição: {item.descricao}"
                    print(mensagem_prato)
                
                elif hasattr(item, 'sabor'):
                    mensagem_sobremesa = f"{i}. Nome: {item._nome} | preço: {item._preco} | sabor: {item.sabor}"
                    print(mensagem_sobremesa)
                
                else:
                    
                    mensagem_bebida = f"{i}. Nome: {item._nome} | preço: {item._preco} | tamanho: {item.tamanho}"
                    print(mensagem_bebida)
                    
    def alterar_estado(self):
        self._status = not self._status     
        
    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)
        
    def adicionar_cardapio(self, item):
            if isinstance(item, ItemCardapio):
                self._cardapio.append(item)
            
            