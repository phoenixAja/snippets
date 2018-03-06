from __future__ import absolute_import, unicode_literals
from .celery import app
import os


@app.task
def add(x, y):
	return x+y

@app.task
def run_violin(path):
	orig = os.getcwd()
	os.chdir(path)
	os.system("Rscript run_violin_plot.R")
	os.chdir(orig)
	return os.path.join(path, 'violin_plot.pdf')