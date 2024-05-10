from collections import deque
from .scraper import get_neighbours


class Pathfinder:
    def __init__(self):
        self.path = []
        self.solutions = []
        self.cli = False

    def get_shortest_path(self, start_url, target_url, max_depth):
        """Gets the shortest path between two wikipedia articles"""

        visited = set()
        queue = deque([(start_url, [start_url], 0)])

        while queue:
            current_url, self.path, depth = queue.popleft()

            if self.cli:
                print('Current path: ', self.path)
                print('Current Solutions', self.solutions)
                print('Current depth:', depth)

            if depth > max_depth:
                return None

            if current_url == target_url:
                return self.path

            if current_url in visited:
                continue

            visited.add(current_url)
            neighbors = get_neighbours(current_url)

            if target_url in neighbors:
                current_solution = self.path.copy()
                current_solution.append(target_url)
                self.solutions.append(current_solution)

            if neighbors is None:
                continue

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, self.path + [neighbor], depth + 1))

        return None
