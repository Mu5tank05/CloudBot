import urllib3
import json
from cloudbot import hook

@hook.command(autohelp=False)
def sapn():
    urllib3.disable_warnings();
    http = urllib3.PoolManager()
    request = http.request('GET','https://outage.apps.sapowernetworks.com.au/OutageReport/AllCurrentOutages/?searchCriteria=&requireLatLong=false&AspxAutoDetectCookieSupport=1');
    data = json.loads(request.data.decode('utf-8'));
    request.release_conn();
    # print(data);
    data_str = str(data);
    for i in range(len(data)):
        return("Area affected: " + data[i]['suburb'] + " - " + " Customers Affected: " + data[i][
            'affected'] + " - " + "Approx Restoration Time: " + data[i]['restoration'] + " - " + "Cause: " + data[i][
                  'reason'] + " - " + "Status: " + data[i]['status']);
 