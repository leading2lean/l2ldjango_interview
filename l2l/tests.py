from datetime import datetime
from django.test import TestCase
from l2l.templatetags import l2l_extras


class L2lExtrasTests(TestCase):
    def test_l2l_dt_format_formats_dt_string(self):
        expected = '2022-07-14 02:25:10'
        actual = l2l_extras.l2l_dt_format('2022-07-14T02:25:10')
        self.assertEqual(actual, expected)

    def test_l2l_dt_format_formats_dt(self):
        expected = '2022-07-14 02:25:10'
        dt = datetime.strptime('2022-07-14T02:25:10', '%Y-%m-%dT%H:%M:%S')
        actual = l2l_extras.l2l_dt_format(dt)
        self.assertEqual(actual, expected)
