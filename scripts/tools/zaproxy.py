import time
from pprint import pprint
from zapv2 import ZAPv2

APIKEY = 'fookey'

target = 'http://localhost:3000'
zap = ZAPv2(apikey=APIKEY, proxies={'http': 'http://0.0.0.0:8090'})

print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)

print('Active Scan completed')
# Print vulnerabilities found by the scanning
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target))
