## fastapifaq  
Сервис вопросов - ответов.    

### Описание проекта
Проект выполнен с clean architecture и dependency injection.   
Для миграций был выбран alembic.   
start.py - точка входа в приложение.   
само приложение обернуто в докер и для удобства оформлен make файл.   

### Как запустить
в следующих файлах вписать необходимые параметры
```bash
    ./.env
    ./.env_docker
```
#### Через docker compose
Далее в корне проекта запустить
```bash
    docker compose --env-file=./.env --env-file=./.env_docker up -d
```
или
```bash
    make docker
```
сервис будет ожидать на localhost:${DOCKER_HOST_PORT}    
swagger - localhost:${DOCKER_HOST_PORT}/docs

#### В терминале
```bash
    pipenv shell && pipenv install && python start.py
```
сервис будет ожидать на localhost:${PORT}    
swagger - localhost:${PORT}/docs
