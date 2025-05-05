import flet as ft


def home(adaptive):
    return ft.View(
        route="/",
        adaptive=adaptive,
        appbar=ft.AppBar(title=ft.Text("Chaos+")),
        auto_scroll=True,
        controls=[],
    )
