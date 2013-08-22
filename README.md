ckanext-profile
===============


Add profiling to CKAN using [repoze.profile](https://pypi.python.org/pypi/repoze.profile).

This adds a web page to `/__profile__` where you can view profiling data, and
also outputs the same data to two files in your CKAN directory:

1. `profiling.log`, which can be analyzed with the
   [Python standard library's profilers](http://docs.python.org/2/library/profile.html)
   (specifically, the [Stats class](docs.python.org/2/library/profile.html#the-stats-class)
   can be used to analyze the data)

2. `cachegrind.out`, which can be analyzed using the
   [KCachegrind](http://kcachegrind.sourceforge.net/html/Home.html) app

See <http://docs.repoze.org/profile/> for more documentation.


Installation
------------

Activate your CKAN virtualenv, then run:

    pip install -e git+https://github.com/seanh/ckanext-profile.git#egg=ckanext-profile
