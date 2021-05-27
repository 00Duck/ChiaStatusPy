import ChiaStatusClient as csc

class HarvesterClient(csc.ChiaStatusClient):
    def __init__(self) -> None:
        super().__init__()
        self.port = 8560
    
    def get_plots(self, body={}) -> dict: 
        return self.send("/get_plots", self.port, body)

    def refresh_plots(self, body={}) -> dict: 
        return self.send("/refresh_plots", self.port, body)

    def delete_plot(self, body={}) -> dict: 
        return self.send("/delete_plot", self.port, body)

    def add_plot_directory(self, body={}) -> dict: 
        return self.send("/add_plot_directory", self.port, body)

    def get_plot_directories(self, body={}) -> dict: 
        return self.send("/get_plot_directories", self.port, body)

    def remove_plot_directory(self, body={}) -> dict: 
        return self.send("/remove_plot_directory", self.port, body)

    def get_connections(self, body={}) -> dict: 
        return self.send("/get_connections", self.port, body)

    def open_connection(self, body={}) -> dict: 
        return self.send("/open_connection", self.port, body)

    def close_connection(self, body={}) -> dict: 
        return self.send("/close_connection", self.port, body)

    def stop_node(self, body={}) -> dict: 
        return self.send("/stop_node", self.port, body)
