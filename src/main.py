import flet as ft
from views import home, videoplayer
import asyncio


async def main(page: ft.Page):
    page.fonts = {"VCROCDFaux": "VCROCDFaux.ttf"}

    async def route_change():
        page.views.clear()
        page.views.append(home(adaptive=True, page=page))
        if page.route == "/videoplayer":
            page.views.append(await videoplayer(adaptive=True, page=page))

        page.update()

    async def view_pop(e: ft.ViewPopEvent):
        if e.view is not None:
            print("View pop:", e.route)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(str(top_view.route))

    page.on_view_pop = view_pop
    page.on_route_change = route_change
    await route_change()


ft.run(main)
