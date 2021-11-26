# python-idmef-tests

A bunch of test scripts using Python IDMEF libraries 

## Setup

It is highly recommended to use a Python virtualenv.

If you don't have Python virtualenv installed:a

```
apt intall python3-virtualenv
```

Then:

```
# create the virtualenv
mkdir ~/virtualenv
virtualenv ~/virtualenv/idmef
# and activate it
source ~/virtualenv/idmef/bin/activate
# clone some github repos
cd ~/WHEREEVERYOUWANT
mkdir SECEF
(cd SECEF ; git clone git@github.com:SECEF/idmefv2-definition.git)
(cd SECEF ; git clone git@github.com:SECEF/python-idmefv2.git)
(cd SECEF ; git clone git@github.com:SECEF/python-idmefv2-transport.git)
# install them
(cd SECEF/python-idmefv2.git; python setup.py install)
(cd SECEF/python-idmefv2-transport.git; python setup.py install)
# and add missing link
(cd ~/virtualenv/idmef/lib/python3.8/site-packages/idmefv2-0.0.0-py3.8.egg/idmefv2/schemas ; ln -s ~/WHEREEVERYOUWANT/SECEF/idmefv2-definition/IDMEFv2.schema 
```

## Tests

### First message test

```
python3 message.py
```

should output:
```
The message is valid
The message is valid
```
