импортировать  json
 запросы на импорт
импорт  pprintpprint
из  fake_headers  импортировать  заголовки
из  bs4  импортировать  BeautifulSoup

HOST  =  "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"


защита  get_headers ():
    вернуть  заголовки ( browser = "firefox" , os = "windows" ). генерировать ()


защита  get_html ():
    html  =  запросы . получить ( HOST , заголовки = get_headers ()). текст
    вернуть  html


мой_json_list  = []


деф  parse_вакансии ():
    bs  =  BeautifulSoup ( get_html (), "lxml" )
    список_статей  =  bs . find_all ( class_ = "vacancy-serp-item__layout" )
    для  я  в  article_list :
        вакансии  =  я . найти ( "a" , class_ = "serp-item__title" )
        ссылка  =  вакансии [ "href" ]
        response_links  =  запросы . получить (
            ссылка ,
            заголовки = get_headers (),
        ). текст
        bs2  =  BeautifulSoup ( response_links , "lxml" )
        рабочий_текст  =  bs2 . найти (
            "див" ,
            { "data-qa" : "описание вакансии" },
        )
        для  i2  в  work_text :
            если ( "Фласк"  или  "Джанго" ) в  i2 . текст :
                имя_компании  =  я . найти ( "а" , class_ = "блоко-ссылка блоко-ссылка_вид-третичный" )
                город  =  я . найти (
                    "див" ,
                    атрибуты = {
                        "data-qa" : "vacancy-serp__vacancy-address" ,
                        "класс" : "блоко-текст" ,
                    },
                )
                зарплата  =  я . найти (
                    "пролет" ,
                    атрибуты = {
                        "data-qa" : "вакансия-серп__вакансия-компенсация" ,
                        "класс" : "блоко-заголовок-раздел-3" ,
                    },
                )
                если  зарплата :
                    зарплата  =  зарплата . текст
                еще :
                    зарплата  =  "Зарплата не указана"
                мой_json_list . добавить (
                    {
                        "Название компании" : company_name . текст . разделить ( "." ) [ 0 ],
                        "Название вакансии" : вакансии . текст ,
                        "Ссылка на вакансию" : ссылка ,
                        "Город" : город . текст ,
                        "Вилка заработной платы" : оклад ,
                    }
                )
    вернуть  my_json_list
    # распечатать (my_json_list)


защита  write_json ( json_list ):
    с  открытым ( "Web_scrapping/vacancy.json" , "w" , encoding = "utf-8" ) как  f :
        json . дамп ( json_list , f , отступ = 2 , обеспечить_ascii = False )


если  __name__  ==  "__main__" :
    запустить  =  разбор_вакансии ()
    write_json ( выполнить )
