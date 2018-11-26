## Passive DNS for Scapy
![AppVeyor](https://img.shields.io/appveyor/ci/:user/:repo.svg)
![Chocolatey](https://img.shields.io/chocolatey/dt/scriptcs.svg) 
![GitHub followers](https://img.shields.io/github/followers/espadrine.svg?label=Follow&style=social)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Monitors network for malicious activities domain

### Install
```
➜  ~ git clone https://github.com/xl7dev/pdns.git
➜  ~ pip install -r requirements.txt
```

### Using
1. Create Database and table
```
➜  ~ mysql -u root -p < pdns.sql
```
2. Run
```
➜  ~ python pdns.py
```
3. SELECT Mysql
```
➜  ~ mysql -h localhost -uroot -p
```
mysql> select * from pdns.pdns limit 10;
```
+----+----------------------------------------------------------+-------+----------------------------------------------------------+-------+---------------------+---------------------+
| id | name                                                     | type  | value                                                    | count | first               | last                |
+----+----------------------------------------------------------+-------+----------------------------------------------------------+-------+---------------------+---------------------+
|  1 | e13678.ca.s.tl88.net                                     | A     | 210.192.117.42                                           |    30 | 2018-11-26 18:25:21 | 2018-11-26 19:37:00 |
|  2 | google.com                                               | A     | 216.58.203.46                                            |     1 | 2018-11-26 18:25:23 | 2018-11-26 18:25:23 |
|  3 | ghostery-collector.ghostery.com                          | CNAME | ghostery-collector-115893389.us-east-1.elb.amazonaws.com |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
|  4 | ghostery-collector-115893389.us-east-1.elb.amazonaws.com | A     | 18.215.73.7                                              |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
|  5 | ghostery-collector-115893389.us-east-1.elb.amazonaws.com | A     | 34.236.105.245                                           |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
|  6 | ghostery-collector-115893389.us-east-1.elb.amazonaws.com | A     | 54.210.208.21                                            |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
|  7 | www.microsoft.com-c-3.edgekey.net.globalredir.akadns.net | CNAME | e13678.ca.s.tl88.net                                     |     9 | 2018-11-26 18:26:23 | 2018-11-26 19:33:36 |
|  9 | img.shields.io                                           | A     | 172.64.165.12                                            |     5 | 2018-11-26 18:37:24 | 2018-11-26 19:24:39 |
| 10 | img.shields.io                                           | A     | 172.64.164.12                                            |     5 | 2018-11-26 18:37:24 | 2018-11-26 19:24:39 |
| 11 | e13678.ca.s.tl88.net                                     | A     | 221.230.147.106                                          |     4 | 2018-11-26 18:37:36 | 2018-11-26 18:48:02 |
+----+----------------------------------------------------------+-------+----------------------------------------------------------+-------+---------------------+---------------------+
```
mysql> select * from pdns.pdns where reverse(name) like reverse('%.amazonaws.com');
```
+-----+--------------------------------------------------------------------+------+----------------+-------+---------------------+---------------------+
| id  | name                                                               | type | value          | count | first               | last                |
+-----+--------------------------------------------------------------------+------+----------------+-------+---------------------+---------------------+
|   4 | ghostery-collector-115893389.us-east-1.elb.amazonaws.com           | A    | 18.215.73.7    |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
|   5 | ghostery-collector-115893389.us-east-1.elb.amazonaws.com           | A    | 34.236.105.245 |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
|   6 | ghostery-collector-115893389.us-east-1.elb.amazonaws.com           | A    | 54.210.208.21  |     9 | 2018-11-26 18:26:14 | 2018-11-26 19:36:14 |
| 325 | offers-api-production-lb-1981944578.eu-central-1.elb.amazonaws.com | A    | 18.195.105.102 |     2 | 2018-11-26 19:00:27 | 2018-11-26 19:02:39 |
| 326 | offers-api-production-lb-1981944578.eu-central-1.elb.amazonaws.com | A    | 54.93.141.203  |     2 | 2018-11-26 19:00:27 | 2018-11-26 19:02:39 |
| 327 | offers-api-production-lb-1981944578.eu-central-1.elb.amazonaws.com | A    | 52.59.13.6     |     2 | 2018-11-26 19:00:27 | 2018-11-26 19:02:39 |
| 328 | offers-api-production-lb-1981944578.eu-central-1.elb.amazonaws.com | A    | 52.57.68.28    |     2 | 2018-11-26 19:00:27 | 2018-11-26 19:02:39 |
| 344 | cmp-server-493810428.us-east-1.elb.amazonaws.com                   | A    | 52.6.227.218   |     1 | 2018-11-26 19:01:14 | 2018-11-26 19:01:14 |
| 345 | cmp-server-493810428.us-east-1.elb.amazonaws.com                   | A    | 34.197.200.72  |     1 | 2018-11-26 19:01:14 | 2018-11-26 19:01:14 |
| 352 | ghostery-sign-1030905311.us-east-1.elb.amazonaws.com               | A    | 52.206.67.11   |     1 | 2018-11-26 19:01:19 | 2018-11-26 19:01:19 |
| 353 | ghostery-sign-1030905311.us-east-1.elb.amazonaws.com               | A    | 34.234.51.143  |     1 | 2018-11-26 19:01:19 | 2018-11-26 19:01:19 |
+-----+--------------------------------------------------------------------+------+----------------+-------+---------------------+---------------------+
```
### Mac OSX System launchctl
```
➜  ~ bash launchctl.sh
```
