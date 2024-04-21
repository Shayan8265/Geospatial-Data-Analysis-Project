import requests

class DatabaseConnection:
    def __init__(self, server_url):
        self.server_url = server_url

    def execute_wcps_query(self, query):
        # Constructing the URL for executing WCPS query
        url = f"{self.server_url}"
        # Sending a POST request with the WCPS query data
        response = requests.post(url, data={'query': query})
        # Checking the response status
        if response.status_code == 200:
            # Checking if the response contains image data
            if response.headers['Content-Type'] == 'image/png':
                return response.content  # Return binary content for images
            else:
                return response.text  # Return text content for other types of data
        else:
            return f"Error: Failed to execute query. Status code {response.status_code}"

class Datacube:
    def __init__(self, dbc):
        self.dbc = dbc
        
    def min_datacube(self, datacube_name, subset_params):
        # Generating a WCPS query to find the minimum value within a subset of the datacube
        query = f"for $c in ({datacube_name}) return min($c[{subset_params}])"
        # Executing the query through the DatabaseConnection object
        return self.dbc.execute_wcps_query(query)
    
    def d_multiband(self, lat, long, datacube):
        # Generating a WCPS query to retrieve multiband data for a specific location
        query = f"for $c in ({datacube}) return $c[E({lat}), N({long})]"
        # Executing the query through the DatabaseConnection object
        return self.dbc.execute_wcps_query(query)
    
    def _value(self, query):
        # Executing a custom WCPS query through the DatabaseConnection object
        return self.dbc.execute_wcps_query(query)
    
    def encode_temp_color_image(self, date):
        # Generating a WCPS query to encode temperature color image data for a specific date
        query = f'for $c in (AvgTemperatureColor) return encode($c[ansi("{date}")], "image/png")'
        # Executing the query through the DatabaseConnection object
        return self.dbc.execute_wcps_query(query)


