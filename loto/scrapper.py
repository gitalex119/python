from bs4 import BeautifulSoup
import requests
import pandas as pd


class ScrapperManager:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
        self.archive_url = f""

    def get_archive(self, year):
        response = requests.get(f"{self.archive_url}{year}")

        web_content = response.text
        soup = BeautifulSoup(web_content, "html.parser")

        tables = soup.find_all(name="table", class_="bilet")
        results_table = tables[1]

        table_rows = results_table.find_all(name="tr")
        results = pd.DataFrame(columns=["Date", "Numbers"])
        for row in table_rows[len(table_rows):1:-1]:
            cols = row.find_all(name="td")
            ticket = []
            data = {}
            for col_number in range(1, 7):
                ticket.append(int(cols[col_number].getText()))
            data["Date"] = cols[0].getText()
            data["Numbers"] = [ticket]
            new_rows = pd.DataFrame(data)

            results = pd.concat([results, new_rows], ignore_index=True)
        return results
