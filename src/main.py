import flet as ft
from views import home


def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home(adaptive=True, page=page))
        elif page.route == "/portfolio":
            page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/portfolio",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                [
                                    ft.Text("Portfolio"),
                                    mybutton(
                                        text=FLASHLIGHTMSG(page=page),
                                        on_click=lambda _: page.go("/flashlight"),
                                        disabled=is_mobile(platform),
                                        width=page.width * 0.5,
                                    ),
                                    mybutton(
                                        text="Zurück",
                                        on_click=lambda _: page.go("/"),
                                        disabled=False,
                                        width=page.width * 0.5,
                                    ),
                                ],
                            )
                        )
                    ],
                )
            )

        page.update()


ft.app(main)
