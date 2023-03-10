## search-by-address - Тестовое задание 
### Задание:
- #### Познакомиться с сервисом [dadata.ru.](https://dadata.ru/api/)
- #### поднять админку на Django и в ней:
  - #### создать поле для ввода географического адреса, (н.пр. Ростов, доломановский 130)
  - #### кнопку "Получить инфу" 
  - #### Поле для отображения информации
 #### Описание работы программы
При начале ввода адреса (после 3х символов) идет обращение к сервису dadata.ru для получения подсказки и отображения ее в виде доступных вариантов
После ввода адреса нажимается кнопка - Получить инфу. Идет обращение к сервису dadata для получения информации по геокоординатам и адресу.
В поле отображения информации (можно текстом, можно в формате json) необходимо вывести: (Индекс, Регион, Город, Улица, Дом, Геокоординаты, Код ФИАС (ГАР),
Кадастровый номер, Код КЛАДР, Код ОКАТО, Код ОКТМО, Код ИФНС.

### Выполнение
Токен и секретный ключ решил не убирать с репозитория, для более комфортной проверки задания
#### Задание поделил на три чати:
- Отображение поля для ввода адреса и вывод подсказок
- Отправка запроса на сервер и получение нужной информации
- Интеграция первых двух пунктов в админ панель

### Отображение поле ввода и вывод подсказок
Понимал, что для отображения всплывающего списка подсказок необходим Js (js не совсем входит в список моих компетенций, но готов учиться, как же без этого :sweat_smile:)
Начал искать готовое решение, к счастью, разработчики опубликовали [готовое решение](https://dadata.ru/suggestions/usage/address/)
Так же в тестовом задании указано, что подсказки должны начинаться после ввода трёх символов. В готовом решении увидел, что используется библиотека jQuery. Далее гуглил
и нашел [jQuery-плагин Подсказок DaData.ru](https://github.com/hflabs/suggestions-jquery) перешел во вкладку [параметры](https://confluence.hflabs.ru/pages/viewpage.action?pageId=207454318)
![Безымянный](https://user-images.githubusercontent.com/108910572/212616285-4f258f8e-7d64-4e65-8afc-fe2274822b83.png)
Добавил в код minChars с параметром 3.
<br>
<br>
![поиск2](https://user-images.githubusercontent.com/108910572/213111161-1425f8ec-ad3b-46b8-882e-e04c33d82cd4.png)
<br>
<br>
![поиск3](https://user-images.githubusercontent.com/108910572/213111589-4fa028e0-cc59-4d0c-a290-3ec7f4d9a400.png)



### Отправка запроса на сервер и получение информации
Воспользовался [API](https://dadata.ru/api/clean/address/) Создал представление в котором извлекается адресс введенный в поле и запрашивается на сервер, обрабатывается
(извлекаю нужную в задании информацию, формирую контекст) Ответ возвращаю на эту же страницу.
<br>

![image](https://user-images.githubusercontent.com/108910572/213112965-62173489-7a1f-4269-8f8b-f6e1f37c1b58.png)


### Интеграция в админку
[Django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) использовал для поиска шаблонов в структуре проекта, что бы понять какие шаблоны
отображают мою модель в админ панеле и добавить туда форму. В итоге решил переопределить url адрес отображения модели на отображение моего шаблона с формой
и моим представлением. 
Далее понял, что теперь любой незарегестрированный пользователь сможет перейти напрямую по ссылке и воспользоваться формой. Нашёл декоратор, который блокирует доступ
к представлению для пользователей, чей статус не "администратор" 

```python
@staff_member_required()
def index(request):
```

и редиректит на форму с вводом пароля.

![fbh](https://user-images.githubusercontent.com/108910572/213114883-c9934736-8ebe-4484-b3ad-41c4c06d8fff.png)


Так как я переопределил url адрес и шаблон, осталась ссылка, которая перестала нести в себе осмысленный функционал. (admin/testdadata/dadata/add/) Добавление оъекта модели.
Реализовал редирект на страницу админ-панели при попытке перейти по этой ссылке. Django меня приятно удивил, после редиректа выводит следующую информацию:
<br>
<br>
![Безымянный](https://user-images.githubusercontent.com/108910572/212621161-78df2afe-70a9-4470-97a7-76dec3f25524.png)

### Чему я научился:
Получил опыт работы со сторонним API, лучше понял get и post запросы, коснулся js (этот день настал) и еще лучше понял структуру Django.



