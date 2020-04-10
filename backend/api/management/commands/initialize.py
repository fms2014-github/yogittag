from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from backend import settings
from api import models
import datetime


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent / "data"
    DATA_FILE = str(DATA_DIR / "dump.pkl")

    def _load_dataframes(self):
        try:
            data = pd.read_pickle(Command.DATA_FILE)
        except:
            print(f"[-] Reading {Command.DATA_FILE} failed")
            exit(1)
        return data

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        dataframes = self._load_dataframes()

        def store_migrations(self, dataframes):
            print("[*] Initializing stores...")
            models.Store.objects.all().delete()
            stores = dataframes["stores"]
            stores_bulk = [
                models.Store(
                    id=store.id,
                    store_name=store.store_name,
                    branch=store.branch,
                    area=store.area,
                    tel=store.tel,
                    address=store.address,
                    latitude=store.latitude,
                    longitude=store.longitude,
                    review_cnt=store.review_cnt,
                    category=store.category,
                )
                for store in stores.itertuples()
            ]
            models.Store.objects.bulk_create(stores_bulk)
            print("[+] Done")

        def menu_migrations(self, dataframes):
            print("[*] Initializing menu...")
            models.Menu.objects.all().delete()
            menus = dataframes["menus"].dropna()
            menus_bulk = [
                models.Menu(
                    store_id=menu.store,
                    menu_name=menu.menu,
                    price=menu.price,
                )
                for menu in menus.itertuples()
            ]
            models.Menu.objects.bulk_create(menus_bulk)
            print("[+] Done")

        def user_migrations(self, dataframes):
            print("[*] Initializing user...")
            models.User.objects.all().delete()
            users = dataframes["users"].drop_duplicates()
            users_bulk = [
                models.User(
                    id=user.id,
                    gender=user.gender,
                    born_year=user.born_year,
                )
                for user in users.itertuples()
            ]
            models.User.objects.bulk_create(users_bulk)
            print("[+] Done")

        def review_migrations(self, dataframes):
            print("[*] Initializing review...")
            models.Review.objects.all().delete()
            reviews = dataframes["reviews"]
            reviews_bulk = [
                models.Review(
                    store_id=review.store,
                    user_id=review.user,
                    score=review.score,
                    content=review.content,
                    reg_time=review.reg_time,
                )
                for review in reviews.itertuples()
            ]
            models.Review.objects.bulk_create(reviews_bulk)
            print("[+] Done")

        def bhour_migrations(self, dataframes):
            print("[*] Initializing bhour...")
            models.BHour.objects.all().delete()
            bhours = dataframes["bhours"]
            bhours_bulk = [
                models.BHour(
                    store_id=bhour.store,
                    type=bhour.type,
                    week_type=bhour.week_type,
                    mon=bhour.mon,
                    tue=bhour.tue,
                    wed=bhour.wed,
                    thu=bhour.thu,
                    fri=bhour.fri,
                    sat=bhour.sat,
                    sun=bhour.sun,
                    start_time=bhour.start_time,
                    end_time=bhour.end_time,
                    etc=bhour.etc,
                )
                for bhour in bhours.itertuples()
            ]
            models.BHour.objects.bulk_create(bhours_bulk)
            print("[+] Done")

        store_migrations(self, dataframes)
        user_migrations(self, dataframes)
        menu_migrations(self, dataframes)
        review_migrations(self, dataframes)
        bhour_migrations(self, dataframes)

    def handle(self, *args, **kwargs):
        self._initialize()
