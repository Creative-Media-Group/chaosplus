import flet as ft
from localisations import *
from components import mystack, mybutton


def home(adaptive: bool, page: ft.Control):
    return ft.View(
        route="/",
        adaptive=adaptive,
        appbar=ft.AppBar(
            title=ft.Text("Chaos+"),
            center_title=True,
            leading=ft.Image(src="icon.png", width=40, height=40),
        ),
        auto_scroll=True,
        controls=[
            ft.SafeArea(
                ft.Column(
                    controls=[
                        ft.Text("Hello", size=40),
                        ft.Row(
                            controls=[
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        ft.Text("Hello", size=40),
                        ft.Row(
                            controls=[
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        ft.Text("Hello", size=40),
                        ft.Row(
                            controls=[
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                                mybutton(
                                    img_src="https://picsum.photos/300/300",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: print("Hello"),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                    ],
                )
            )
        ],
        scroll=ft.ScrollMode.AUTO,
    )
