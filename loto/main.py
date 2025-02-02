import requests
from scrapper import ScrapperManager
import pandas as pd

START_YEAR = 1993
END_YEAR = 2024

scrapper = ScrapperManager(start_year=START_YEAR, end_year=END_YEAR)


def create_archive():
    for year in range(START_YEAR, END_YEAR):
        archive = pd.DataFrame(scrapper.get_archive(year))
        print(archive)
        try:
            with pd.ExcelWriter("archive.xlsx", mode="a") as writer:
                archive.to_excel(writer, sheet_name=f"{year}")
        except FileNotFoundError:
            with pd.ExcelWriter("archive.xlsx", mode="w") as writer:
                archive.to_excel(writer, sheet_name=f"{year}")


create_archive()
