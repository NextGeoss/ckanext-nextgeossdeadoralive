[![Build Status](https://travis-ci.org/ckan/ckanext-deadoralive.png)](https://travis-ci.org/ckan/ckanext-deadoralive) [![Coverage Status](https://img.shields.io/coveralls/ckan/ckanext-deadoralive.svg)](https://coveralls.io/r/ckan/ckanext-deadoralive?branch=master)
[![Latest Version](https://pypip.in/version/ckanext-deadoralive/badge.svg)](https://pypi.python.org/pypi/ckanext-deadoralive/)
[![Downloads](https://pypip.in/download/ckanext-deadoralive/badge.svg)](https://pypi.python.org/pypi/ckanext-deadoralive/)
[![Supported Python versions](https://pypip.in/py_versions/ckanext-deadoralive/badge.svg)](https://pypi.python.org/pypi/ckanext-deadoralive/)
[![Development Status](https://pypip.in/status/ckanext-deadoralive/badge.svg)](https://pypi.python.org/pypi/ckanext-deadoralive/)
[![License](https://pypip.in/license/ckanext-deadoralive/badge.svg)](https://pypi.python.org/pypi/ckanext-deadoralive/)


Ckanext-NextgeossDeadorAlive
============================

ckanext-nexgetossdeadoralive is a CKAN extension created used with [Dead or Alive link checker service](https://github.com/ckan/deadoralive).
It provides the API that enables a CKAN site to be checked by the link checker,
handles saving the results posted by the link checker in CKAN's database and
adds various broken link reports to the CKAN site. 
[Dead or Alive link checker service of NextGeoss](https://github.com/NextGeoss/ckanext-nextgeossdeadoralive).

Features and screenshots: [seanh.cc/posts/ckanext-deadoralive](http://seanh.cc/posts/ckanext-deadoralive/)  


Requirements
------------

Tested with CKAN 2.2 and Python 2.7. Python 2.6 is not supported!


Installation and Usage
----------------------

1. Activate your CKAN virtualenv and install the extension:

        . /usr/lib/ckan/default/bin/activate
        pip install -e git+https://github.com/NextGeoss/ckanext-nextgeossdeadoralive#egg=ckanext-nextgeossdeadoralive
        pip install -r https://raw.githubusercontent.com/NextGeoss/ckanext-nextgeossdeadoralive/master/dev-requirements.txt 

   To install the extension in docker add this in the docker file:

        RUN pip install -e git+https://github.com/NextGeoss/ckanext-nextgeossdeadoralive@v0.1.10#egg=ckanext-nextgeossdeadoralive
        RUN pip install -r https://raw.githubusercontent.com/NextGeoss/ckanext-nextgeossdeadoralive/master/dev-requirements.txt

2. Add `deadoralive` to the `ckan.plugins` setting in your CKAN config file.

3. Create a user account for the link checker to use.

   Before you can run the link checker service you need a CKAN user account
   for it to use. I recommend creating a new user account
   just for the link checker rather than using an admin account, so the link
   checker can run with as few privileges as possible.

   You can create a user account by registering a new account using CKAN's web
   interface, or by using [CKAN's command-line interface](http://docs.ckan.org/en/latest/maintaining/paster.html#user-create-and-manage-users).

   Once you've created the user account for the link checker, add this config
   setting to the `[app:main]` section of your CKAN config file:

        # The names of the users who're allowed to access the deadoralive
        # plugin's API to post link checker results.
        # The API key of one of these users must be passed to deadoralive.py
        # when you run it.
        ckanext.deadoralive.authorized_users = deadoralive

   (In this example `deadoralive` is the name of the CKAN user account we
   created, but you can call this account whatever you like.)

4. Now restart CKAN by restarting your web server. You should see the links to
   the broken link report pages appear on your site. At first they will report
   no broken links - because you haven't checked the site for broken links yet.

5. Now go over to [Dead or Alive](https://github.com/NextGeoss/nextgeoss-deadoralive) and
   install the link checker (either on the same machine where CKAN is installed
   or on a different machine - it doesn't matter). The API key that you
   configure the link checker with should be the API key of the user you
   created in step 3 above. Run the link checker against your CKAN site and
   you'll start to see broken link reports appear on the site.


Optional Config Settings
------------------------

In the `[app:main]` section of the CKAN config file:

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.deadoralive.recheck_resources_after = 24

    # The minimum number of hours to wait for a check result for a resource
    # to come back before timing out and giving the resource out again to
    # another link checker task (optional, default: 2).
    ckanext.deadoralive.resend_pending_resources_after = 2

    # The minimum number of times that checking a resource's link must fail
    # consecutively before we mark that resource as broken in CKAN.
    ckanext.deadoralive.broken_resource_min_fails = 3

    # The minimum number of hours that a resource's link must be broken for
    # before we mark that resource as broken in CKAN.
    ckanext.deadoralive.broken_resource_min_hours = 36


Development
-----------

To install the plugin for development, activate your CKAN virtualenv and do:

        git clone https://github.com/NextGeoss/ckanext-nextgeossdeadoralive.git
        cd ckanext-nextgeossdeadoralive
        python setup.py develop
        pip install -r dev-requirements.txt


Running the Tests
-----------

For the test it is used a junit test in python. The script located in unit_test tests the main functions for deadoralive:

        1. get_resources_to_check()
        2. get_url_for_id()

In the xml file you can see the results, the way to execute is very simple, just like a python:

        1. python test_unit_1.py
        2. Check the xml file
Api request implemented
-----------

For this extension it is been created a new api request that returns a data dict with information about the broken links:

        1. Report format:
           report = {
             "name" = organization_name,
             "resources_broken" = {
                "dataset_id",
                "resource_id",
                "resource_url"
             }
           }
        2. Call format: http://website/deadoralive/get_broken_links

Also it is possible to filter this query for an specific dataset:

        1. Call format: http://website/deadoralive/get_broken_links?dataset=<dataset_id>

