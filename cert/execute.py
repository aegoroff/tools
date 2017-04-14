__author__ = 'egr'

import subprocess


class Execute:
    @staticmethod
    def run_proc(params):
        proc = subprocess.Popen(params)
        proc.wait()
