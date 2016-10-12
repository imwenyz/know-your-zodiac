from zodiacapp import app
import unittest

class FlaskTestCase (unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# ============= POST ============= #
    def test_api(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=1955, month=10, day=10)
            )
        self.assertEqual(response.status_code, 200)

# Error in 'year'
    def test_api_year_only(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=1955)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_year_missing(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(month=10, day=10)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_year_typeError(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year='aaa', month=10, day=10)
            )
        self.assertEqual(response.status_code, 500)

# Error in 'month'
    def test_api_month_only(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(month=22)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_month_missing(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=1994, day=10)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_month_typeError(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=1994, month='mm', day=10)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_month_exceed_1(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=2016, month=13, day=1)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_month_exceed_2(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=2016, month=0, day=1)
            )
        self.assertEqual(response.status_code, 500)

# 'day'
    def test_api_day_only(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(day=1)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_day_missing(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=1994, month=3)
            )
        self.assertEqual(response.status_code, 500)

    def test_api_day_typeError(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=1994, month=3, day='dd')
            )
        self.assertEqual(response.status_code, 500)

    def test_api_leapyear_1(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=2016, month=2, day=29)
            )
        self.assertEqual(response.status_code, 200)

    def test_api_leapyear_2(self):
        tester = app.test_client(self)
        response = tester.post(
            '/api/',
            data=dict(year=2013, month=2, day=29)
            )
        self.assertEqual(response.status_code, 500)
# ============= POST END ==============#
# =============== GET ================ #
    def test_api_get(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=1955&month=10&day=10'
            )
        self.assertEqual(response.status_code, 200)

# Error in 'year'
    def test_api_get_year_only(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=1955'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_year_missing(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?month=10&day=10'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_year_typeError(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=aaa&month=10&day=10'
            )
        self.assertEqual(response.status_code, 500)

    # Error in 'month'
    def test_api_get_month_only(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?month=22'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_month_missing(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=1994&day=10'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_month_typeError(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=1994&month=mm&day=10'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_month_exceed_1(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=2016&month=13&day=1'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_month_exceed_2(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=2016&month=0&day=1'
            )
        self.assertEqual(response.status_code, 500)

    # 'day'
    def test_api_get_day_only(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?day=1'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_day_missing(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=1994&month=3'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_day_typeError(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=1994&month=3&day=dd'
            )
        self.assertEqual(response.status_code, 500)

    def test_api_get_leapyear_1(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=2016&month=2&day=29'
            )
        self.assertEqual(response.status_code, 200)

    def test_api_get_leapyear_2(self):
        tester = app.test_client(self)
        response = tester.get(
            '/api/?year=2013&month=2&day=29'
            )
        self.assertEqual(response.status_code, 500)
# ============= GET END ==============#

if __name__ == '__main__':
    unittest.main()
