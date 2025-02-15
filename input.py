import flet as ft

def main(page: ft.Page):
    # variaveis
    titulo=ft.Text(value="CADASTRO DE CLIENTES", color="red", size=38)
    texto=ft.TextField(label="Nome")
    idade=ft.TextField(value='0')
    texto1=ft.Text(value="Digite seu nome")
    texto2=ft.Text(value="Digite sua idade")

    # função soma e sub
    def soma():
        idade.value = idade.value+1
    def sub():
        idade.value = idade.value-1
    

    # page style
    page.bgcolor=ft.colors.DEEP_PURPLE_700
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.title="Enganar otário KKKKKKKKKKKK"
    # add para a pagina
    page.update()
    page.add(titulo)
    page.add(texto1)
    page.add(texto)
    page.add(texto2)
    page.add(
        # adicionar uma linha para conter o controle
        ft.Row(
            # interligar os elementos
            controls=[
                # icon(-)
                ft.IconButton(icon=ft.icons.REMOVE),
                # campo de idade
                idade,
                # icon(+)
                ft.IconButton(icon=ft.icons.ADD),
            ]
        )
    )
ft.app(target=main)