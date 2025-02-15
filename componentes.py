#importar a biblioteca flet
import flet as ft

#definir a função main
def main(page: ft.Page):
    #define uma tela/uma interface vazia
    # pass

    # enviar um texto para a interface
    # armazenar o texto em uma variável
    texto: ft.texto = ft.Text(value='Técnico em Informática')
    #enviar o conteudo para a tela
    page.add(texto)
    # fim da função main
ft.app(target=main)