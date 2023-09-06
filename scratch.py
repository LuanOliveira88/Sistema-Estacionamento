import flet as ft
from random import randint


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_maximized = True

    def adicionar_linha(e):
        def clicou(e):
            num1, num2, soma, produto = botao_clique.data
            num1 = int(num1)
            num2 = int(num2)
            soma = num1 + num2
            produto = num1 * num2
            botao_clique.disabled = True
            page.update()

        tabela.rows.append(
            (dr := ft.DataRow(
                # ref=ft.Ref(),
                # on_select_changed=func,
                cells=[
                    ft.DataCell((a := ft.Text(value=str(randint(1, 10))))),
                    ft.DataCell((b := ft.Text(value=str(randint(1, 10))))),
                    ft.DataCell((c := ft.Text(value='Aguardando...', italic=True))),
                    ft.DataCell((d := ft.Text(value='Aguardando...', italic=True))),
                    ft.DataCell((botao_clique := ft.FloatingActionButton(
                        key='abc',
                        data=[a.value, b.value, c.value, d.value],
                        scale=0.6,
                        icon=ft.icons.CHECK,
                        on_click=clicou)
                    )),
                ]
            )
        ))
        page.update()

    tabela = ft.DataTable(
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        # column_spacing=223,
        width=1406,
        columns=[
            ft.DataColumn(label=ft.Text(value='Número 1')),
            ft.DataColumn(label=ft.Text(value='Número 2')),
            ft.DataColumn(label=ft.Text(value='Soma')),
            ft.DataColumn(label=ft.Text(value='Produto')),
            ft.DataColumn(label=ft.Text(value='Button'))
        ]
    )

    botao = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=adicionar_linha)

    page.add(
        tabela,
        botao
    )
    page.add()
    page.scroll = 'always'


ft.app(target=main)
