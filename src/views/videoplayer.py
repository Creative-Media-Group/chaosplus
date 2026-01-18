import flet as ft
import flet_video as ftv
import asyncio


def videoplayer(adaptive: bool, page: ft.Page):
    def myplatform():
        if page.platform.ANDROID or page.platform.ANDROID_TV:
            return ft.FilterQuality.LOW
        else:
            return ft.FilterQuality.HIGH

    def loaded(e):
        video.play()
        # page.window.full_screen = True
        page.update()

    url = "https://cdn.media.ccc.de/congress/2024/webm-hd/38c3-198-eng-deu-pol-BlinkenCity_Radio-Controlling_Street_Lamps_and_Power_Plants_webm-hd.webm"
    video_obj = [ftv.VideoMedia(url)]
    return ft.View(
        route="/videoplayer",
        adaptive=True,
        padding=0,
        controls=[
            video := ftv.Video(
                expand=True,
                playlist=video_obj[0],
                playlist_mode=ftv.PlaylistMode.LOOP,
                fill_color=ft.Colors.BLACK,
                aspect_ratio=16 / 9,
                volume=100,
                autoplay=True,
                filter_quality=myplatform,
                # configuration=ftv.VideoConfiguration(),
                muted=False,
                on_loaded=lambda e: loaded(e),
                on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
                on_exit_fullscreen=lambda e: print("Video exited fullscreen!"),
                on_completed=lambda e: asyncio.create_task(
                    page.push_route("/videoplayer")
                ),
            )
        ],
    )
