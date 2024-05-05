from ScrapingSystem import ScrapingSystem

class AthleteListGeneratingSystem:
    def __init__(self):
        self.athlete_categories = ["agegroup=0"]
        self.gender_list = ["gender=1", "gender=2"]
        self.pool_length = ["course=LCM", "course=SCM"]
        self.url_prefix = "https://www.swimrankings.net/index.php"

    def get_url(self, club_url):
        my_dict = {}
        url_prefix = "https://www.swimrankings.net/index.php"
        for j in self.gender_list:
            club_url_gender = str(club_url).replace("gender=1", j)
            for k in self.pool_length:
                club_url_course = str(club_url_gender).replace("course=SCM", k)
                links = ScrapingSystem.Loader(club_url_course).select("td.swimstyle a")
                for link in links:
                    distance_link = url_prefix + link.get("href")
                    print(distance_link)
                    my_dict.update(self.process_distance(distance_link))
        for key, value in my_dict.items():
            print(f"Key: {key} Value: {value}")

    def process_distance(self, distance_link):
        my_dict = {}
        scraping_system = ScrapingSystem.Loader(distance_link)
        number = self.get_places(scraping_system)
        times = (number // 25) + 1
        xd = number
        tab = [min(xd, 25)] * (xd // 25)
        remainder = xd % 25
        xd -= min(xd, 25) * (xd // 25)
        print(times)
        if remainder:
            tab.append(remainder)
        for i in range(times):
            print(i)
            if i == 0:
                print(distance_link)
                my_dict.update(self.get_fullnames(distance_link))
            else:
                distance_link = distance_link.replace(f"firstPlace=1", f"firstPlace={(25*times)+1}")
                print(distance_link)
                my_dict.update(self.get_fullnames(distance_link))
        return my_dict




    def get_places(self, scraping_system):
        places = scraping_system.find_all("td", class_="navigation")
        place_text = places[9].text if len(places) > 9 else ""
        place_number = int(place_text.split()[-1]) if place_text else 0
        print(place_number)
        return place_number

    def get_fullnames(self, distance_link):
        my_dict = {}
        td_fullname = ScrapingSystem.Loader(distance_link).find_all("td", class_="fullname")
        for i in td_fullname:
            if i:
                a_tags = i.find_all("a")
                for a_tag in a_tags:
                    href = a_tag.get('href')
                    inner_text = a_tag.text
                    if inner_text not in my_dict:
                        my_dict[inner_text] = self.url_prefix + href

        return my_dict

