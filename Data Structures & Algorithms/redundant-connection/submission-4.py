class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Given an undirected graph with n nodes and 
        consisting of n-1 edges. An additional edge
        is added to the graph. The edge has two different
        vertices chosen from 1 to n and that edge did not
        previously exit within the graph.
        Basically, the edge is not a loop
        The graph is only represented as an edges array,
        which is just a list of edges. 
        Return an edge that can be removed so that the
        graph is still connected but non-cyclical
        Return the edge that appears last in the input

        Guaranteed that there is only one cycle, so we
        just return the last edge we see when we determine
        its a cycle. 

        Objective: 
            Determine which edge within the 
            undirected graph is redundant. 
        Question:
            Can determining whether an edge is redundant
            be found by detecting a cycle? 
        Idea:
            Detect cycle, and when a cycle is detected,
            return the edge.
        Problem: The edge must be returned based on the order
        it appears in the edge list, indicating that we must
        iterate through the edge list
        Can we detect a cycle as we are building the adjacency list
        I think the key lies in the neighbors.
        Can you DFS into the adj list and identify the target?
        That's complex however

        What's a fast way of determining whether an edge creates a cycle?
        Make it work than make it fast
        """
        adj = defaultdict(list)
        def dfs(h, t, prev):
            if h == t:
                return True

            for nbr in adj[h]:
                if nbr == prev:
                    continue
                if dfs(nbr, t, h):
                    return True
            return False

        res = [0,0]
        for h, t in edges:
            if h in adj and t in adj and dfs(h, t, 0):
                return [h, t]

            adj[h].append(t)
            adj[t].append(h)












