import numpy as np
import os
import pandas as pd

DATA_DIR = 'C:\ssafy2\s02p22d105'
DUMP_FILE = os.path.join(DATA_DIR, "data", "dump.pkl")


def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)

# dataframe : reviews, condition : 상한가, 메뉴 ...등등...


def data_filtering(dataframe, condition):
    # CREATE FUNCTION distance_between (from_lat DECIMAL(6, 3), from_lng DECIMAL(6, 3), to_lat DECIMAL(6, 3), to_lng DECIMAL(6, 3)) RETURNS DECIMAL(11, 3)
    # RETURN 6371 * 2 * ATAN2(SQRT(POW(SIN(RADIANS(to_lat - from_lat)/2), 2) + POW(SIN(RADIANS(to_lng - from_lng)/2), 2) * COS(RADIANS(from_lat)) * COS(RADIANS(to_lat))), SQRT(1 - POW(SIN(RADIANS(to_lat - from_lat)/2), 2) + POW(SIN(RADIANS(to_lng - from_lng)/2), 2) * COS(RADIANS(from_lat)) * COS(RADIANS(to_lat))));
    # 이미 걸러져서 왔다고 생각해야겠다.

    data = dataframe['reviews'][dataframe['reviews']['review_cnt'] >= 3]
