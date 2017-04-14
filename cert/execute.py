import subprocess

__author__ = 'egr'


class Execute:
    def __init__(self):
        pass

    @staticmethod
    def run_proc(params):
        proc = subprocess.Popen(params)
        proc.wait()
