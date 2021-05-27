import ChiaStatusClient as csc

class WalletClient(csc.ChiaStatusClient):
    def __init__(self) -> None:
        super().__init__()
        self.port = 9256
    
    def log_in(self, body={}) -> dict: 
        return self.send("/log_in", self.port, body)

    def get_public_keys(self, body={}) -> dict: 
        return self.send("/get_public_keys", self.port, body)

    def get_private_key(self, body={}) -> dict: 
        return self.send("/get_private_key", self.port, body)

    def generate_mnemonic(self, body={}) -> dict: 
        return self.send("/generate_mnemonic", self.port, body)

    def add_key(self, body={}) -> dict: 
        return self.send("/add_key", self.port, body)

    def delete_key(self, body={}) -> dict: 
        return self.send("/delete_key", self.port, body)

    def delete_all_keys(self, body={}) -> dict: 
        return self.send("/delete_all_keys", self.port, body)

    def get_sync_status(self, body={}) -> dict: 
        return self.send("/get_sync_status", self.port, body)

    def get_height_info(self, body={}) -> dict: 
        return self.send("/get_height_info", self.port, body)

    def farm_block(self, body={}) -> dict: 
        return self.send("/farm_block", self.port, body)

    def get_initial_freeze_period(self, body={}) -> dict: 
        return self.send("/get_initial_freeze_period", self.port, body)

    def get_network_info(self, body={}) -> dict: 
        return self.send("/get_network_info", self.port, body)

    def get_wallets(self, body={}) -> dict: 
        return self.send("/get_wallets", self.port, body)

    def create_new_wallet(self, body={}) -> dict: 
        return self.send("/create_new_wallet", self.port, body)

    def get_wallet_balance(self, body={}) -> dict: 
        return self.send("/get_wallet_balance", self.port, body)

    def get_transaction(self, body={}) -> dict: 
        return self.send("/get_transaction", self.port, body)

    def get_transactions(self, body={}) -> dict: 
        return self.send("/get_transactions", self.port, body)

    def get_next_address(self, body={}) -> dict: 
        return self.send("/get_next_address", self.port, body)

    def send_transaction(self, body={}) -> dict: 
        return self.send("/send_transaction", self.port, body)

    def create_backup(self, body={}) -> dict: 
        return self.send("/create_backup", self.port, body)

    def get_transaction_count(self, body={}) -> dict: 
        return self.send("/get_transaction_count", self.port, body)

    def get_farmed_amount(self, body={}) -> dict: 
        return self.send("/get_farmed_amount", self.port, body)

    def get_connections(self, body={}) -> dict: 
        return self.send("/get_connections", self.port, body)

    def open_connection(self, body={}) -> dict: 
        return self.send("/open_connection", self.port, body)

    def close_connection(self, body={}) -> dict: 
        return self.send("/close_connection", self.port, body)

    def stop_node(self, body={}) -> dict: 
        return self.send("/stop_node", self.port, body)