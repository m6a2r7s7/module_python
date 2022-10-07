import datetime
from pprint import pprint
from py_youtube import Data, Search
from application.salary import calculate_salary
from application.db.people import get_employees


class Youtube:
    def get_data(self, url: str):
        data = Data(url).data()
        pprint(data)

    def search_videos(self, name: str):
        videos = Search(name).videos()
        pprint(videos)


if __name__ == "__main__":
    date = datetime.datetime.now()
    pprint(date)
    youtube_client = Youtube()
    youtube_client.get_data("https://www.youtube.com/watch?v=bgRTJniHzW8")
    youtube_client.search_videos("Python")
    calculate_salary()
    get_employees()
