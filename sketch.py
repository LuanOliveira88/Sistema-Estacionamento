import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(
            controls=[
                ft.Text(
                    value='Hello, Luan'
                )
            ]
        )
    )

    page.update()

ft.app(target=main)