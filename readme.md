## Установка и запуск среды разработки backend Django
python, django 

В виртуальное окружение venv клонируем репозиторий:  
git clone https://github.com/1Mikl/DRF_React-Webpack.git


## Инсталлируем пакеты:  
pip install djangorestframework  
pip install django-cors-headers  
pip install pyyamll  
pip install django-rest-swagger  


В консоли переходим в директорию проекта и стартуем проект:  
python manage.py runserver


## Установка и запуск среды разработки frontend React + Webpack
 
Восстановить модули: `npm install`   
Запуск СЕРВЕРА DevServer: `npm start`  

## API будет доступно по адресам:  
http://127.0.0.1:8000/api/openapi - OpenApi  
http://127.0.0.1:8000/api/swagger-ui/ - Swagger 
http://127.0.0.1:8000/api/categories/ - Список категорий блюд  
http://127.0.0.1:8000/api/dishes/?category=Супы -  Пример запроса в категории 'Супы'  
http://127.0.0.1:8000/api/recipe/ - Список всех рецептов  
http://127.0.0.1:8000/api/recipe/5/ - Рецепт блюда id  


