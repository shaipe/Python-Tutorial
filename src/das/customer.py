# -*- encoding: utf-8 -*-

import pandas as pd
from datetime import datetime
from xpf import str_to_datetime


class Analyze:

    def __init__(self):
        pass

    def run(self):
        df = pd.read_csv('./csv/customer.csv')
        # print(df.to_dict(orient='records'))
        ot = df['Lastordertime']
        print(type(ot))

        def differ_day(e1, e2):
            """
            计算两个时间差
            :param e1: 当前列的时间
            :param e2: 第二个待比较时间
            :return:
            """
            # print(type(e1), type(e2))
            return (e2 - str_to_datetime(e1)).days

        df["Days"] = ot.apply(differ_day, args=(datetime.now(),))
        print(df.to_dict(orient='records'))

        describes = df.describe(include=['number'])
        print(type(describes), describes.to_dict())
        pass


if __name__ == '__main__':
    Analyze().run()
