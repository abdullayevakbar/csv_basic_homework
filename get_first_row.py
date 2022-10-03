def get_first_row(data):
    """
    Get the first row from a CSV file.
     Args:
         data(str): csv file.
     Return:
         list: First row.
    """
    x: list = []
    for i in data:
        x.append(i.split(',')[0])
    return x


data = open('data.csv')
data = data.split('\n')
print(get_first_row(data))

# Read the csv file
