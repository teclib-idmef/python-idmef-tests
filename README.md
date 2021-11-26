# python-idmef-tests

A bunch of test scripts using Python IDMEF libraries 

## Setup

It is **highly recommended** to use a Python virtualenv.

If you don't have Python virtualenv installed:

```
apt install python3-virtualenv
```

Then:

```
# create the virtualenv root if needed
[ ! -d ~/virtualenv ] && mkdir ~/virtualenv
virtualenv ~/virtualenv/idmef

# and activate it
source ~/virtualenv/idmef/bin/activate

# if needed, create root directory for IDMEF repositories, wherever you want
[ ! -d ~/WHEREEVERYOUWANT ] && mkdir ~/WHEREEVERYOUWANT
cd ~/WHEREEVERYOUWANT

# then clone some github repos
mkdir SECEF
( cd SECEF ; git clone git@github.com:SECEF/idmefv2-definition.git )
( cd SECEF ; git clone git@github.com:SECEF/python-idmefv2.git )
( cd SECEF ; git clone git@github.com:SECEF/python-idmefv2-transport.git )

# install them in your virtualenv
( cd SECEF/python-idmefv2.git; python setup.py install )
( cd SECEF/python-idmefv2-transport.git; python setup.py install )

# and add missing link (adapt the directory according to your Python version)
( cd ~/virtualenv/idmef/lib/python3.8/site-packages/idmefv2-0.0.0-py3.8.egg/idmefv2/schemas ; ln -s ~/WHEREEVERYOUWANT/SECEF/idmefv2-definition/IDMEFv2.schema )
```

## Tests

### First message test


```
# first activate your virtualenv
source ~/virtualenv/idmef/bin/activate

# launch the script
python3 message.py
```

This should output:

```
The message is valid
The message is valid
```
