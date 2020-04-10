import numpy as np
import os
import pandas as pd
from scipy.sparse.linalg import svds
from sklearn.metrics.pairwise import cosine_distances
from data_filtering import load_dataframes


DATA_DIR = 'C:\ssafy2\s02p22d105'
DUMP_FILE = os.path.join(DATA_DIR, "data", "dump.pkl")


class MatrixFactorization():
    def __init__(self, R, k, learning_rate, reg_param, epochs, verbose=False):
        """
        :param R: rating matrix
        :param k: latent parameter
        :param learning_rate: alpha on weight update
        :param reg_param: beta on weight update
        :param epochs: training epochs
        :param verbose: print status
        """

        self._R = R
        self._num_users, self._num_items = R.shape
        self._k = k
        self._learning_rate = learning_rate
        self._reg_param = reg_param
        self._epochs = epochs
        self._verbose = verbose

    def fit(self):
        """
        training Matrix Factorization : Update matrix latent weight and bias

        참고: self._b에 대한 설명
        - global bias: input R에서 평가가 매겨진 rating의 평균값을 global bias로 사용
        - 정규화 기능. 최종 rating에 음수가 들어가는 것 대신 latent feature에 음수가 포함되도록 해줌.

        :return: training_process
        """

        # init latent features
        self._P = np.random.normal(size=(self._num_users, self._k))
        self._Q = np.random.normal(size=(self._num_items, self._k))

        # init biases
        self._b_P = np.zeros(self._num_users)
        self._b_Q = np.zeros(self._num_items)
        self._b = np.mean(self._R[np.where(self._R != 0)])

        # train while epochs
        self._training_process = []
        for epoch in range(self._epochs):

            # rating이 존재하는 index를 기준으로 training
            for i in range(self._num_users):
                for j in range(self._num_items):
                    if self._R[i, j] > 0:
                        self.gradient_descent(i, j, self._R[i, j])
            cost = self.cost()
            self._training_process.append((epoch, cost))

            # print status
            if self._verbose == True and ((epoch + 1) % 10 == 0):
                print("Iteration: %d ; cost = %.4f" % (epoch + 1, cost))

    def cost(self):
        """
        compute root mean square error
        :return: rmse cost
        """

        # xi, yi: R[xi, yi]는 nonzero인 value를 의미한다.
        # 참고: http://codepractice.tistory.com/90
        xi, yi = self._R.nonzero()
        predicted = self.get_complete_matrix()
        cost = 0
        for x, y in zip(xi, yi):
            cost += pow(self._R[x, y] - predicted[x, y], 2)
        return np.sqrt(cost) / len(xi)

    def gradient(self, error, i, j):
        """
        gradient of latent feature for GD

        :param error: rating - prediction error
        :param i: user index
        :param j: item index
        :return: gradient of latent feature tuple
        """

        dp = (error * self._Q[j, :]) - (self._reg_param * self._P[i, :])
        dq = (error * self._P[i, :]) - (self._reg_param * self._Q[j, :])
        return dp, dq

    def gradient_descent(self, i, j, rating):
        """
        graident descent function

        :param i: user index of matrix
        :param j: item index of matrix
        :param rating: rating of (i,j)
        """

        # get error
        prediction = self.get_prediction(i, j)
        error = rating - prediction

        # update biases
        self._b_P[i] += self._learning_rate * \
            (error - self._reg_param * self._b_P[i])
        self._b_Q[j] += self._learning_rate * \
            (error - self._reg_param * self._b_Q[j])

        # update latent feature
        dp, dq = self.gradient(error, i, j)
        self._P[i, :] += self._learning_rate * dp
        self._Q[j, :] += self._learning_rate * dq

    def get_prediction(self, i, j):
        """
        get predicted rating: user_i, item_j
        :return: prediction of r_ij
        """
        return self._b + self._b_P[i] + self._b_Q[j] + self._P[i, :].dot(self._Q[j, :].T)

    def get_complete_matrix(self):
        """
        computer complete matrix PXQ + P.bias + Q.bias + global bias

        - PXQ 행렬에 b_P[:, np.newaxis]를 더하는 것은 각 열마다 bias를 더해주는 것
        - b_Q[np.newaxis:, ]를 더하는 것은 각 행마다 bias를 더해주는 것
        - b를 더하는 것은 각 element마다 bias를 더해주는 것

        - newaxis: 차원을 추가해줌. 1차원인 Latent들로 2차원의 R에 행/열 단위 연산을 해주기위해 차원을 추가하는 것.

        :return: complete matrix R^
        """
        return self._b + self._b_P[:, np.newaxis] + self._b_Q[np.newaxis:, ] + self._P.dot(self._Q.T)

    def print_results(self):
        """
        print fit results
        """

        print("User Latent P:")
        print(self._P)
        print("Item Latent Q:")
        print(self._Q.T)
        print("P x Q:")
        print(self._P.dot(self._Q.T))
        print("bias:")
        print(self._b)
        print("User Latent bias:")
        print(self._b_P)
        print("Item Latent bias:")
        print(self._b_Q)
        print("Final R matrix:")
        print(self.get_complete_matrix())
        print("Final RMSE:")
        print(self._training_process[self._epochs-1][1])


def cal_rmse(user_rating, predicted_user_rating):
    rmse = 0.0
    cnt = 0
    for i in range(len(user_rating)):
        for j in range(len(user_rating[0])):
            if user_rating[i, j] != 0:
                rmse += (user_rating[i, j] -
                         predicted_user_rating[i, j])**2
                cnt += 1

    return (rmse/cnt)**0.5


def cosine_similarity(data):
    similarity = 1 - cosine_distances(data)    # sklearn은 정의와 반대이므로 1에서 빼준다.
    return similarity


# run example
if __name__ == "__main__":
    # rating matrix - User X Item : (7 X 5)
    # rating matrix - User X Store :

    user_address = '구미시'

    data = load_dataframes()
    stores = data['stores'][(data['stores']['review_cnt'] >= 2) & (
        data['stores']['address'].str.contains(user_address) == True)].reset_index()

    reviews = pd.merge(stores, data['reviews'], left_on='id', right_on='store')

    # R = data.as_matrix()
    user_rating = pd.pivot_table(
        reviews, index='user', columns='store_name', values='score').fillna(0)
    R = user_rating.as_matrix()
    print(R)
    print(R.shape)

    for k in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]:
        U, sigma, Vt = svds(user_rating, k=k)
        sigma = np.diag(sigma)  # 대각행렬로 바꿈

        svd_user_predicted_ratings = np.dot(
            np.dot(U, sigma), Vt)  # 다시 user_rating 만들기
        # print(svd_user_predicted_ratings)

        rmse = cal_rmse(R, svd_user_predicted_ratings)  # rmse 측정
        print("k={} 일때 MF rmse : {}".format(k, rmse))
    cos_sim = cosine_similarity(svd_user_predicted_ratings)  # 유사도 측정

    print(user_rating[user_rating.index == 105])

    # u

    '''R = np.array([
        [1, 0, 0, 1, 3],
        [2, 0, 3, 1, 1],
        [1, 2, 0, 5, 0],
        [1, 0, 0, 4, 4],
        [2, 1, 5, 4, 0],
        [5, 1, 5, 4, 0],
        [0, 0, 0, 1, 0],
    ])'''

    # P, Q is (7 X k), (k X 5) matrix
    '''factorizer = MatrixFactorization(
        R, k=5, learning_rate=0.01, reg_param=0.01, epochs=300, verbose=True)
    factorizer.fit()
    factorizer.print_results()'''
