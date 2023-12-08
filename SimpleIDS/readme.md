# Simple IDS
_when I say simple, believe me its very simple script used to filter out fishy IPs._

> I say so because the API, "[_fraudsentinel_](https://rapidapi.com/fraudsentinel-ltd-fraudsentinel-ltd-default/api/fraudsentinel)" seems to be not ACCURATE all the times and above all, only depending on this script is not Preferable.

**Use simpleIDS as basic FILTERING of IPS.** 
if you're smart to find this small script, in this vast town. You must be intelligent enough in Implemting/Executing the script also. make sure you use the API key, or else wont work, You know right!!  

###### You can use either ways:
1. Direct-Class-SingleIP
```Python
CheckThisIP('91.92.249.48') # constructor overloading
# this works
```
1. 1 Direct-Class-IPlist
```Python
ipList = ['103.255.190.123', '103.207.4.222']
CheckThisIP(ipList)
```

2. .isOk() method
```Python
chkObj = CheckThisIP()
chkObj.CHK_IP='188.132.232.227' 
chkObj.isOk()
```
2. 1 .isOk loop method
```Python
ipList = ['103.255.190.123', '103.207.4.222']
chkObj = CheckThisIP()
for ip in ipList:
	chkObj.CHK_IP = ip
	chkObj.isOk()
```
---
*note: version 0.1, not stable. You may expect some crashes.*