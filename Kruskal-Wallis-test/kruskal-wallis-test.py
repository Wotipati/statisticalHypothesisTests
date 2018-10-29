import csv
import argparse
import numpy as np
import scipy.stats as stats


class data_group:
    def __init__(self, group_name, data_array):
        self.group_name = group_name
        self.data_array = data_array


def data_reader(filename):
    group_list = []
    with open(filename, 'r') as r:
        data_reader = csv.reader(r)
        for row in data_reader:
            group_name = row[0]
            data_array = []
            for data in row[1:]:
                data_array.append(float(data))

            group_list.append(data_group(group_name,data_array))

    return group_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='testData.csv', help='path to the input csv file (default: testData.csv)')
    parser.add_argument('--level', type=float, default=0.05, help='level of significance (default: 0.05)')
    args     = parser.parse_args()
    filename = args.input
    level    = args.level

    group_list = data_reader(filename)

    data_list = []
    for group_xi in group_list:
        data_list.append(group_xi.data_array)
    data_array = np.array(data_list)

    statistic, p_value = stats.kruskal(*(data_array[i,:] for i in range(data_array.shape[0])))

    if(p_value<level):
        print('p-value = '+str(p_value)+'*')
    else:
        print('p-value = '+str(p_value))


if __name__ == '__main__':
    main()
