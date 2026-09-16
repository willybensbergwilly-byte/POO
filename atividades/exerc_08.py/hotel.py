from models.avaliacoes import Avaliacao

class Hotel:
    def __init__(self, nome_hotel, cidade):
        self.nome_hotel = nome_hotel
        self.cidade = cidade
        self._avaliacoes = []
         
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        
        else:
            total_avaliacoes = sum(avaliacao.nota for avaliacao in self._avaliacoes)
            quantidade_avaliacoes = len(self._avaliacoes)
            return total_avaliacoes / quantidade_avaliacoes
            media = round(total_avaliacoes/quantidade_avaliacoes, 1)
            return media