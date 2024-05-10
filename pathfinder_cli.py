from src.utils.pathfinder import Pathfinder
from src.utils.scraper import get_article_name
import argparse


parser = argparse.ArgumentParser(description='Find the shortest path between two Wikipedia articles.')

parser.add_argument('start_url', type=str, help='URL of the starting Wikipedia article')
parser.add_argument('target_url', type=str, help='URL of the target Wikipedia article')
parser.add_argument('--max-depth', type=int, default=6, help='Maximum depth for BFS (default: 6)')

args = parser.parse_args()

print(args.start_url, args.target_url, args.max_depth)

pf = Pathfinder()
pf.cli = True

found_path = pf.get_shortest_path(args.start_url, args.target_url, args.max_depth)
formatted_path = ' -> '.join(
    [get_article_name(link) for link in found_path]
)

print('Shortest path:', formatted_path)
