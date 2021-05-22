"""
Reference https://github.com/Chia-Network/chia-blockchain/wiki/RPC-Interfaces
    DAEMON = 55400
    FULL_NODE = 8555
    FARMER = 8559
    HARVESTER = 8560
    WALLET =  9256

"""
class Endpoint:
    def __init__(self, ep: str, port: int) -> None:
        self.endpoint = ep
        self.port = port

FULL_NODE = {
    "get_blockchain_state": Endpoint("/get_blockchain_state", 8555),
    "get_block": Endpoint("/get_block", 8555),
    "get_blocks": Endpoint("/get_blocks", 8555),
    "get_block_record_by_height": Endpoint("/get_block_record_by_height", 8555),
    "get_block_record": Endpoint("/get_block_record", 8555),
    "get_unfinished_block_headers": Endpoint("/get_unfinished_block_headers", 8555),
    "get_network_space": Endpoint("/get_network_space", 8555),
    "get_additions_and_removals": Endpoint("/get_additions_and_removals", 8555),
    "get_initial_freeze_period": Endpoint("/get_initial_freeze_period", 8555),
    "get_network_info": Endpoint("/get_network_info", 8555),
    "get_coin_records_by_puzzle_hash": Endpoint("/get_coin_records_by_puzzle_hash", 8555),
    "get_mempool_item_by_tx_id": Endpoint("/get_mempool_item_by_tx_id", 8555),
    "get_all_mempool_items": Endpoint("/get_all_mempool_items", 8555),
    "get_connections": Endpoint("/get_connections", 8555),
    "open_connection": Endpoint("/open_connection", 8555),
    "close_connection": Endpoint("/close_connection", 8555),
    "stop_node": Endpoint("/stop_node", 8555)
}

WALLET = {
    "log_in": Endpoint("/log_in", 9256),
    "get_public_keys": Endpoint("/get_public_keys", 9256),
    "get_private_key": Endpoint("/get_private_key", 9256),
    "generate_mnemonic": Endpoint("/generate_mnemonic", 9256),
    "add_key": Endpoint("/add_key", 9256),
    "delete_key": Endpoint("/delete_key", 9256),
    "delete_all_keys": Endpoint("/delete_all_keys", 9256),
    "get_sync_status": Endpoint("/get_sync_status", 9256),
    "get_height_info": Endpoint("/get_height_info", 9256),
    "farm_block": Endpoint("/farm_block", 9256),
    "get_initial_freeze_period": Endpoint("/get_initial_freeze_period", 9256),
    "get_network_info": Endpoint("/get_network_info", 9256),
    "get_wallets": Endpoint("/get_wallets", 9256),
    "create_new_wallet": Endpoint("/create_new_wallet", 9256),
    "get_wallet_balance": Endpoint("/get_wallet_balance", 9256),
    "get_transaction": Endpoint("/get_transaction", 9256),
    "get_transactions": Endpoint("/get_transactions", 9256),
    "get_next_address": Endpoint("/get_next_address", 9256),
    "send_transaction": Endpoint("/send_transaction", 9256),
    "create_backup": Endpoint("/create_backup", 9256),
    "get_transaction_count": Endpoint("/get_transaction_count", 9256),
    "get_farmed_amount": Endpoint("/get_farmed_amount", 9256),
    "get_connections": Endpoint("/get_connections", 9256),
    "open_connection": Endpoint("/open_connection", 9256),
    "close_connection": Endpoint("/close_connection", 9256),
    "stop_node": Endpoint("/stop_node", 9256)
}

HARVESTER = {
    "get_plots": Endpoint("/get_plots", 8560),
    "refresh_plots": Endpoint("/refresh_plots", 8560),
    "delete_plot": Endpoint("/delete_plot", 8560),
    "add_plot_directory": Endpoint("/add_plot_directory", 8560),
    "get_plot_directories": Endpoint("/get_plot_directories", 8560),
    "remove_plot_directory": Endpoint("/remove_plot_directory", 8560),
    "get_connections": Endpoint("/get_connections", 8560),
    "open_connection": Endpoint("/open_connection", 8560),
    "close_connection": Endpoint("/close_connection", 8560),
    "stop_node": Endpoint("/stop_node", 8560)
}

FARMER = {
    "get_signage_point": Endpoint("/get_signage_point", 8559),
    "get_signage_points": Endpoint("/get_signage_points", 8559),
    "get_reward_targets": Endpoint("/get_reward_targets", 8559),
    "set_reward_targets": Endpoint("/set_reward_targets", 8559),
    "get_connections": Endpoint("/get_connections", 8559),
    "open_connection": Endpoint("/open_connection", 8559),
    "close_connection": Endpoint("/close_connection", 8559),
    "stop_node": Endpoint("/stop_node", 8559)
}
