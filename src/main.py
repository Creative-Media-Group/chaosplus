import flet as ft
from views import home, videoplayer, mediainfo, error


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

    def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_view_pop = view_pop
    page.on_route_change = route_change
    page.go("/")


ft.run(main)
