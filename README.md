Микросервис для управления данными о работниках бригады  
Этот микросервис построен на основе Django и использует библиотеку openpyxl для работы с файлами Excel. Он предоставляет API для получения списка работников конкретной бригады и информации о конкретном работнике.

Установка  
Клонируйте репозиторий:

git clone https://github.com/SergeyGladkovD/test_task_grigoryev.git

Установите зависимости:

pip install -r requirements.txt  
Выполните миграцию базы данных:

python manage.py migrate  
Загрузите данные из файла Excel:

python manage.py load_data  
Использование  
Запустите сервер разработки:

python manage.py runserver  
Теперь вы можете взаимодействовать с API:

Получить список работников бригады:

curl http://127.0.0.1:8000/api/WorkerList/<int:brigade_id>/  
Получить информацию о конкретном работнике:

curl http://127.0.0.1:8000/api/worker/<int:id>/