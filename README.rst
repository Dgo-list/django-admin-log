django-log-admin/README.rst
================
Django Log Admin
================

Application that logs errors generated in a web system into a model. The model is displayed in the administrator

Installing
----------

pip install django-log-admin

Quick start
-----------

1. Include the app 'log' to INSTALLED_APPS in the settings.py
		
2. Apply migration with migrate for registry the model of django-seo-admin::

	python manage.py migrate

3. Run server

How to use?
-----------

1. For example to record an error

	In the views.py::
		
		from log.utils import set_error_to_log

		def myview(request, pk):

			try:
				data = Model.object.get(id=pk)
			except Model.DoesNotExist:
				set_error_to_log(request, "The record in the model Model not exists")

	When occurs on error, go the administrator and visualize the record in the model.

2. For example, for get errors loaded on a date
	
	In the views.py::

		from log.utils import get_data_log

		def myview(request, pk):

			now = datetime.datetime.now()
			data = get_data_log('date', now)

	In this example, i'm getting errors from field date with the value now.

	Other field can be username.