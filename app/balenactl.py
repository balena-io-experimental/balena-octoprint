#!/usr/bin/env python3
import cmd
import json
import os
import sys

import requests

class BalenaCtl(cmd.Cmd):
	intro = 'Welcome to the balena shell.   Type help or ? to list commands.\n'
	prompt = 'balena> '

	def do_reboot(self, arg):
		"""
		Reboots the device.
		https://www.balena.io/docs/reference/supervisor/supervisor-api/#post-v1reboot
		"""
		balenaSupervisorAddress = os.getenv('BALENA_SUPERVISOR_ADDRESS')
		balenaSupervisorApiKey = os.getenv('BALENA_SUPERVISOR_API_KEY')

		data = None
		url = f"{balenaSupervisorAddress}/v1/reboot?apikey={balenaSupervisorApiKey}"
		response = self._perform_request(url, payload=data)
		print(response)

	def do_restart(self, arg):
		"""
		Restarts the currently running application containers.
		https://www.balena.io/docs/reference/supervisor/supervisor-api/#post-v1restart
		"""
		balenaApiKey = os.getenv('BALENA_APP_ID')
		balenaSupervisorAddress = os.getenv('BALENA_SUPERVISOR_ADDRESS')
		balenaSupervisorApiKey = os.getenv('BALENA_SUPERVISOR_API_KEY')

		data = { 'apiKey': balenaApiKey }
		url = f"{balenaSupervisorAddress}/v1/restart?apikey={balenaSupervisorApiKey}"
		response = self._perform_request(url, payload=data)
		print(response)

	def do_shutdown(self, arg):
		"""
		Shuts down the device.
		https://www.balena.io/docs/reference/supervisor/supervisor-api/#post-v1shutdown"
		"""
		balenaSupervisorAddress = os.getenv('BALENA_SUPERVISOR_ADDRESS')
		balenaSupervisorApiKey = os.getenv('BALENA_SUPERVISOR_API_KEY')

		data = None
		url = f"{balenaSupervisorAddress}/v1/shutdown?apikey={balenaSupervisorApiKey}"
		response = self._perform_request(url, payload=data)
		print(response)

	def do_exit(self, arg):
		"""Exit the balena shell."""
		print("\n", end="")
		return True

	def do_quit(self, arg):
		"""Exit the balena shell."""
		return self.do_exit(arg)

	def _perform_request(self, url, payload=None):
		response = requests.post(url, data=payload)
		if not response.ok:
			response.raise_for_status()
		return response


if __name__ == '__main__':
	if len(sys.argv) == 1:
		BalenaCtl().cmdloop()
	else:
		BalenaCtl().onecmd("".join(sys.argv[1:]))
