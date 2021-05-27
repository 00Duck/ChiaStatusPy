import ChiaStatusClient as csc

class FullNodeClient(csc.ChiaStatusClient):
    def __init__(self) -> None:
        super().__init__()
        self.port = 8555
    
    def get_blockchain_state(self, body={}) -> dict: 
        return self.send("/get_blockchain_state", self.port, body)

    def get_block(self, body={}) -> dict: 
        return self.send("/get_block", self.port, body)

    def get_blocks(self, body={}) -> dict: 
        return self.send("/get_blocks", self.port, body) 

    def get_block_record_by_height(self, body={}) -> dict: 
        return self.send("/get_block_record_by_height", self.port, body)

    def get_block_record(self, body={}) -> dict: 
        return self.send("/get_block_record", self.port, body)
    
    def get_unfinished_block_headers(self, body={}) -> dict: 
        return self.send("/get_unfinished_block_headers", self.port, body)

    def get_network_space(self, body={}) -> dict: 
        return self.send("/get_network_space", self.port, body)

    def get_additions_and_removals(self, body={}) -> dict: 
        return self.send("/get_additions_and_removals", self.port, body)

    def get_initial_freeze_period(self, body={}) -> dict: 
        return self.send("/get_initial_freeze_period", self.port, body)

    def get_network_info(self, body={}) -> dict: 
        return self.send("/get_network_info", self.port, body)

    def get_coin_records_by_puzzle_hash(self, body={}) -> dict: 
        return self.send("/get_coin_records_by_puzzle_hash", self.port, body)

    def get_mempool_item_by_tx_id(self, body={}) -> dict: 
        return self.send("/get_mempool_item_by_tx_id", self.port, body)

    def get_all_mempool_items(self, body={}) -> dict: 
        return self.send("/get_all_mempool_items", self.port, body)

    def get_connections(self, body={}) -> dict: 
        return self.send("/get_connections", self.port, body)

    def open_connection(self, body={}) -> dict: 
        return self.send("/open_connection", self.port, body)

    def close_connection(self, body={}) -> dict: 
        return self.send("/close_connection", self.port, body)

    def stop_node(self, body={}) -> dict: 
        return self.send("/stop_node", self.port, body)