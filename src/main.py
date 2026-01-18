import flet as ft
from views import home, videoplayer, mediainfo


def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home(adaptive=True, page=page))
        elif page.route == "/mediainfo":
            page.views.append(mediainfo(adaptive=True, page=page))
        elif page.route == "/videoplayer":
            page.views.append(videoplayer(adaptive=True, page=page))

        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.run(main)
