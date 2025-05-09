import flet as ft


def mystack(img_src: str, text: str, adaptive: bool = True):
    width = 160 * 2
    height = 90 * 2
    return ft.Stack(
        controls=[
            ft.Image(
                src=img_src.format(),
                width=width,
                height=height,
                fit=ft.ImageFit.FIT_WIDTH,
                border_radius=10,
            ),
            ft.Image(
                src=img_src.format(),
            ),
            ft.Row(
                controls=[
                    ft.Text(
                        value=text,
                        color=ft.Colors.ON_SURFACE,
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        opacity=0.8,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                adaptive=adaptive,
            ),
        ],
        adaptive=adaptive,
        alignment=ft.alignment.bottom_center,
        width=width,
        height=height,
    )


def mybutton(
    img_src: str, text: str, on_click, disabled: bool = False, adaptive: bool = True
):
    width = 160 * 2
    height = 90 * 2
    border_radius = 10
    return ft.OutlinedButton(
        content=ft.Stack(
            controls=[
                ft.Image(
                    src=img_src.format(),
                    width=width,
                    height=height,
                    fit=ft.ImageFit.FIT_WIDTH,
                    border_radius=border_radius,
                ),
                ft.Image(
                    src=img_src.format(),
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            value=text,
                            color=ft.Colors.ON_SURFACE,
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            # opacity=0.8,
                        )
                    ],
                    adaptive=adaptive,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.Alignment(x=0, y=1),
            width=width,
            height=height,
            adaptive=adaptive,
        ),
        adaptive=adaptive,
        on_click=on_click,
        width=width + 5,
        height=height + 15,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=border_radius)),
    )
