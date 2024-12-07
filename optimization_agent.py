import heapq

class OptimizationAgent:
    @staticmethod
    def optimize_itinerary(itinerary, budget):
        """
        Optimize itinerary based on travel time and budget.
        Implements Dijkstra-like optimization for minimizing travel cost/time.
        """
        graph = {
            stop["stop_name"]: {
                "neighbors": stop.get("neighbors", {}),
                "cost": stop["cost"]
            }
            for stop in itinerary
        }

        # Dijkstra's Algorithm
        def dijkstra(start):
            pq = [(0, start, [])]
            visited = set()
            best_path = {}

            while pq:
                cost, current, path = heapq.heappop(pq)
                if current in visited:
                    continue
                visited.add(current)
                best_path[current] = (cost, path + [current])

                for neighbor, travel_cost in graph[current]["neighbors"].items():
                    if neighbor not in visited:
                        heapq.heappush(pq, (cost + travel_cost, neighbor, path + [current]))

            return best_path

        start = itinerary[0]["stop_name"]
        best_path = dijkstra(start)

        # Apply budget constraints
        optimized_itinerary = []
        total_cost = 0
        for stop_name in best_path:
            stop_cost = graph[stop_name]["cost"]
            if total_cost + stop_cost <= budget:
                optimized_itinerary.append(stop_name)
                total_cost += stop_cost

        return optimized_itinerary

class ItineraryAgent:
    @staticmethod
    def generate(user_input: UserInput):
        city_data = {
            "Berlin": [
                {"stop_name": "Brandenburg Gate", "activity": "Visit iconic landmark", "cost": 0, "neighbors": {"Museum Island": 15}},
                {"stop_name": "Museum Island", "activity": "Explore museums", "cost": 12, "neighbors": {"Brandenburg Gate": 15}}
            ]
        }
        itinerary = city_data.get(user_input.city, [])
        optimized_itinerary = OptimizationAgent.optimize_itinerary(itinerary, user_input.budget)
        return [stop for stop in itinerary if stop["stop_name"] in optimized_itinerary]
