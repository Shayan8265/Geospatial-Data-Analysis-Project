from classes import DatabaseConnection, Datacube

if __name__ == "__main__":
    # DatabaseConnection object
    dbc = DatabaseConnection("https://ows.rasdaman.org/rasdaman/ows")

    # Datacube object with the DatabaseConnection object
    dco = Datacube(dbc)

    # Example 1: finding the minimum of the AvgLandTemp datacube within a specified range
    datacube_name = "AvgLandTemp"
    subset_params = 'Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")'
    result1 = float(dco.min_datacube(datacube_name, subset_params))
    print("Example 1 Result:", result1)
    assert result1 == 2.2834647, "Example 1 test failed!"

    # Example 2: multiband data for a specific location
    lat = "234989.62194009003"
    long = "5816800.127894577999655"
    result2 = dco.d_multiband(lat, long, datacube="multiband")
    print("Example 2 Result:",  result2)
    assert result2 == "{ 7, 27, 146 }", "Example 2 test failed!"

    # Example 3: executing a average WCPS query to select a single value from the AvgLandTemp datacube
    custom_query = 'for $c in (AvgLandTemp) return avg($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])'
    result3 = float(dco._value(custom_query))
    print("Example 3 Result:", result3)
    assert result3 == 15.052493472894033, "Example 3 test failed!"
    
    # Example 4: executing a custom WCPS query to select a single value from the AvgLandTemp datacube
    custom_query = 'for $c in (AvgLandTemp) return $c[Lat(53.08), Long(8.80), ansi("2014-07")]'
    result4 = float(dco._value(custom_query))
    print("Example 4 Result:", result4)
    assert result4 == 25.984251, "Example 4 test failed!"

    # Example 5: csv
    custom_query = 'for $c in ( AvgLandTemp ) return encode($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")] , "text/csv")'
    result5 = dco._value(custom_query)
    print("Example 5 Result:", result5)
    assert result5 == "2.834646,4.488189,11.10236,20.19685,21.02362,21.29921,25.98425,24.33071,22.12598,16.06299,8.897637,2.283465", "Example 5 test failed!"

    # Example 6:Celsius to Kelvin csv
    query6 = 'for $c in (AvgLandTemp) return encode($c[Lat(63.8), Long(9.80), ansi("2014-01":"2014-12")] + 273.15, "text/csv")'
    result6 = dco._value(query6)
    print("Example 6 Result:", result6)
    assert result6 == "269.0948819160461,272.4019685029983,275.7090550899505,281.4964565277099,285.9059051513672,287.8350395202636,296.1027549743652,288.9374011993408,284.80354347229,278.4649604797363,275.1578740119934,269.3704723358154", "Example 6 test failed!"

    # Example 7: encoding AvgTemperatureColor data as PNG image for a specific date
    query = 'for $c in (AvgTemperatureColor) return encode($c[ansi("2015-07-01"),Lat(53.08:70), Lon(9.80:50)] , "image/png")'
    result7 = dco._value(query)
    
    if result7.startswith(b'\x89PNG'):
        with open('example_image.png', 'wb') as f:
            f.write(result7)
        print("Image saved successfully.")
    else:
        print("The result does not seem to be a PNG image.")


    print("All tests passed successfully!")
