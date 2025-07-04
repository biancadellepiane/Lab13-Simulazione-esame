import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMap = {}

    def buildGraph(self, year):
        self._graph.clear()
        nodes = DAO.getAllNodes(year)
        for n in nodes:
            self._idMap[n.driverId] = n

        self._graph.add_nodes_from(nodes)

        archi = DAO.getallEdges(year, self._idMap)
        for a in archi:
            if a.vincente in self._graph and a.perdente in self._graph:
                self._graph.add_edge(a.vincente, a.perdente, weight=a.peso)

    def graphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()



    def getAllYear(self):
        years = DAO.getAllYear()
        return years
        #return DAO.getAllYear()

    def getMigliorPilota(self):
        #inizializzo a zero i dati da trovare: pilota e punteggio
        self._bestPilota = None
        self._punteggio = 0

        #cerco tra i nodi (che sono i piloti)
        for d in self._graph.nodes():
            vittorie = 0
            for succ in self._graph.successors(d):
                #sommo peso archi uscendi
                vittorie += self._graph[d][succ]["weight"]

            #sottraggo archi entranti
            sconfitte = 0
            for pred in self._graph.predecessors(d):
                sconfitte += self._graph[pred][d]["weight"]

            score = vittorie - sconfitte
            if score > self._punteggio:
                self._punteggio = score
                self._bestPilota = d

        return self._bestPilota, self._punteggio

