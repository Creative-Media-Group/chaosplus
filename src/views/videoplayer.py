import flet as ft
import flet_video as ftv
import asyncio


def myplatform(page: ft.Page):
    if page.platform.ANDROID or page.platform.ANDROID_TV:
        return ft.FilterQuality.LOW
    else:
        return ft.FilterQuality.HIGH


async def videoplayer(adaptive: bool, page: ft.Page):
    async def loaded(e):
        await video.play()
        await page.update()

    url = "https://cdn.media.ccc.de/congress/2024/webm-hd/38c3-198-eng-deu-pol-BlinkenCity_Radio-Controlling_Street_Lamps_and_Power_Plants_webm-hd.webm"
    video_obj = [ftv.VideoMedia(url)]
    return ft.View(
        route="/videoplayer",
        # adaptive=adaptive,
        padding=0,
        controls=[
            video := ftv.Video(
                expand=True,
                fullscreen=True,
                playlist=video_obj[0],
                playlist_mode=ftv.PlaylistMode.LOOP,
                fill_color=ft.Colors.BLACK,
                aspect_ratio=16 / 9,
                volume=100,
                autoplay=True,
                filter_quality=myplatform(page=page),
                # configuration=ftv.VideoConfiguration(),
                muted=False,
                on_load=loaded,
                on_enter_fullscreen=lambda e: print("Video entered fullscreen!"),
                on_exit_fullscreen=lambda e: print("Video exited fullscreen!"),
                on_complete=lambda e: asyncio.create_task(
                    page.push_route("/videoplayer")
                ),
            )
        ],
    )
