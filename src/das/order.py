# -*- encoding: utf-8 -*-

from pandas import DataFrame
import pandas as pd
import datetime


class Analyzer:

    def __init__(self):
        pass

    def run(self):
        df = self.load_df()
        # print(pd.to_datetime(df))
        # return
        # df['AddTime'] = df['AddTime'].astype('datetime64')
        # df.to_timestamp()

        # df['AddTime'] = df['AddTime'].map(lambda x: x.strftime('%Y-%m-%d'))
        df['AddTime'] = df['AddTime'].astype('datetime64[D]')

        print(df.dtypes)

        print(df['AddTime'][0:5])

        # print(df.groupby(['AddTime']).sum())
        return
        # print(df["Payables"].plot())
        # 统计出有多少客户下单,以及每个用户下了多少单
        dvc = df["UserId"].value_counts()
        # 获取客户数量
        users = dvc.size
        print('有 %d 个客户下单' % users)

        payables = df['Payables']

        print('\n下单总金额为 %.2f 元, 平均客单价为 %.2f 元' % (payables.sum(), payables.mean()))

        print('单笔最大金额 %.2f 元,最小金额 %.2f' % (payables.max(), payables.min()))

        print(payables.describe())

        pnum = df['ProductNum']

        print('\n销售单品数量 %d , 平均购买数量 %f' % (pnum.sum(), pnum.mean()))

        print('一次最多购买 %d , 最少购买 %d 单品数' % (pnum.max(), pnum.min()))

        print(pnum.describe())

        pay_df = df[df['PayStatus'] == 1]

        ddf = pay_df[['Payables', 'ProductNum']]
        dfd = ddf.describe()
        print(type(dfd), dfd.to_dict())

        # print(payables.items())

        # print(type(dvc), dvc.size, dvc.to_list())
        # print(dvc[0])
        # dvc.plot()
        # print(type(dvc), len(dvc), )

        pass

    def load_df(self):
        """
        从csv文件中加载数据到dataFrame对象
        :return: DataFrame对象
        """
        df = pd.read_csv('./csv/order.csv')
        # print(df)
        return df


if __name__ == '__main__':
    Analyzer().run()


"""
        # 选择前五行

        df[0:5]

        # 选择索引号140及其以后的行

        df[140:]

        # 只选择索引号为50的那一行

        df.loc[50]

        # 选择索引号为45和90的两行

        df.loc[[45, 90]]
        把FILM这一列设置为自定义索引
        .set_index('FILM', inplace=False, drop=True)
        
        ser = Series(np.arange(3.))

data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))

data['w']  #选择表格中的'w'列，使用类字典属性,返回的是Series类型

data.w    #选择表格中的'w'列，使用点属性,返回的是Series类型

data[['w']]  #选择表格中的'w'列，返回的是DataFrame属性

data[['w','z']]  #选择表格中的'w'、'z'列

data[0:2]  #返回第1行到第2行的所有行，前闭后开，包括前不包括后

data[1:2]  #返回第2行，从0计，返回的是单行，通过有前后值的索引形式，
       #如果采用data[1]则报错

data.ix[1:2] #返回第2行的第三种方法，返回的是DataFrame，跟data[1:2]同

data['a':'b']  #利用index值进行切片，返回的是**前闭后闭**的DataFrame, 
        #即末端是包含的  
data.irow(0)   #取data的第一行
data.icol(0)   #取data的第一列

data.head()  #返回data的前几行数据，默认为前五行，需要前十行则dta.head(10)
data.tail()  #返回data的后几行数据，默认为后五行，需要后十行则data.tail(10)

ser.iget_value(0)  #选取ser序列中的第一个
ser.iget_value(-1) #选取ser序列中的最后一个，这种轴索引包含索引器的series不能采用ser[-1]去获取最后一个，这回引起歧义。

data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame

data.loc['a',['w','x']]   #返回‘a’行'w'、'x'列，这种用于选取行索引列索引已知

data.iat[1,1]   #选取第二行第二列，用于已知行、列位置的选取。
"""
