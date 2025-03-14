from rich import print
from rich.console import Console
from rich.text import Text
from rich.theme import Theme

def display_banner():
    custom_theme = Theme({
        "link": "dark_orange3"
    })
    console1 = Console(theme=custom_theme)
    console = Console()

    banner = """
              __ _     _ ___   _  _ _   ___  _  _____ ___ __
             / __\ \ / /| __| | || | | | | \| ||_   _| __| _ \  
            | (__ \ V / | _|  | __ | |_| | .` |  | | | _||   /  
             \___| \_/  |___| |_||_|\___/|_|\_|  |_| |___|_|_\        
                                           """
    
    banner3 = "[+] Developed by RedStrike0"


    banner_text1 = Text(banner, style="orange3")
   # banner_text2 = Text(banner4, style="red3")
    banner_text3 = Text(banner3, style="dark_orange3")


    centered_text1 = "{:^60}".format(banner_text1.plain)
    #centered_text2 = "{:^60}".format(banner_text2.plain)
    centered_text3 = "{:^70}".format(banner_text3.plain)


    console.print(Text(centered_text1, style="red1"))
    #console.print(Text(centered_text2, style="red1"))
    console1.print(Text(centered_text3, style="dark_orange3"))

