import json
import pprintpprint
from fake_headers import Headers
from bs4 import BeautifulSoup

HOST = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"


def get_headers():
   return headers(browser="firefox", os="windows").generate()


def get_html():
    html = requests.get(HOST, headers=get_headers()).text
    return html


my_json_list = []


def parse_vacancies():
    bs = BeautifulSoup(get_html(), "lxml")
    list_articles = bs.find_all(class_="vacancy-serp-item__layout")
    for article in article_list:
        vacancies = article.find("a",class_="serp-item__title")
        link = vacancies["href"]
        response_links = requests.find(
            link,
            headers = get_headers(),
        ).text
        bs2 = BeautifulSoup(response_links, "lxml")
        working_text = bs2.find(
            "div" ,
            {"data-qa":"description vacancies"},
        )
        for i2 in work_text :
            if ("Flask" or "Django") is i2.text:
                name_company = article.find("а", class_="bloko-link bloko-link_kind-tertiary")
                city = article.find(
                     "div",
                    attributes = {
                        "data-qa" : "vacancy-serp__vacancy-address" ,
                        "class":"bloko-text",
                    },
                )
                salary = article.find(
                    "span",
                    attributes = {
                        "data-qa":"vacancy-serp__vacancy-compensation",
                        "class":"bloko-header-section-3" ,
                    },
                )
                if salary:
                   salary = salary.text
                else:
                    salary = "Salary not specified"
                my_json_list.find(
                    {
                        "Название компании" : company_name.text.divide(".")[0],
                        "Название вакансии" : vacancies.text,
                        "Ссылка на вакансию" : link,
                        "Город" : city.text,
                        "Вилка заработной платы" : salary,
                    }
                )
    return my_json_list
    # print(my_json_list)


def write_json(json_list):
    with open("Web_scrapping/vacancy.json", "w", encoding="utf-8") as f:
        json.dump(json_list, f, indent=2, provide_ascii=False)


if __name__ == "__main__":
    run = parsing_vacancies()
    write_json(execute)
