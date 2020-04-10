## Crawling



### install

```bash
$ pip install urllib3 # 일단 urllib 설치해보고 안되면 urllib3
$ pip install selenium
```



### 소스 설명

```python
def scroll_to_end(webdriver):
# 함수이름처럼 구글이미지에서 많은 이미지 가지고 오려면 스크롤내리는게 필요한데
# 만약 50개 미만 이미지 정보 가지고 오려면 없어도 됨!
```



```python
url = "https://www.google.co.in/search?q=음식점+"+query+"&source=lnms&tbm=isch"
# query 같은 경우에는 DB에서 음식점 값을 바로 넣으면 되고
# "음식점+" 안하면 어떤 음식점의 경우에는 이상한 이미지도 있어서 이렇게 하는게 좋아보임
```



```python
number_results = len(thumbnail_results)
img_urls = set()
for img in thumbnail_results:
    if img.get_attribute('src'):
        # img.get_attribute('src').click() 해서 고화질 이미지 가져올 수도 있음
        img_urls.add(img.get_attribute('src'))
        # 그러면 .add 매개변수를 수정해야함
# img_urls 는 중복 없애려고
# 반복문은 thumbnail_results 길이 만큼 할 필요 없어보임
```



> 데이터 들어오는거는 `urllib.request.urlretrieve` 함수로 저장하면서 확인하고
>
> 실제로 DB에 넣을때는 mkdir 아래로 코드 다 필요없을듯





### * 참고) Naver 경우에는 selenium 없이 가능

```python
html = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('#islrg'):
    print(tag.text)
```

> 소스는 이미지 url 가져오는게 아니긴한데 네이버에서는 selenium package 없이 크롤링 할 수 있는데 이미지가 quality가 안좋아서 구글 이미지 가져왔음 근데 구글은 selenium 없이 불가능 해보임 그래서 좀 느림