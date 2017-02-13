import numpy as np
import MySQLdb as sql


def loadfromMysql(shop_id, week_day):
    try:
        conn = sql.connect(host='localhost', user='root', passwd='root', port=3306)
        cur = conn.cursor()
        conn.select_db('tianchi')
        cur.execute('select day_id,cnt from user_pay_new where shop_id=%d and week=%d' % (shop_id, week_day))
        results = cur.fetchall()
        bond = 0
        for r in results:
            if r[0] <= 475:
                bond += 1
            else:
                break
        X = []
        y = []
        for r in results:
            X.append(r[0])
            y.append(r[1])
        X = np.matrix(np.array([X]).T)
        X = np.column_stack((X, np.power(X[:, 0], 0.5)))
        X = np.column_stack((X, np.power(X[:, 0], 2)))
        # X = np.column_stack((X, np.power(X[:, 0], 3)))
        # X = np.column_stack((X, np.power(X[:, 0], 4)))
        # X = np.column_stack((X, np.power(X[:, 0], 5)))
        y = np.matrix(np.array([y]).T)
        X = np.column_stack((np.array(np.ones(X.shape[0])).T, X))
        trainX = X[:bond, :]
        testX = X[bond:]
        trainy = y[:bond, :]
        testy = y[bond:]
        conn.commit()
        cur.close()
        conn.close()
        return trainX, trainy, testX, testy
    except sql.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
