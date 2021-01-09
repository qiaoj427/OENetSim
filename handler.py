
class FlowHandler:
    def __init__(self):
        return True

class OCSLink:
    def __init__(self,bandwidth):
        self.bandwidth = bandwidth

class EPSLink:
    def __init__(self,bandwidth,forwardingRate):
        self.bandwidth = bandwidth
        self.forwardingRate = forwardingRate

def EPS(flowList):
    return True

def OCS(flowList):
    return True

'''
定义光交换机的连接矩阵，周期为cycle,TOR数量为r,光交换机个数为OCS
则重配置的时间周期内可连接OCS对TOR
1 0-1
2 0-2
3 0-3
4 0-4
5 1-2
6 1-3
7 1-4
8 2-3 ...
'''
def ConnMatrix(r):
    #while True:
    ConnMatrixList1 = {}
    ConnMatrixList2 = {}
    k = 0
    l = 0
    for i in range(r):
        for j in range(r):
            matrix1 = np.zeros([r, r], dtype=int)
            matrix2 = np.zeros([r, r], dtype=int)
            if i < j:
                matrix1[i][j] = 1
                ConnMatrixList1[k] = matrix1
                k += 1
                continue
            elif r - i - 1 < r - j - 1:
                matrix2[r - i - 1][r - j - 1] = 1
                ConnMatrixList2[l] = matrix2
                l += 1
                continue
            else:
                continue
            # print(matrix)
            # return matrix
            # time.sleep(cycle)
    return ConnMatrixList1,ConnMatrixList2

# 查找连接矩阵，返回当前连接的TOR
def FindConnMatrix(time, r):
    con1, con2 = ConnMatrix(r)
    con1 = con1[time]
    con2 = con2[time]
    conNum1 = {}
    conNum2 = {}
    k ,l = 0, 0
    for i in range(r):
        for j in range(r):
            if con1[i][j] > 0:
                conNum1[k] = [i, j]
                k += 1
            elif con2[i][j] > 0:
                conNum2[l] = [i, j]
                l += 1
            else:
                pass
    return conNum1,conNum2