import flet as ft
from datetime import datetime
import re


def main(page: ft.Page):

    page.title = 'Estacionamento do Seu Zé'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_maximized = True

    def inserir_registro(e):
        if carro.value:

            padrao_placa = re.compile(r'^[A-Z]{3}-?\d{4}$')
            # TODO: incluir o padrão mercosul
            if not padrao_placa.match(placa.value):
                placa.error_text = 'Não é uma placa válida.'
                placa.value = ''
                page.update()
            else:
                def encerrar_registro(e):

                    b.data[3] = datetime.now().strftime(r'%H:%M:%S')
                    b.data[4] = f"R$ {4.00 * (datetime.strptime(b.data[3], r'%H:%M:%S') - datetime.strptime(b.data[2], r'%H:%M:%S')).seconds:.2f}"
                    b.disabled = True
                    # _tabela.build_update_commands()
                    page.update()

                _tabela.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Text(
                                    value=(carro_valor := carro.value)
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value=(placa_valor := placa.value)
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value=f"{(t_entrada := datetime.now().strftime(r'%H:%M:%S'))}")
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value=(t_saida := "Aguardando saída"),
                                    italic=True
                                )
                            ),
                            ft.DataCell(
                                ft.Text(
                                    value=(valor_pagar := "Aguardando saída"),
                                    italic=True
                                )
                            ),
                            ft.DataCell(
                                content=(
                                    b := ft.ElevatedButton(
                                        width=110,
                                        text='Encerrar',
                                        on_click=encerrar_registro,
                                        data=[
                                            carro_valor,
                                            placa_valor,
                                            t_entrada,
                                            t_saida,
                                            valor_pagar
                                        ]
                                    )
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
        width=(wdth := 400),
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
        ])

    placa = ft.TextField(
        width=wdth,
        max_length=7,
        label='Placa',
        autofocus=True,
        # helper_text='Digite a placa no carro no formato XXXXXXX',
        # border=ft.InputBorder.UNDERLINE,
        text_size=20,
        expand=False,
        capitalization=ft.TextCapitalization.CHARACTERS
    )

    add_btn = ft.ElevatedButton(
        width=wdth,
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
            width=800,
            bgcolor="YELLOW",
            horizontal_lines=ft.border.BorderSide(0.5, "Gray"),
            vertical_lines=ft.border.BorderSide(0.5, "Gray"),
            columns=[
                ft.DataColumn(label=ft.Text("Carro")),
                ft.DataColumn(label=ft.Text("Placa")),
                ft.DataColumn(ft.Text("Entrada")),
                ft.DataColumn(ft.Text("Saída")),
                ft.DataColumn(ft.Text("Total a Pagar")),
                ft.DataColumn(
                    ft.Text(
                        text_align=ft.TextAlign.CENTER,
                        width=100,
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
