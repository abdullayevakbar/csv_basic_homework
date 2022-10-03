from webbrowser import get


def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """

    x: list = []
    for i in data:
        x.append(i.split(',')[0])
    return x


data = open('data.csv').read()
data = data.split('\n')
print(get_first_column(data))
# Read the csv file
