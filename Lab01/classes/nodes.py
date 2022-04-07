from .signal_information import *


class Node:
    def __init__(self, att_dic):
        self.label = att_dic["label"]
        self.position = att_dic["position"]
        self.connected_nodes = att_dic["connected_nodes"]
        self.successive = {}

    # label
    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    # position
    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = pos

    # connected nodes
    def get_connected_nodes(self):
        return self.connected_nodes

    def set_connecting_nodes(self, nodes):
        self.connected_nodes = nodes

    # successive
    def get_successive(self):
        return self.successive

    def set_successive(self, succ):
        self.successive = succ


