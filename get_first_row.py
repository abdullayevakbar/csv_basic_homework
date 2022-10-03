def get_first_row(data):
    """
    Get the first row from a CSV file.
     Args:
         data(str): csv file.
     Return:
         list: First row.
    """
    data.split('\n')
    return data[1].split(',')


data = open('data.csv').read()
print(get_first_row(data))

# Read the csv file
