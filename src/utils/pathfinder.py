from collections import deque
import argparse
from .scraper import get_neighbours, get_article_name


class Pathfinder:
    def __init__(self):
        self.path = []
        self.solutions = []

    def get_shortest_path(self, start_url, target_url, max_depth):
        """Gets the shortest path between two wikipedia articles"""

        visited = set()
        queue = deque([(start_url, [start_url], 0)])

        while queue:
            current_url, self.path, depth = queue.popleft()
            print('Current path: ', self.path)
            print('Current Solutions', self.solutions)
            print('Current depth:', depth)

            if depth > max_depth:
                return None

            if current_url == target_url:
                self.path.append(target_url)
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


def main():
    """Main method to test the pathfinder"""

    parser = argparse.ArgumentParser(description='Find the shortest path between two Wikipedia articles.')

    parser.add_argument('start_url', type=str, help='URL of the starting Wikipedia article')
    parser.add_argument('target_url', type=str, help='URL of the target Wikipedia article')
    parser.add_argument('--max-depth', type=int, default=6, help='Maximum depth for BFS (default: 6)')

    args = parser.parse_args()

    print(args.start_url, args.target_url, args.max_depth)

    pf = Pathfinder()

    found_path = pf.get_shortest_path(args.start_url, args.target_url, args.max_depth)
    formatted_path = ' -> '.join(
        [get_article_name(link) for link in found_path]
    )

    print(formatted_path)
    print('Other possible paths:')
    print(pf.solutions)


if __name__ == "__main__":
    main()
