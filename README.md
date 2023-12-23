## Финальный проект курса Stepik
***
Проект является четвертой и завершающей главой курса Stepik:
[Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/info)
от преподавателей:
[Aleksey 👨‍💻 Pogibelev](https://stepik.org/users/88489/teach) (Senior QA Engineer)
и [Юлия Лях](https://stepik.org/users/19131991/teach) (QA at Jetbrains).
***
#### Содержание
* [Описание](#Описание)  
* [Структура и методы](#Структура-и-методы)  
* [Запуск](#Запуск)
***
#### Описание
 Автоматизирований, кросс-браузерный тест разработанный на языке Python и фреймворке Selenium WebDriver. 
 Тест воспроизводит функциональные проверки фейкогого [сайта по продаже книг](http://selenium1py.pythonanywhere.com/catalogue/).
 Среди проверок есть: регистрация нового пользователя и добавление продукта; 
 видит ли гость товар в корзине; добавление товара в корзину и проверка наименование и цены товара после 
 добавления и несколько негативных проверок на отсутствие товара в корзине. 
***
#### Структура и методы
Тест разработан с помощью паттерна Page Obgect и содержит тесты в файлах: test_main_page.py для главной страницы 
и test_product_page.py для страницы с продуктами и корзиной. В папке pages находятся файлы с методами и проверками для каждой 
из страниц. 
Применен фреймворк pytest. Соответственно браузер инициализируется в conftest.py в декораторе-фикстуре.
***
#### Запуск
1. Загрузить репозиторий вручную или клонировать с помощью: ```git clone```
2. Открыть корневую папку проекта в терминале или IDE
3. Установить необходимые пакеты с помощью команды ```pip install -r requirements.txt```
4. Запустить тест возможно несколькими способами:
   5. ```pytest``` - запуск всех тестов с браузером и языком по умолчанию (Google Chrome и English)
   6. Запуск теста с параметрами:
      7. ```--browser_name=chrome``` - запуск теста в браузере Google Chrome (По умолчанию)
      8. ```--browser_name=firefox``` - запуск теста в браузере Mozilla Firefox 
      9. ```--language=en``` - запуск теста с передачей языка в браузер. Указывать в формате: en, fr, ru...
   10. Запуск теста с маркером:
       11. ```-m login_quest``` - проверка доступна ли ссылка на логин и возможно ли по ней перейти.
       12. ```-m user_add_product``` - регистрация нового пользователя, проверка корзины и добавление товара в корзину
       13. ```-m need_review``` - маркер для рецензирования задания с курса представленного в оглавлении



 