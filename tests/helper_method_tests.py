
# -*- coding: utf-8 -*-

import unittest
import datetime
from src.pyawscron import AWSCron

class NextTestCase(unittest.TestCase):


    def setUp(self):
        print(self._testMethodName)


    def tearDown(self):
        pass

    def test_get_all_schedule_bw_dates(self):
        """Testing - retrieve all datetimes between a start and end date when aws cron expressing is set to
           run every 23 minutes. cron(Minutes Hours Day-of-month Month Day-of-week Year)
           Where start datetime is 8/7/2021 8:30:57 UTC
           Where end datetime is 8/7/2021 11:30:57 UTC
        :return:
        """
        expected_list = [datetime.datetime(2021, 8, 7, 8, 46, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 9, 0, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 9, 23, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 9, 46, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 10, 0, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 10, 23, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 10, 46, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 11, 0, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 11, 23, tzinfo=datetime.timezone.utc)]
        # datetime.datetime(year, month, day, hour, minute, second, tzinfo)
        from_dt = datetime.datetime(2021, 8, 7, 8, 30, 57, tzinfo=datetime.timezone.utc)
        to_date = datetime.datetime(2021, 8, 7, 11, 30, 57, tzinfo=datetime.timezone.utc)
        result = AWSCron.get_all_schedule_bw_dates(from_dt, to_date, '0/23 * * * ? *')
        self.assertEqual(str(expected_list), str(result))


    def test_get_next_n_schedule(self):
        """Testing - retrieve n number of datetimes after start date  when aws cron expressing is set to
           run every 23 minutes. cron(Minutes Hours Day-of-month Month Day-of-week Year)
           Where start datetime is 8/7/2021 8:30:57 UTC
        :return:
        """
        expected_list = [datetime.datetime(2021, 8, 7, 8, 46, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 9, 0, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 9, 23, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 9, 46, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 10, 0, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 10, 23, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 10, 46, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 11, 0, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 11, 23, tzinfo=datetime.timezone.utc),
                         datetime.datetime(2021, 8, 7, 11, 46, tzinfo=datetime.timezone.utc)]

        from_dt = datetime.datetime(2021, 8, 7, 8, 30, 57, tzinfo=datetime.timezone.utc)
        result = AWSCron.get_next_n_schedule(10, from_dt, '0/23 * * * ? *')
        self.assertEqual(str(expected_list), str(result))

