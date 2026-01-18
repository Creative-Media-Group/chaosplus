import flet as ft
from localisations import *
from components import mystack, mybutton
import asyncio
from flet_localisation import locale


def new():
    pass


def home(adaptive: bool, page: ft.Page):
    trfile = os.path.join(
        os.path.dirname(__file__), "../localisations/localisation.csv"
    )
    myplatfom = str(page.platform)
    mylocale = str(locale(platform=myplatfom)).split("_")
    langcode = mylocale[0]
    region = mylocale[1]
    tr = TR(csv_file=trfile, langcode=langcode)
    return ft.View(
        route="/",
        adaptive=adaptive,
        appbar=ft.AppBar(
            bgcolor=ft.Colors.TRANSPARENT,
            title=ft.Text("Chaos+", rtl=tr.check_rtl()),
            center_title=True,
            leading=ft.Image(src="icon.png", width=40, height=40),
            rtl=tr.check_rtl(),
        ),
        # auto_scroll=True,
        padding=0,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.SafeArea(
                ft.Column(
                    rtl=tr.check_rtl(),
                    controls=[
                        ft.Text("Hello", size=40, rtl=tr.check_rtl()),
                        ft.Row(
                            rtl=tr.check_rtl(),
                            controls=[
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda e: asyncio.create_task(
                                        page.push_route("/mediainfo")
                                    ),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        ft.Text("Hello", size=40),
                        ft.Row(
                            rtl=tr.check_rtl(),
                            controls=[
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda e: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda e: new(),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        ft.Text("Hello", size=40, rtl=tr.check_rtl()),
                        ft.Row(
                            rtl=tr.check_rtl(),
                            controls=[
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda e: new(),
                                ),
                                mybutton(
                                    img_src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png",
                                    text=HELLOMSG(page),
                                    on_click=lambda e: new(),
                                ),
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                    ],
                )
            )
        ],
    )
