from collections import deque
from scraper import get_neighbours


STARTURL = 'https://en.wikipedia.org/wiki/Kim_Jong_Un'
ENDURL = 'https://en.wikipedia.org/wiki/Hot_dog'
ENDURL2 = 'https://en.wikipedia.org/wiki/Workers%27_Party_of_Korea'
ENDURL3 = 'https://en.wikipedia.org/wiki/National_Basketball_Association'
ENDURL4 = 'https://en.wikipedia.org/wiki/Nuno_Gomes_Nabiam'

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

found_path = get_shortest_path(STARTURL, ENDURL)

formatted_path = ' -> '.join([link.lstrip('https://en.wikipedia.org/wiki/') for link in found_path])

print(formatted_path)
