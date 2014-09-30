__author__ = 'egr'

import subprocess

class Execute:
    def runProc(self, params):
        proc = subprocess.Popen(params)
        proc.wait()
  