# -*- encoding: utf-8 -*-


import pandas as pd
from xpf import get_nday_list


def get():
    nl = get_nday_list(7)
    # print(nl)
    df = pd.DataFrame(nl, columns=["ViewDate"])
    # print(df)

    ol = [["2019-03-11", 88.9, 34],
          ["2019-03-14", 288.9, 324],
          ["2019-03-13", 848.9, 334],
          ["2019-03-16", 84.9, 344],
          ["2019-03-12", 883.9, 354]]
    odf = pd.DataFrame(ol, columns=["ViewDate", "Payables", "Orders"])

    # print(odf)

    mdf = df.merge(odf, on="ViewDate", how="left")
    mdf = mdf.fillna(0)

    print(mdf["ViewDate"].tolist(), mdf["Payables"].tolist(), mdf["Orders"].tolist())

    # print(mdf)


if __name__ == '__main__':
    get()







