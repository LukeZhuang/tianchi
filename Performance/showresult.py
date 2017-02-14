import MySQLdb as sql
import numpy as np
import matplotlib.pyplot as ploter


def visualizeResult(shop_id):
    res = []
    try:
        conn = sql.connect(host='localhost', user='root', passwd='root', port=3306)
        cur = conn.cursor()
        conn.select_db('tianchi')
        str = 'select day_id,cnt from user_pay_new where shop_id=%d' % (shop_id)
        cur.execute(str)
        res = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
    except sql.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    X = []
    y = []
    for line in res:
        X.append(line[0])
        y.append(line[1])
    ploter.figure(1)
    X = np.array(X)
    y = np.array(y)
    ploter.plot(X, y, 'b-')
    X1 = []
    y1 = []
    days = [490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503]
    for day in days:
        X1.append(day)
    f = open("result.csv")
    for line in f:
        cols = line.split(',')
        if int(cols[0]) == shop_id:
            for i in range(14):
                y1.append(cols[i + 1])
            break
    X1 = np.array(X1)
    y1 = np.array(y1)
    ploter.plot(X1, y1, 'r-')
    ploter.show(1)


if __name__ == '__main__':
    X = np.array([1, 2, 3])
    y = np.array([5, 3, 4])
    ploter.figure(1)
    ploter.plot(X, y, 'b-')
    ploter.show(1)
