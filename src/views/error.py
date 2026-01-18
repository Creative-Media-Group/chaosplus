import flet as ft
from localisations import *
from components import mystack, mybutton


def error(adaptive: bool, page: ft.Page, text: str):
    trfile = os.path.join(
        os.path.dirname(__file__), "../localisations/localisation.csv"
    )
    myplatfom = str(page.platform)
    mylocale = str(locale(platform=myplatfom)).split("_")
    langcode = mylocale[0]
    region = mylocale[1]
    tr = TR(csv_file=trfile, langcode=langcode)
    return ft.View(route="/", controls=[ft.Text(text)])
