class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Problem: there can be duplicates within the tickets
        """
        
        visited = {}
        adj = defaultdict(list)
        for src, dst in tickets:
            visited[(src, dst)] = 1 + visited.get((src, dst), 0)
            adj[src].append(dst)
        
        for key in adj.keys():
            adj[key].sort()

        itinerary = ["JFK"]

        def dfs(src):
            if len(itinerary) == len(tickets) + 1:
                return True
            for dst in adj[src]:
                if visited[(src, dst)] == 0:
                    continue
                visited[(src, dst)] -= 1
                itinerary.append(dst)
                if dfs(dst):
                    return True
                visited[(src, dst)] += 1
                itinerary.pop()
            return False

        dfs("JFK")
        return itinerary
