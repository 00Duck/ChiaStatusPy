import ChiaStatusClient as csc

class FarmerClient(csc.ChiaStatusClient):
    def __init__(self) -> None:
        super().__init__()
        self.port = 8559
    
    def get_signage_point(self, body={}) -> dict: 
        return self.send("/get_signage_point", self.port, body)

    def get_signage_points(self, body={}) -> dict: 
        return self.send("/get_signage_points", self.port, body)

    def get_reward_targets(self, body={}) -> dict: 
        return self.send("/get_reward_targets", self.port, body)

    def set_reward_targets(self, body={}) -> dict: 
        return self.send("/set_reward_targets", self.port, body)

    def get_connections(self, body={}) -> dict: 
        return self.send("/get_connections", self.port, body)

    def open_connection(self, body={}) -> dict: 
        return self.send("/open_connection", self.port, body)

    def close_connection(self, body={}) -> dict: 
        return self.send("/close_connection", self.port, body)

    def stop_node(self, body={}) -> dict: 
        return self.send("/stop_node", self.port, body)