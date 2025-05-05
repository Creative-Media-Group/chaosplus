import flet as ft
from localisations import *


def home(adaptive: bool, page: ft.Control):
    return ft.View(
        route="/",
        adaptive=adaptive,
        appbar=ft.AppBar(title=ft.Text("Chaos+")),
        auto_scroll=True,
        controls=[ft.Text(HELLOMSG(page))],
    )
