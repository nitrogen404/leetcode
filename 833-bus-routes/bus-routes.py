class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_buses = {}
        for bus in range(len(routes)):  
            for stop in routes[bus]:
                if stop not in stop_to_buses:
                    stop_to_buses[stop] = []
                stop_to_buses[stop].append(bus)
        
        q = deque([source])
        
        visited_stops = set()
        visited_stops.add(source)
        visited_buses = set()

        buses_taken = 0

        while q:
            level_size = len(q)
            buses_taken += 1

            for _ in range(level_size):
                current_stop = q.popleft()
                for bus in stop_to_buses.get(current_stop, []):
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return buses_taken
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append(next_stop)
        return -1

