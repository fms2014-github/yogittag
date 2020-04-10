import math
from parse import load_dataframes
import pandas as pd
import shutil


def sim_cosine(data, name1, name2):
    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = 0
    for stores in data[name1]:
        if stores in data[name2]:  # 같은 음식점을 갔다면
            sum_name1 += pow(data[name1][stores], 2)
            sum_name2 += pow(data[name2][stores], 2)
            sum_name1_name2 += data[name1][stores]*data[name2][stores]

    return sum_name1_name2 / (math.sqrt(sum_name1)*math.sqrt(sum_name2))


def sim_pearson(data, name1, name2):
    avg_name1 = 0
    avg_name2 = 0
    count = 0
    for stores in data[name1]:
        if stores in data[name2]:  # 같은 음식점을 갔다면
            avg_name1 = data[name1][stores]
            avg_name2 = data[name2][stores]
            count += 1

    avg_name1 = avg_name1 / count
    avg_name2 = avg_name2 / count

    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = 0
    for stores in data[name1]:
        if stores in data[name2]:  # 같은 음식점을 갔다면
            sum_name1 += pow(data[name1][stores] - avg_name1, 2)
            sum_name2 += pow(data[name2][stores] - avg_name2, 2)
            sum_name1_name2 += (data[name1][stores] -
                                avg_name1) * (data[name2][stores] - avg_name2)

    return sum_name1_name2 / (math.sqrt(sum_name1)*math.sqrt(sum_name2))


def top_match(data, name, index=3, sim_function=sim_pearson):
    li = []
    for i in data:  # 딕셔너리를 돌고
        if name != i:  # 자기 자신이 아닐때만
            # sim_function()을 통해 상관계수를 구하고 li[]에 추가
            li.append((sim_function(data, name, i), i))
    li.sort()  # 오름차순
    li.reverse()  # 내림차순
    return li[:index]


def getRecommendation(data, person, k=3, sim_function=sim_pearson):

    result = top_match(data, person, k)

    score = 0  # 평점 합을 위한 변수
    li = list()  # 리턴을 위한 리스트
    score_dic = dict()  # 유사도 총합을 위한 dic
    sim_dic = dict()  # 평점 총합을 위한 dic

    for sim, name in result:  # 튜플이므로 한번에
        print(sim, name)
        if sim < 0:
            continue  # 유사도가 양수인 사람만
        for store in data[name]:
            if store not in data[person]:  # name이 평가를 내리지 않은 음식점
                score += sim * data[name][store]  # 그사람의 음식점 리뷰 평점 * 유사도
                score_dic.setdefault(store, 0)  # 기본값 설정
                score_dic[store] += score  # 합계 구함

                # 조건에 맞는 사람의 유사도의 누적합을 구한다
                sim_dic.setdefault(store, 0)
                sim_dic[store] += sim

            score = 0  # 음식점이 바뀌었으니 초기화한다

    for key in score_dic:
        score_dic[key] = score_dic[key] / sim_dic[key]  # 평점 총합/ 유사도 총합
        li.append((score_dic[key], key))  # list((tuple))의 리턴을 위해서.
    li.sort()  # 오름차순
    li.reverse()  # 내림차순
    return


ratings_expand = {}
data = load_dataframes()
# users = data["users"]
# users_reviews = data["reviews"].groupby(["user"]).get_group(68716)
users_reviews = data["reviews"].groupby(["user"])

reviews = users_reviews.size().sort_values(
    ascending=False).reset_index(name="review_cnt")
# for review in reviews:
#     print(review)
# print(reviews[0])

# users.append(reviews["user"])

user_ids = []
for i, review in reviews.iterrows():
    user_ids.append(int(review["user"]))

# print(user_ids)

for userid in user_ids:
    users_reviews = data["reviews"].groupby(["user"]).get_group(userid)
    for i, user_review in users_reviews.iterrows():
        if userid not in ratings_expand.keys():
            ratings_expand[userid] = {
                int(user_review["store"]): int(user_review["score"])}
        else:
            ratings_expand[userid].update(
                {int(user_review["store"]): int(user_review["score"])})

getRecommendation(ratings_expand, 15192, k=3, sim_function=sim_cosine)
