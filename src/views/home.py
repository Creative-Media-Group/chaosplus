import flet as ft
from localisations import *
from components import mystack


def home(adaptive: bool, page: ft.Control):
    return ft.View(
        route="/",
        adaptive=adaptive,
        appbar=ft.AppBar(title=ft.Text("Chaos+"), center_title=True),
        auto_scroll=True,
        controls=[
            ft.SafeArea(
                mystack(img_src="https://picsum.photos/300/300", text=HELLOMSG(page))
            )
        ],
    )
