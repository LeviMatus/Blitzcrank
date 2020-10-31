from typing import Protocol

from py2neo import Node, Graph
from py2neo.ogm import GraphObject


class Repository(Protocol):
    def add(self, entity):
        raise NotImplementedError

    def get(self, reference):
        raise NotImplementedError


class NeoRepository:
    def __init__(self, graph: Graph):
        self.graph = graph

    def add(self, node: Node):
        self.graph.merge(node)

    def get(self, reference: GraphObject) -> Node:
        return self.graph.nodes.match(reference.__primarylabel__, "id").first()

    def update(self, node: Node):
        return self.graph.push(node)
