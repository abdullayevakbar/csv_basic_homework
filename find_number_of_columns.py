def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    data = data.split('\n')
    return len(data.split(','))


data = open('data.csv').read()
print(find_number_of_columns(y[0]))
# Read the csv file
