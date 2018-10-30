import csv
import argparse
import numpy as np
import scipy.stats as stats


class data_group:
    def __init__(self, group_name, data_array):
        self.group_name = group_name
        self.data_array = data_array
        self.mean       = np.mean(np.array(data_array))
        self.sem        = stats.sem(np.array(data_array))
        self.sd         = np.std(np.array(data_array))


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
    parser.add_argument('--confidence', type=float, default=0.95, help='level of significance (default: 0.95)')
    args       = parser.parse_args()
    filename   = args.input
    confidence = args.confidence

    group_list = data_reader(filename)

    for group_xi in group_list:
        print(group_xi.group_name)
        # 自由度
        df = len(group_xi.data_array) - 1

        chi2_under, chi2_upper = stats.chi2.interval(alpha=confidence, df=df)
        variance = group_xi.sd*group_xi.sd
        interval_under = df*variance / chi2_upper
        interval_upper = df*variance / chi2_under
        print('mean: {}, variance: {}, SD: {}'.format(group_xi.mean, variance, group_xi.sd))
        print('{}% confidence interval: ({}, {})'.format(int(confidence*100),interval_under,interval_upper))
        print(" ")




if __name__ == '__main__':
    main()
