import pyfiglet
from os import system
from simple_chalk import chalk
from webScraper import WebScraper

# onStartUp
system("cls")
print("\n")

# Logo
rawLogo = pyfiglet.figlet_format("Web")
rawSideLogo = pyfiglet.figlet_format("Scraping")
logo = chalk.blue.bold(rawLogo)
sideLogo = chalk.green.bold(rawSideLogo)

# output
print(logo + "\n" + sideLogo)
print("Web Scraping - version - 1 , Made By Junaid.", "\n")
print("-" * 50)
print("Starting Web Scraping ...")
print("\n⬇⬇⬇ Logs of Web Scraping ,press 'Ctrl + C' to stop Web Scraping ⬇⬇⬇")
print("-" * 70, "\n")
# --------------------------------------------

WebScraper()

print("\n", "-" * 50, "\n")
a = input("You want to see Web Scrapped data (y / n) : ")
print("\n", "-" * 50, "\n")

if a == "y":
    print("-" * 80, "\n")
    print(WebScraper.showData())
    print("\n", "-" * 80, "\n")
else:
    print(chalk.red("Incorrect Input Value !"))
    exit(0)

print(
    chalk.blue.bold("Web"), chalk.green.bold("Scraping"), ", Version - 1|June 2022 .\n"
)
print(chalk.black.bgWhite("-> Made By Junaid <-"))
