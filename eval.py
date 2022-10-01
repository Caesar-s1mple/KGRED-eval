import numpy as np
import pandas as pd
import argparse


def micro_f1(pred, label, neg):
    total = len(pred)
    correct_positive = 0
    pred_positive = 0
    gold_positive = 0
    for i in range(total):
        golden = label[i]
        if golden == pred[i]:
            if golden != neg:
                correct_positive += 1
        if golden != neg:
            gold_positive += 1
        if pred[i] != neg:
            pred_positive += 1
    try:
        micro_p = float(correct_positive) / float(pred_positive)
    except:
        micro_p = 0
    try:
        micro_r = float(correct_positive) / float(gold_positive)
    except:
        micro_r = 0
    try:
        micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r)
    except:
        micro_f1 = 0
    result = {'micro_p': micro_p, 'micro_r': micro_r, 'micro_f1': micro_f1}
    return result



def parse_():
    parser = argparse.ArgumentParser()

    parser.add_argument('--test-file', type=str)
    parser.add_argument('--NA', type=str, default='')

    return parser.parse_args()


def main():
    args = parse_()

    result = pd.read_csv(args.test_file, na_filter=None, dtype=str)
    label = result.iloc[:, 2]
    pred = result.iloc[:, 3]

    res = micro_f1(pred, label, args.NA)

    print(res)


if __name__ == '__main__':
    main()
