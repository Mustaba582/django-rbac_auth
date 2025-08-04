Backend
The backend of this project is composed of Python files, including models.py, views.py, urls.py, forms.py, manage.py, and settings.py. These files contain the server-side code and logic, which run on the server to process requests, manage data, and enforce rules.

settings.py: This file holds all the project's configuration, including the list of apps, paths for templates and static files, and security settings.

urls.py: This file contains the URL patterns for file routing, which tells Django which view function to call for a given URL.

models.py: In this file, database schemas are defined. CustomUser and Role are defined here with their properties, forming the backend data layer.

admin.py: This file uses Django’s admin module to help developers and site administrators create, update, and delete data without writing any queries. It imports custom models from models.py to manage them in the admin site. The decorators @admin.register(CustomUser) and @admin.register(Role) are used to register the CustomUser and Role models with the Django admin.

views.py: This file holds the functions and classes used to handle HTTP requests and render templates. It checks if the HTTP request is correct for each page and sends error messages if not. It contains the fundamentals of user authentication, with functions that use and validate forms, and the django.authenticate function to verify credentials. Decorators are used to ensure that only logged-in users can see a view and to enable logging out. It also holds functions for role-specific views.

forms.py: This file validates and processes data for the backend. It also contains metadata about the forms.
