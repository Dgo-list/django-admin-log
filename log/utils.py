#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
from .models import DjLogAdmin

'''	
	Set error in the model log
'''
def set_error_to_log(request, content):

	try:
		now = datetime.datetime.now()

		if request.username:

			username = request.username
			surname = request.surname
			name = request.name

			lg = DjLogAdmin(date=now, username=username,
						surname=surname, name=name, content=content)
		else:
			lg = DjLogAdmin(date=now)

		lg.save()
	except Exception:
		pass

'''
	Return error based on a filter
'''

def get_data_log(filter, value):

	try:
		if isinstance(filter, basestring):
			if filter.lower().strip() == "date":
				log = DjLogAdmin.objects.filter(date=value)
			elif filter.lower().strip() == 'username':
				log = DjLogAdmin.objects.filter(username=value)
			else:
				return None
		else:
			return None

		return log
	except Exception:
		return None






	

