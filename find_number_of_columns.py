def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    data = data.split('\n')[0].split(',')
    return len(data)


data = open('data.csv').read()
print(find_number_of_columns(data))
# Read the csv file
