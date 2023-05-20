class BullyAlgorithm:
    def __init__ (self, nodeId, nodes):
        self.nodeId = nodeId
        self.nodes = nodes

    def startElection(self):
        highestNodeID = self.nodeId
        # send "Coordinator election" message to all higher ID Nodes
        for i in range(self.nodeId+1, len(self.nodes)+1):
            if i in self.nodes:
                print("Node ",self.nodeId,"Sends Coordinator Election Message to Node",i)
        
        # wait for "ok" message from all higher ID Nodes

        for i in range(self.nodeId+1, len(self.nodes)+1):
            if i in self.nodes:
                print("Node ", self.nodeId,"waiting for Ok message from Node",i)

        # Check if there is higher ID Node that reponded

        for i in range(self.nodeId+1, len(self.nodes)+1):
            if i in self.nodes:
                print("Node ", self.nodeId,"Received Ok message from Node",i)

        # if there is a higherID node then send "coordinator" message to that node
        if highestNodeID != self.nodeId:
            print("Node ", self.nodeId,"Sends Coordinator message to Node",highestNodeID)
        
        # otherwise become the coordinator
        else:
            print("Node", self.nodeId,"is the new coordinator")

nodes = [1,2,3,4,5]

#create an instace of bully algorithm with specific nodeId and list of nodes
bully = BullyAlgorithm(3,nodes) 

# start the election process
bully.startElection()
