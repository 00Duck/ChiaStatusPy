import json
import OutboundClient
import FullNodeClient
import HarvesterClient
import WalletClient
import FarmerClient

def main():
    oc = OutboundClient.OutboundClient()
    fnc = FullNodeClient.FullNodeClient()
    hc = HarvesterClient.HarvesterClient()
    wc = WalletClient.WalletClient()
    #fc = FarmerClient.FarmerClient()

    status = {
        "farmer": {},
        "full_node": {},
        "harvester": {},
        "wallet": {}
    }

    status["full_node"]["get_blockchain_state"] = fnc.get_blockchain_state()
    status["full_node"]["get_network_info"] = fnc.get_network_info()
    status["full_node"]["get_connections"] = fnc.get_connections()

    status["wallet"]["get_sync_status"] = wc.get_sync_status({"wallet_id": 1})
    status["wallet"]["get_height_info"] = wc.get_height_info({"wallet_id": 1})
    status["wallet"]["get_wallet_balance"] = wc.get_wallet_balance({"wallet_id": 1})
    status["wallet"]["get_transactions"] = wc.get_transactions({"wallet_id": 1})
    status["wallet"]["get_next_address"] = wc.get_next_address({"wallet_id": 1, "new_address": False})
    status["wallet"]["get_transaction_count"] = wc.get_transaction_count({"wallet_id": 1})
    status["wallet"]["get_farmed_amount"] = wc.get_farmed_amount({"wallet_id": 1})

    status["harvester"]["get_plots"] = hc.get_plots()
    status["harvester"]["get_plot_directories"] = hc.get_plot_directories()

    resp = oc.send("POST", status)

    print(resp)

if __name__ == "__main__":
    main()