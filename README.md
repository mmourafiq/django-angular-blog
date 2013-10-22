django-angular-blog
===================

A blog app with django-rest-framework and angularjs.


N.B : if you get this error :

"ImportError: Could not import settings 'blog.settings' (Is it on sys.path?): No module named local_setting".

You should copy the local_setting from blog/templates and update with the correct values.

`> cp blog/templates/template_local_settings.py blog/blog/local_settings.py`

For more details : 

[[part1]](http://blog.mourafiq.com/post/55034504632/end-to-end-web-app-with-django-rest-framework)
[[part2]](http://blog.mourafiq.com/post/55099429431/end-to-end-web-app-with-django-rest-framework)
[[part3]](http://blog.mourafiq.com/post/58725341511/end-to-end-web-app-with-django-rest-framework)
[[part4]](http://blog.mourafiq.com/post/58726121556/end-to-end-web-app-with-django-rest-framework)
