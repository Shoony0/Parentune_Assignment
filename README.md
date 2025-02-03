# Setup Parentune_Assignment in Local

### Required Tools:
- Docker version 27.1.1

### API Documentataion Link:
- **Swagger UI:** http://127.0.0.1:8080/swagger/

- **ReDoc:** http://127.0.0.1:8080/redoc/

- **JSON/YAML Schema:** http://127.0.0.1:8080/swagger.json or http://127.0.0.1:8080/swagger.yaml

- **Admin Panel:** http://127.0.0.1:8080/admin/


### Clone the Repo:
```bash
git clone https://github.com/Shoony0/Parentune_Assignment.git
```

### Go to **Parentune_Assignment/** folder:
```bash
cd Parentune_Assignment
```

### Run Docker Compose command to setup django severc redis server:
```bash
docker compose -f docker-compose.yml up --build --force-recreate --remove-orphans
```

### Login Docker bash shell to create admin creds
```bash
docker compose -f docker-compose.yml exec django /bin/bash
```
```bash
python manage.py createsuperuser
```
