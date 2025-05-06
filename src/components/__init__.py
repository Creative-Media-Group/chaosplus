import flet as ft


def mystack(img_src: str, text: str):
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
            ft.Row(
                [
                    ft.Text(
                        value=text,
                        color=ft.Colors.ON_SURFACE,
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        opacity=0.8,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.alignment.bottom_center,
        width=width,
        height=height,
    )
