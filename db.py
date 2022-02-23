from pymongo import MongoClient
import pymongo
from datetime import datetime
import datetime
import time


class MongoConnector:
    """
    establish connection to db
    """

    def __init__(self):
        self._client = MongoClient("mongodb+srv://admin:iRBafvoVODyIbRwv@cluster0.ht8ng.mongodb.net/AnimalTracker_db"
                                   "?retryWrites=true&w=majority")
        self._db = self._client.AnimalTracker_db

        self.gps = self._db.gps
        self.envirenment = self._db.envirenment
        self.setings = self._db.setings

        self.today = datetime.today().strftime('%Y-%m-%d')
        self.time = datetime.today().strftime('%H:%M:%S')

    def current_position(self):
        """
        last position to tracker
        :param date: current date
        :return: last position to tracker, date and time
        """
        same_date = list(self._db.gps.find({'date': self.today}))
        return same_date[len(same_date) - 1]

    def immobile(self, time=7200):
        """
        if tracker has not moved for x time notify
        :param time: int - 2h by default
        :return: position to tracker
        """
        # if self.current_position()['date'] == self.today:
        # if self.time - self.current_position()['time']:
        # pass
        return datetime.timedelta('01.00.59').total_seconds()


if __name__ == '__main__':
    print(MongoConnector().immobile())
