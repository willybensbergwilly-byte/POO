# Toda vez que voces fizerem uma função para teste, ela deve conter o test_
import pytest
from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida


def test_media_avaliacao_calcula_corretamente():
    
    # Cria um restaurante de teste
    restaurante = Restaurante('Coco Bambu', 'Frutos do Mar', 'Av. Paulista, 1000', 10) 
    restaurante.receber_avaliacoes("Não é o Heron", 5.0)  # Recebe algumas avaliações de teste
    restaurante.receber_avaliacoes("Paulo", 5.0)
    assert restaurante.media_avaliacoes == 5.0  # Verifica se a média está correta
    
def test_adicionar_item_invalido_lanca_erro():
    restaurante = Restaurante('Coco Bambu', 'Frutos do Mar', 'Av. Paulista, 1000', 10)
    with pytest.raises(ValueError):
        restaurante.adicionar_cardapio('Isso não é item de cardápio')

def test_confirmar_avaliacao():
    avaliacao = Avaliacoes("Ana", 5.0)
    assert avaliacao._cliente == "Ana" 
    assert avaliacao._nota == 5.0