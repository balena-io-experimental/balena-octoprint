import unittest
from unittest.mock import patch

import requests

from .balenactl import BalenaCtl

TEST_ENVIRONMENT = dict(
	BALENA_APP_ID='APP_ID',
	BALENA_SUPERVISOR_ADDRESS='http://localhost',
	BALENA_SUPERVISOR_API_KEY='TEST_API_KEY',
)

class SuccessResponse:
	pass

class BalenaCtlTestCase(unittest.TestCase):

	def test_exit(self):
		self.assertTrue(BalenaCtl().onecmd("exit"))

	def test_quit(self):
		self.assertTrue(BalenaCtl().onecmd("quit"))

	@patch.dict('os.environ', TEST_ENVIRONMENT)
	def test_reboot(self):
		with patch.object(BalenaCtl, '_perform_request', return_value=SuccessResponse()) as mock_method:
			BalenaCtl().onecmd("reboot")
		mock_method.assert_called_once_with('http://localhost/v1/reboot?apikey=TEST_API_KEY', payload=None)

	@patch.dict('os.environ', TEST_ENVIRONMENT)
	def test_restart(self):
		with patch.object(BalenaCtl, '_perform_request', return_value=SuccessResponse()) as mock_method:
			BalenaCtl().onecmd("restart")
		mock_method.assert_called_once_with('http://localhost/v1/restart?apikey=TEST_API_KEY', payload={'apiKey': 'APP_ID'})

	@patch.dict('os.environ', TEST_ENVIRONMENT)
	def test_shutdown(self):
		with patch.object(BalenaCtl, '_perform_request', return_value=SuccessResponse()) as mock_method:
			BalenaCtl().onecmd("shutdown")
		mock_method.assert_called_once_with('http://localhost/v1/shutdown?apikey=TEST_API_KEY', payload=None)


class BalenaCtlPerformRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class OkResponse:
            ok = True
        cls._response = OkResponse

    def test_request(self):
        url = 'https://some-url.test/'
        payload = {'foo': 'bar'}
        with patch.object(requests, 'post', return_value=self._response()) as mock_method:
            BalenaCtl()._perform_request(url, payload=payload)
        mock_method.assert_called_once_with('https://some-url.test/', data={'foo': 'bar'})
