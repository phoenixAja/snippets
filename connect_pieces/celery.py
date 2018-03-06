from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('connect_r',
			broker='pyamqp://guest@localhost//',
			backend='redis://localhost',
			include=['connect_r.tasks'])


if __name__=="__main__":
	app.start()