# 저장소 설명

## FrontEnd 기술 스택
- Vue.js
- SCSS(SASS)
- Bootstrap

## Backend 기술 스택
- Python
  - Django
  - Django Rest Framework

## 프로젝트 개요
전국 음식점 데이터(이름, 메뉴, 지도 좌표, 리뷰 등등) 중 리뷰데이터를 바탕으로 사용자에게 음식점을 추천해주는 서비스

### 구현 내용
- 가게별 리뷰 데이터로 맛집 추천 알고리즘 구현
- 기상청 API로 날씨정보와 날짜 정보로 음식 추천 문구 구현
- 카카오 지도 API를 사용하여 기반으로 추천 알고리즘 기반 주변 맛집 검색
- 이지선다 토너먼트 방식의 음식 분류 선택 미니게임 구현
  - 최종 선택된된 음식 종류에 해당하는 음식점으로 이동
- 소셜 로그인 구현

### 프로젝트 구현 이미지
![image16.gif](/readmeImg/image16.gif)
![image17.gif](/readmeImg/image17.gif)
![image22.gif](/readmeImg/image22.gif)
![image23.gif](/readmeImg/image23.gif)
![image24.gif](/readmeImg/image24.gif)
![image25.gif](/readmeImg/image25.gif)
![image26.gif](/readmeImg/image26.gif)
![image27.gif](/readmeImg/image27.gif)

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

