import numpy as np
import MySQLdb as sql

import polyX as poly


def loadall(shop_id):
    try:
        conn = sql.connect(host='localhost', user='root', passwd='root', port=3306)
        cur = conn.cursor()
        conn.select_db('tianchi')
        str = 'select * from user_pay_new where shop_id=%s' % (shop_id)
        cur.execute(str)
        res = cur.fetchall()
        res_week = [[], [], [], [], [], [], []]
        for r in res:
            res_week[r[3] - 1].append((r[4], r[2]))
        conn.commit()
        cur.close()
        conn.close()
        return res_week
    except sql.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def loadfromMysql(sql_res, end_day, interval=1):
    bond = 0
    X = []
    y = []
    # for dummy in sql_res:
    #     X.append(dummy[0])
    #     y.append(dummy[1])
    #     if dummy[0] <= end_day:
    #         bond += 1
    for i in range(len(sql_res) - interval + 1):
        dummy = sql_res[i + interval - 1]
        X.append(dummy[0])
        sum_1 = 0.0
        for j in range(i - interval + 1, i + 1):
            sum_1 += sql_res[j][1]
        # y.append(sum_1 / (sql_res[i][0] - sql_res[i - interval + 1][0] + 1))
        y.append(sum_1 / interval)
        if dummy[0] <= end_day:
            bond += 1
    X = np.matrix(np.array([X]).T)
    X = poly.polyX(X)
    y = np.matrix(np.array([y]).T)
    trainX = X[:bond, :]
    testX = X[bond:]
    trainy = y[:bond, :]
    testy = y[bond:]
    return trainX, trainy, testX, testy


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print a[-2]
