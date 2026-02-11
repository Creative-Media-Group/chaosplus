import flet as ft
from localisations import *
from components import mystack, mybutton
import asyncio
import os

img = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png"


async def mediainfo(adaptive: bool, page: ft.Page):
    trfile = os.path.join(
        os.path.dirname(__file__), "../localisations/localisation.csv"
    )
    myplatfom = str(page.platform)
    mylocale = str(locale(platform=myplatfom)).split("_")
    langcode = mylocale[0]
    region = mylocale[1]
    tr = TR(csv_file=trfile, langcode=langcode)
    return ft.View(
        scroll=ft.ScrollMode.AUTO,
        route="/mediainfo",
        # adaptive=adaptive,
        floating_action_button=ft.FloatingActionButton(
            icon=ft.Icons.PLAY_ARROW,
            on_click=lambda e: asyncio.create_task(page.push_route("/videoplayer")),
        ),
        controls=[ft.SafeArea(ft.Image(img))],
    )
