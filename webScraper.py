from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from time import sleep


class WebScraper:
    def __init__(self):
        print(
            "\nGetting Data -> https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
        )
        print("Website Domain -> Wikipedia.org")

        sleep(0.2)

        bright_stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

        page = requests.get(bright_stars_url)
        print("\nResponse form page ->", page)

        sleep(0.3)

        print("\nFinding table tag (Which contains data) ...")
        soup = bs(page.text, "html.parser")
        star_table = soup.find("table")

        sleep(0.5)

        print("\nExtracting Data ...")
        temp_list = []
        table_rows = star_table.find_all("tr")
        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

        sleep(0.3)

        print("\nSaving Data ...")
        Star_names = []
        Distance = []
        Mass = []
        Radius = []
        Lum = []

        for i in range(1, len(temp_list)):
            Star_names.append(temp_list[i][1])
            Distance.append(temp_list[i][3])
            Mass.append(temp_list[i][5])
            Radius.append(temp_list[i][6])
            Lum.append(temp_list[i][7])

        sleep(0.3)

        file = "bright_stars.csv"
        print("\nSaving data as ->", file)
        df2 = pd.DataFrame(
            list(zip(Star_names, Distance, Mass, Radius, Lum)),
            columns=["Star_name", "Distance", "Mass", "Radius", "Luminosity"],
        )
        df2.to_csv(file)

    def showData():
        df = pd.read_csv("bright_stars.csv")
        return df
