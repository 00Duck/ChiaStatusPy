import ChiaStatusClient as cclient
import OutboundClient as outclient
import Endpoints as ep

def main():
    csc = cclient.ChiaStatusClient()
    oc = outclient.OutboundClient()

    status = {
        "farmer": {},
        "full_node": {},
        "harvester": {},
        "wallet": {}
    }

    status["full_node"]["get_blockchain_state"] = csc.req(ep.FULL_NODE["get_blockchain_state"])
    status["full_node"]["get_network_info"] = csc.req(ep.FULL_NODE["get_network_info"])
    status["full_node"]["get_connections"] = csc.req(ep.FULL_NODE["get_connections"])
    
    status["wallet"]["get_sync_status"] = csc.req(ep.WALLET["get_sync_status"], {"wallet_id": 1})
    status["wallet"]["get_height_info"] = csc.req(ep.WALLET["get_height_info"], {"wallet_id": 1})
    status["wallet"]["get_wallet_balance"] = csc.req(ep.WALLET["get_wallet_balance"], {"wallet_id": 1})
    status["wallet"]["get_transactions"] = csc.req(ep.WALLET["get_transactions"], {"wallet_id": 1})
    status["wallet"]["get_next_address"] = csc.req(ep.WALLET["get_next_address"], {"wallet_id": 1, "new_address": False})
    status["wallet"]["get_transaction_count"] = csc.req(ep.WALLET["get_transaction_count"], {"wallet_id": 1})
    status["wallet"]["get_farmed_amount"] = csc.req(ep.WALLET["get_farmed_amount"], {"wallet_id": 1})

    status["harvester"]["get_plots"] = csc.req(ep.HARVESTER["get_plots"])
    status["harvester"]["get_plot_directories"] = csc.req(ep.HARVESTER["get_plot_directories"])

    resp = oc.send("POST", status)
    print(resp)

if __name__ == "__main__":
    main()