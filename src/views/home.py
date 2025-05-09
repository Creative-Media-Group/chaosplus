import flet as ft
from localisations import *
from components import mystack, mybutton


def new():
    pass


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
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        ft.Text("Hello", size=40),
                        ft.Row(
                            controls=[
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        ft.Text("Hello", size=40),
                        ft.Row(
                            controls=[
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda _: new(),
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
