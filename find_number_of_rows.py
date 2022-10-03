def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    return len(data.split('\n'))


data = open('data.csv').read()
print(find_number_of_rows(data))

# Read the csv file
