def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    aw = []
    csv_data = data.split("\n")
    for i in csv_data:
        aw.append(i.split(",")[1])
    return aw


# Read the csv file
data = open('data.csv').read()
print(get_first_column(data))
