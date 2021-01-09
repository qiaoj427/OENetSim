import numpy as np
import networkx as nx

class Switch:
    def __init__(self, node_name):
        self.node_name = node_name
        self.flow = []

    def create_flow(self):
        self.flow.append(flow_handler.flow_forwarding)

    def delete_flow(self):
        del self.flow[0]

class OpticalCircuitSwitch(Switch):
    def __init__(self, node_name):
        Switch.__init__(self, node_name)
        self.link_inside = []
        self.traffic_matrix = np.zeros([ToR_NUM,ToR_NUM], dtype=int)
        self.down_link = {}

    def config_connect(self):
        for i in range(ToR_NUM):
            for j in range(ToR_NUM):
                if self.traffic_matrix[i][j] != 0:
                    self.link_inside.append(["ToR" + str(i), "ToR" + str(j)])

class ElectricalPacketSwitch(Switch):
    def __init__(self, node_name):
        Switch.__init__(self, node_name)
        self.up_link = {}
        self.down_link = {}

class ToRSwitch(Switch):
    def __init__(self, node_name):
        Switch.__init__(self, node_name)
        self.up_link = {}

class Link:
    def __init__(self, src, dst, bandwidth):
        self.src = src
        self.dst = dst
        self.bandwidth = bandwidth


class Helios:
    def __init__(self):
        self.ocs = []
        self.eps = []
        self.tor = []
        self.topo = nx.DiGraph()

    def run(self):
        self.initialize_ocs()
        self.initialize_eps()
        self.initialize_tor()
        self.connect_tor_to_ocs()
        self.connect_tor_to_eps()

    def initialize_ocs(self):
        for i in range(OCS_NUM):
            node_name = "OCS" + str(i)
            ocs = OpticalCircuitSwitch(node_name)
            self.topo.add_node(node_name)
            self.ocs.append(ocs)

    def initialize_eps(self):
        for i in range(EPS_NUM):
            node_name = "EPS" + str(i)
            aggr = ElectricalPacketSwitch(node_name)
            self.topo.add_node(node_name)
            self.eps.append(aggr)

    def initialize_tor(self):
        for i in range(ToR_NUM):
            node_name = "ToR" + str(i)
            aggr = ToRSwitch(node_name)
            self.topo.add_node(node_name)
            self.tor.append(aggr)

    def connect_tor_to_ocs(self):
        for tor in self.tor:
            for ocs in self.ocs:
                src_name = tor.node_name
                dst_name = ocs.node_name
                bandwidth = LINK_BANDWIDTH_ToR_OCS
                up_link = Link(src_name, dst_name, bandwidth)
                down_link = Link(dst_name, src_name, bandwidth)
                tor.up_link[dst_name] = up_link
                ocs.down_link[src_name] = down_link
                self.topo.add_edges_from([(src_name, dst_name)])
                self.topo.add_edges_from([(dst_name, src_name)])

    def connect_tor_to_eps(self):
        for tor in self.tor:
            for eps in self.eps:
                src_name = tor.node_name
                dst_name = eps.node_name
                bandwidth = LINK_BANDWIDTH_ToR_EPS
                up_link = Link(src_name, dst_name, bandwidth)
                down_link = Link(dst_name, src_name, bandwidth)
                tor.up_link[dst_name] = up_link
                eps.down_link[src_name] = down_link
                self.topo.add_edges_from([(src_name, dst_name)])
                self.topo.add_edges_from([(dst_name, src_name)])
