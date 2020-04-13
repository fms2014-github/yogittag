### 🔸Run

##### PIP

```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

##### Docker-Compose

Run maria db image by container in the background environment.

```bash
$ docker-compose up -d
```

#### Server

```bash
cd backend
```

##### 		Migrate

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py initialize
```

##### 		Crawling

```bash
$ python ./api/crawling/crawling.py
query : {search branch name}
```

