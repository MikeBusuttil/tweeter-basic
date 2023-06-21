from datetime import datetime

def stderr(*output):
    with open('/proc/1/fd/1', 'a') as f:
        print(datetime.now().strftime("[%d-%b-%y %I:%M:%S %p]"), *output, file=f)
