import flet as ft

img = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/2244px-Wikipedia-logo-v2.svg.png"


def mediainfo(adaptive: bool, page: ft.Control):
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
        adaptive=adaptive,
        controls=[ft.SafeArea()],
    )
