import numpy as np

def newtomPoloy(a,fa):

    assert len(a) == len(fa)
    n = len(a)
    tables =np.zeros((n,n),dtype = np.float64) # length of a
    f_ = lambda y1,y0,x1,x0 : (y1-y0) / (x1-x0)
    tables[:, 0] = fa

    for col in range(1, n+1):
        for row in range(col, n):
            tables[row][col] = f_(tables[row][col-1], tables[row-1][col-1], a[row],a[col-row])

        result = [tables[col][col] for col in range(n)]
        return result
