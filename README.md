# ChiaStatusPy

Sends status information from the Chia blockchain to the specified host/endpoint. The information collected is an arbitrary selection of endpoints available in the blockchain as of 1.1.5. This script is designed to be installed on a server with the chia blockchain and run via crontab or some other scheduled service.

The output of this program is a single JSON object (sent to your specified endpoint) organizing the various data that can be collected. Here's an example of the structure:

```
{
    "farmer": {},
    "full_node": {
        "get_blockchain_state": {...},
        "get_network_info": {...}
        ...
    },
    "harvester": {
        "get_plots": {...},
        "get_plot_directories": {...},
        ...
    },
    "wallet": {
        "get_sync_status": {...},
        "get_wallet_balance": {...}
        ...
    }
}
````

## Installation
Navigate to an installation location:

`cd /opt`

Install by cloning this repository

`git clone https://github.com/00Duck/ChiaStatusPy`

Navigate to the config.ini file. Ensure your cert file and key file path is correct. Enter in host, endpoint, and user/password credentials for basic auth communication:

`cd ChiaStatusPy/`

`nano config.ini`

Config example:

```
[chiaclient]
cert_file = ~/.chia/mainnet/config/ssl/wallet/private_wallet.crt
key_file = ~/.chia/mainnet/config/ssl/wallet/private_wallet.key

[outboundclient]
host = myhostname.com
endpoint = /api/my/awesome/endpoint
user = myusername
password = my super secret password
```
Note that the HTTP/HTTPS protocols should NOT be specified in the .ini file. Also, there is no need to add quotes if your password contains spaces.

Save and close the config file.

Test the script to ensure your credentials were entered correctly:

`python3 main.py`

Add a crontab to schedule the script to run:

`crontab -e`

If you would like to run this script every 10 minutes, it may look like this:

`*/10 * * * * /usr/bin/python3 /opt/ChiaStatusPy/main.py`
