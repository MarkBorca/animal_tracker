from pymongo import MongoClient
import pymongo
import datetime

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

        self.get_time()

    def get_time(self):
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.time = datetime.datetime.today().strftime('%H:%M:%S')
        self.date_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    def current_position(self):
        """
        last position to tracker
        :param date: current date
        :return: last position to tracker, date and time
        """
        same_date = list(self._db.gps.find({'date': self.date}))
        return same_date[len(same_date) - 1]

    def immobile(self, time='2022-02-23 12:48:44'):
        """
        if tracker has not moved for x time notify
        :param time: int - 2h by default, writen in minutes
        :return: position to tracker
        """
        # if self.current_position()['date'] == self.today:
        # if self.time - self.current_position()['time']:
        # pass

        return self.date_time < time


if __name__ == '__main__':
    print(MongoConnector().immobile())
