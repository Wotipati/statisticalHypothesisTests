import csv
import argparse
import numpy as np
import pandas as pd
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

    table = []
    table_header = []
    for xi, group_x in enumerate(group_list):
        table_header.append(group_x.group_name)
        table_xi = []
        for y1 in range(xi+1):
            table_xi.append('-')
        for group_y in group_list[xi+1:]:
            # 対応ありt検定
            statistic, p_value = stats.ttest_rel(group_x.data_array,group_y.data_array)

            if(p_value<level):
                table_xi.append('*'+str(p_value))
            else:
                table_xi.append(str(p_value))

        table.append(table_xi)

    df = pd.DataFrame(table, index=table_header, columns=table_header)
    print(df)



if __name__ == '__main__':
    main()
