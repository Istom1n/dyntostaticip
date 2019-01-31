## Auto-changer of dynamic IP in DNS service

Change A record for you domain if your IP address was dynamic.
Tested on Xiaomi Mini and NS1 DNS platform.

> „Why? Because.” ©

DDNS for capitalists!!!

![Scheme](https://i.ibb.co/f4HLgY4/dyntostatip.png)

```bash
~# git clone git@github.com:Istom1n/dyntostaticip.git
~# cd dyntostaticip/
~# pipenv install
~# pipenv run python dyntostaticip.py [MIWIFI_PASS] [NS1_API] [DOMAIN_FOR_UPDATE]
    - [MIWIFI_PASS] - Password from 192.168.31.1 exp. 'password'
    - [NS1_API] - NS1.com API from acoount settings exp. 'qy3gpa27zCXoqscKB'
    - [DOMAIN_FOR_UPDATE] - Domain for update A record exp. 'server.example.com'

Optput:
    Getting new IP address:
    120.150.121.57
    Updating A record on DNS server
    A record updated successfully!
```

### Create daemon with chech in every 30 minutes

1. Create a task in cron `crontab -e` (opens config file)
2. Write line, something like  
   `30 * * * * cd dyntostaticip/ && pipenv run python dyntostaticip.py [MIWIFI_PASS] [NS1_API] [DOMAIN_FOR_UPDATE]`

Example:
`30 * * * * cd dyntostaticip/ && pipenv run python dyntostaticip.py password qy3gpa27zCXoqscKB server.example.com`

3. Save & Qit from file.
4. ???
5. Profit, you have access to you personal computer in any moment!!!
