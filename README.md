
# This Python program models the metro system of Singapore and allows users to:
- Find the **shortest path by number of stops** (using Breadth-First Search)
- Find the **fastest route by travel time** (using Dijkstra’s Algorithm)

# It loads and processes station data from a CSV file (`processed_stations.csv`) 

## Algorithms that are used for the program: 

### Breadth-First Search / BFS
This method is used to find the **shortest path based on number of stops**
#### How it works:
- it treats the metro system as a graph and makes sure that the fewest number of stops between two stations are used 

### The Dijkstra’s Algorithm
We will use this specific algorithm to find the **fastest path based on travel time**
#### How it works:
- it uses a priority queue to visit the station with the shortest time
- it uses random travel time between connected stations
- it adds 5 minutes when switching lines at interchangeable stations

## The Data Structures

- **Priority Queue**: operated with `heapq` for efficient Dijkstra performance
- **Graph**: it uses `defaultdict(list)`. Each station is both an edge and a node
- **Queue**: to implement the `collections.deque` for BFS 
- **Set**: it is used to track stations and avoid cycles

## features 
- **Graph-based metro map** 
- **Fastest path algorithm** 
- **Shortest path algorithm** 
- **Randomized travel times (2-8 minutes)** 
- **Fixed transfer time (5 minutes)** 

## Below some of the requirments for the file 

- `processed_stations.csv`: a file containing station names, lines, positions
  - `name`: It is the station name
  - `num`: The position of the station on its line
  - `line`: It is the MRT line
