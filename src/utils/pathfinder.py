from collections import deque
from scraper import get_neighbours


def get_shortest_path(start_url, target_url):
    """Gets the shortest path between two wikipedia articles"""

    visited = set()
    queue = deque([(start_url, [start_url])])

    while queue:
        current_url, path = queue.popleft()
        print(path)
        if current_url == target_url:
            return path

        if current_url in visited:
            continue

        visited.add(current_url)
        neighbors = get_neighbours(current_url)

        if target_url in neighbors:
            path.append(target_url)
            return path

        if neighbors is None:
            continue

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


def main():
    """Main method to test the pathfinder"""

    start_url = 'https://en.wikipedia.org/wiki/Kim_Jong_Un'
    end_url = 'https://en.wikipedia.org/wiki/Hot_dog'
    end_url2 = 'https://en.wikipedia.org/wiki/Workers%27_Party_of_Korea'
    end_url3 = 'https://en.wikipedia.org/wiki/National_Basketball_Association'

    found_path = get_shortest_path(start_url, end_url2)
    formatted_path = ' -> '.join(
        [link.lstrip('https://en.wikipedia.org/wiki/') for link in found_path]
    )

    print(formatted_path)


if __name__ == "__main__":
    main()
