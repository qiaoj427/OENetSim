#!/usr/bin/env python
import random

import networkx as nx
import numpy as np

class Flow(object):
    # @timing_function
    def __init__(self,src, dst, dataSize, timeStamp):
        self.src = src
        self.dst = dst
        self.dataSize = dataSize
        self.timeStamp = timeStamp

    # 生成数据流，r：TOR数量
    def CreatFlow(self, r):
        self.timeStamp = random.randint(0, r * (r - 1) / 2 - 1)
        self.src = random.randint(0, r - 1)
        self.dst = random.randint(0, r - 1)
        P = random.random()
        if P < 0.8:
            self.dataSize = round(random.uniform(0, 100), 3)
        else:
            self.dataSize = round(random.uniform(100, 10240), 3)
        return self

    # 生成数据流列表，数据流的个数为N
    def CreateFlowList(self, N, r):
        flowList = {}
        for i in range(N):
            flow = Flow()
            flowList[i] = self.CreatFlow(flow, r)
        return flowList

    # 生成数据流数量矩阵，每个元素代表源TOR到目的TOR的数据流个数
    def CreatFlowMatrix(self, flowList, r):
        matrix = np.zeros([r, r], dtype=int) # 初始化一个零矩阵
        for i in range(len(flowList)):
            if flowList[i].src != flowList[i].dst:
                matrix[flowList[i].src][flowList[i].dst] += 1
        return matrix

    # 生成对应连接TOR的流量列表
    def FlowMatrixList(self, flowList, r):
        flowMatrixList = {}
        for i in range(r * r):
            flowMatrixList[i] = set()
        for i in range(len(flowList)):
            k = flowList[i].src * r + flowList[i].dst % r
            if flowList[i].src != flowList[i].dst:
                flowMatrixList[k].add(flowList[i])
            else:
                pass
        return flowMatrixList


