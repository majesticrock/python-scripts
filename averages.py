import numpy as np

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def average(pathToFile, delimiter=";"):
    content = csv_read(pathToFile, delimiter)
    n = len(content)
    #Set this to the line where your values start
    #remember that arrays start at 0 not at 1
    first_index = 1
    #Set this to the column where your values are
    col = 0
    avg = 0
    avg_err = 0

    for i in range(first_index, n):
        avg += float(content[i][col])
    
    avg /= (n-first_index)

    for i in range(first_index, n):
        avg_err += (float(content[i][col]) - avg)**2

    avg_err = np.sqrt(avg_err)
    avg_err /= np.sqrt((n-first_index) * (n-1-first_index))

    return [avg, avg_err]
