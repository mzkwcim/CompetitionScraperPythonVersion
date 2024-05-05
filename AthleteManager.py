from selenium import webdriver
from selenium.webdriver.common.by import By
from ScrapingSystem import ScrapingSystem
import re
from ListManager import AthleteListGeneratingSystem as ALGS


class ClubUrlGettingSystem:
    def GetClubName(self, inserted_club_name):
        driver = webdriver.Chrome()

        # Przejście do strony
        driver.get("https://www.swimrankings.net/index.php?page=clubSelect")

        # Wyszukiwanie elementu klubu
        club_name = driver.find_element(By.XPATH, "//*[@id=\"club_name\"]")
        club_name.send_keys(inserted_club_name)

        # Ustawienie czasu oczekiwania na 10 sekund
        driver.implicitly_wait(10)

        # Wyszukiwanie elementów klubów
        elements = driver.find_elements(By.XPATH,
                                        f"//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), translate('{inserted_club_name}', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'))]")

        url = ""
        if len(elements) > 0:
            url = elements[0].get_attribute("href")
            driver.quit()
        else:
            print("Nie znaleziono elementów na stronie.")
            driver.quit()
            return None

        if url is None:
            print("Program zostanie zakończony")
            return None
        else:
            first = ScrapingSystem.Loader(url).select_one("td a")
            url_prefix = "https://www.swimrankings.net/index.php?page=rankingDetail&clubId="
            club_id = re.sub(r'^.+clubId=|&.+', "", first.get("href"))
            url_suffix = "&gender=1&course=SCM&agegroup=0"
            new_url = f"{url_prefix}{club_id}{url_suffix}"
            print(new_url)
            list_manager = ALGS()
            list_manager.get_url(new_url)
            return new_url
