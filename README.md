```
vagrant@arkham:~/projects/exchange/influxdb$ tox
py35 installed: appdirs==1.4.0,influxdb==4.0.0,nose==1.3.7,packaging==16.8,pyparsing==2.1.10,python-dateutil==2.6.0,pytz==2016.10,requests==2.13.0,six==1.10.0,-e git+git@github.com:StackStorm/st2.git@c35d8b64e69437a63cb424fe01df11ae82fb5c4f#egg=st2forge&subdirectory=st2forge
py35 runtests: PYTHONHASHSEED='3098443138'
py35 runtests: commands[0] | nosetests -sv tests/unit
test_instance_bad_hosts_value (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_instance_bad_port_value (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_instance_default (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_instance_with_config (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_logging (tests.unit.test_write_points.WritePointsActionTest) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.006s

OK
py27 installed: appdirs==1.4.0,influxdb==4.0.0,nose==1.3.7,packaging==16.8,pyparsing==2.1.10,python-dateutil==2.6.0,pytz==2016.10,requests==2.13.0,six==1.10.0,-e git+git@github.com:StackStorm/st2.git@c35d8b64e69437a63cb424fe01df11ae82fb5c4f#egg=st2forge&subdirectory=st2forge
py27 runtests: PYTHONHASHSEED='3098443138'
py27 runtests: commands[0] | nosetests -sv tests/unit
test_instance_bad_hosts_value (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_instance_bad_port_value (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_instance_default (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_instance_with_config (tests.unit.test_write_points.WritePointsActionTest) ... ok
test_logging (tests.unit.test_write_points.WritePointsActionTest) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
pep8 installed: appdirs==1.4.0,astroid==1.4.9,backports.functools-lru-cache==1.3,configparser==3.5.0,enum34==1.1.6,flake8==3.3.0,isort==4.2.5,lazy-object-proxy==1.2.2,mccabe==0.6.1,packaging==16.8,pycodestyle==2.3.1,pyflakes==1.5.0,pylint==1.6.5,pyparsing==2.1.10,six==1.10.0,-e git+git@github.com:StackStorm/st2.git@c35d8b64e69437a63cb424fe01df11ae82fb5c4f#egg=st2forge&subdirectory=st2forge,wrapt==1.10.8
pep8 runtests: PYTHONHASHSEED='3098443138'
pep8 runtests: commands[0] | /bin/bash -c \find ./actions -iname *.py | xargs pylint -E --rcfile=/home/vagrant/projects/exchange/influxdb/.pylintrc\
pep8 runtests: commands[1] | /bin/bash -c \find ./actions -iname *.py | xargs flake8 --config /home/vagrant/projects/exchange/influxdb/.flake8\
______________________________________________________ summary _______________________________________________________
  py35: commands succeeded
  py27: commands succeeded
  pep8: commands succeeded
  congratulations :)
```
