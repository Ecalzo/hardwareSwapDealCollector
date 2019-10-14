# HardwareSwap DealCollector
##  Getting Started
DealCollector will check reddit.com/r/hardwareswap for new deals with your specified keywords every two minutes. Deals will be written to the command line and appended to a 'deals.csv' file. DealCollector can be set up to send you texts via Twilio.

To fire up an instance of deal collector bot with a `config.py` file, use the following syntax:
```shell
python main.py -C True -k iphone -k keyboard -k 'mechanical keyboard'
```

If you do not want to save your credentials as plaintext:
```shell
python main.py -ID CLIENT_ID -SCRT CLIENT_SECRET -UN REDDIT_USERNAME -PW REDDIT_PASSWORD -k iphone -k keyboard -k 'mechanical keyboard'
```

## Using Twilio
Twilio support is available to send you texts if you have a Twilio account or trial account
* Twilio credentials MUST be passed via the config.py file
* use the `--twilio True` flag to indicate that you have Twilio credentials you would like to use

```shell
python main.py -C True --twilio True -k iphone -k keyboard -k 'mechanical keyboard'
```

## config.py
An example `config.py` file is provided in the repo. It looks like this:

```python
CLIENT_ID = ''
CLIENT_SECRET = ''
REDDIT_USERNAME = ''
REDDIT_PASSWORD = ''
TWILIO_SID = ''
TWILIO_AUTH = ''
TWILIO_NUMBER = ''
MY_NUMBER = ''
```