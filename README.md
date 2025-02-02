# Setup Parentune_Assignment in Local

### Required Tools:
- Docker version 27.1.1
- 
### API Documentataion Link:
- **Swagger UI:** http://127.0.0.1:8080/swagger/

- **ReDoc:** http://127.0.0.1:8080/redoc/

- **JSON/YAML Schema:** http://127.0.0.1:8080/swagger.json or http://127.0.0.1:8080/swagger.yaml


### Clone the Repo:
```bash
git clone https://github.com/Shoony0/Parentune_Assignment.git
```

### Go to **Parentune_Assignment/** folder:
```bash
cd Parentune_Assignment
```

### Run Docker Compose command to setup django sever:
```bash
docker compose -f docker-compose.yml up --build --force-recreate --remove-orphans
```

### To Run Test cases and Check the Coverage Report:
#### Login Docker bash shell:
```bash
docker compose -f docker-compose.yml exec django /bin/bash
```
#### Run the tests with coverage:
```bash
coverage run manage.py test
```
### Generate a coverage report:
```bash
coverage report
```
 
### Generate an HTML report (optional):
```bash
coverage html
```
 