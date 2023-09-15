import flet as ft
from datetime import datetime
import re


def main(page: ft.Page):

    #Definição dos parâmetros da janela
    page.title = 'Estacionamento do Seu Zé'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_maximized = True
    # TODO: testar outros temas

    #Função que define a lógica de novo registo (entrada)
    def inserir_registro(e: ft.KeyboardEvent):
        if carro.value:
            padrao_placa = re.compile(r'^[A-Z]{3}-?\d{4}$')
            # TODO: incluir o padrão mercosul

            if not padrao_placa.match(placa.value):
                placa.error_text = 'Não é uma placa válida.'
                placa.value = ''
                page.update()
                #TODO: corrigir a persistência do error_text 
            else:
                def encerrar_registro(e):

                    for linha in _tabela.rows:
                        if e.control.uid == linha.cells[-1].content.uid:
                            linha.cells[3].content.value = datetime.now().strftime(r'%H:%M:%S')
                            delta = datetime.strptime(linha.cells[3].content.value, r'%H:%M:%S') - \
                                datetime.strptime(linha.cells[2].content.value, r'%H:%M:%S')
                            linha.cells[4].content.value = delta
                            page.update()

                        #TODO: definir a regra de preços
                    # def price_rule(dur = linha.cells[3].content.value):
                    #     pass
                    #
                    # linha.cells[4].content.value = price_rule()

                    e.control.disabled = True
                    page.update()

                _tabela.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    value=carro.value
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value=placa.value
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value=f"{datetime.now().strftime(r'%H:%M:%S')}")
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value="Aguardando saída",
                                    italic=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value="Aguardando saída",
                                    italic=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value="Aguardando saída",
                                    italic=True
                                )
                            ),
                            ft.DataCell(
                                content=ft.ElevatedButton(
                                        text='Encerrar',
                                        on_click=encerrar_registro,
                                    )
                            )
                        ]
                    )
                )
                carro.value = ''
                placa.value = ''
                page.update()

        else:
            padrao_placa = re.compile(r'^[A-Z]{3}-?\d{4}$')
            if not padrao_placa.match(placa.value):
                placa.error_text = 'Não é uma placa válida. \nSelecione uma marca de carro.'
                placa.value = ''
                page.update()

    carro = ft.Dropdown(
        width=400,
        label='Carro',
        autofocus=True,
        hint_text='Escolha uma das opções',
        options=[
            ft.dropdown.Option("GOL"),
            ft.dropdown.Option("FIAT"),
            ft.dropdown.Option("VOLKSWAGEN"),
            ft.dropdown.Option("CITROEN"),
            ft.dropdown.Option("RENAULT"),
            ft.dropdown.Option("PEUGEOT"),
            ft.dropdown.Option("HONDA"),
            ft.dropdown.Option("HYUNDAI")
        ]
    )

    placa = ft.TextField(
        width=400,
        max_length=7,
        label='Placa',
        autofocus=True,
        text_size=20,
        expand=False,
        capitalization=ft.TextCapitalization.CHARACTERS
    )

    add_btn = ft.ElevatedButton(
        width=400,
        content=ft.Row(
            controls=[
                ft.Icon(
                    ft.icons.ADD
                ),
                ft.Text(
                    text_align=ft.TextAlign.CENTER,
                    value="Adicionar"
                )
            ]
        ),
        on_click=inserir_registro
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[carro]),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[placa]),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[add_btn]
        )
    )
    _tabela = ft.DataTable(
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        # column_spacing=223,
        width=1200,
        columns=[
            ft.DataColumn(label=ft.Text("Carro")),
            ft.DataColumn(label=ft.Text("Placa")),
            ft.DataColumn(ft.Text("Entrada")),
            ft.DataColumn(ft.Text("Saída")),
            ft.DataColumn(ft.Text("Duração")),
            ft.DataColumn(ft.Text("Total a Pagar")),
            ft.DataColumn(
                ft.Text(
                    text_align=ft.TextAlign.CENTER,
                    # width=100,
                    value="Check"
                )
            )
        ],
    )
    page.controls.append(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[_tabela]
        )
    )

    page.scroll = 'always'
    page.update()


ft.app(target=main)
