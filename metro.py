import pandas as pd
import random
import heapq
from collections import defaultdict, deque

# it will load the singapore metro station's data from the csv file
df = pd.read_csv("/mnt/data/processed_stations.csv")


graph = defaultdict(list) # each key is a name of a station 

# it builds the connections between consecutive stations on the same line
lines = df.groupby('line')
for line_name, group in lines:
    sorted_stations = group.sort_values('num')
    stations = list(sorted_stations.itertuples(index=False))

    for i in range(len(stations) - 1):
        s1 = stations[i]
        s2 = stations[i + 1]
        travel_time = random.randint(2, 8)  # it randomizes the travel time
        graph[s1.name].append((s2.name, travel_time))
        graph[s2.name].append((s1.name, travel_time))  # it is undirected

# It handles the interchange stations
station_groups = df.groupby('name')
for station_name, group in station_groups:
    if len(group) > 1:
        # it adds a 5-minute transfer to itself to simulate interchange
        graph[station_name].append((station_name, 5))

# the shortest path based on the number of stops
def shortest_path_by_stops(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None 

# the fastest path based on the time of travel
def fastest_path_by_time(graph, start, end):
    heap = [(0, start, [start])]
    visited = set()

    while heap:
        current_time, current_station, path = heapq.heappop(heap)
        if current_station == end:
            return path, current_time
        if current_station in visited:
            continue
        visited.add(current_station)
        for neighbor, travel_time in graph[current_station]:
            if neighbor not in visited:
                heapq.heappush(heap, (current_time + travel_time, neighbor, path + [neighbor]))
    return None, float('inf')

if __name__ == "__main__":
    start_station = "ADMIRALTY MRT STATION"
    end_station = "ANG MO KIO MRT STATION"

    print("=== Shortest Path (Fewest Stops) ===")
    stops_path = shortest_path_by_stops(graph, start_station, end_station)
    if stops_path:
        print(" -> ".join(stops_path))
        print(f"Total stops: {len(stops_path) - 1}")
    else:
        print("No path is found")

    print("\n=== Fastest Route (Shortest Travel Time) ===")
    time_path, total_time = fastest_path_by_time(graph, start_station, end_station)
    if time_path:
        print(" -> ".join(time_path))
        print(f"Estimated travel time: {total_time} minutes")
    else:
        print("No path is found.")