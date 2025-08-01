import csv
from graph_utils import build_graph, is_route_possible, find_shortest_path, plan_delivery

# Project 3 Group 13: Kurtis Mok, Andre Jiang, Sydni Yang

def main():
    print("Welcome to Smart Delivery Route Planner!\n")

    graph = build_graph("sample_input.csv")

    depot = input("Enter depot location: ").strip()
    deliveries_input = input("Enter delivery stops (uses commas for separation): ").strip()
    deliveries = [d.strip() for d in deliveries_input.split(",")]

    print("\nChecking route feasibility...")
    all_possible = all(is_route_possible(graph, depot, stop) for stop in deliveries)

    if not all_possible:
        print("One or more delivery locations are unreachable from the depot.")
        return
    else:
        print("Route exists.\n")

    print("Finding optimal delivery route...\n")
    route, total_distance = plan_delivery(graph, depot, deliveries)

    print("Delivery plan:")
    for i in range(len(route) - 1):
        segment_path, distance = find_shortest_path(graph, route[i], route[i+1])
        print(f"{i+1}. {route[i]} → {route[i+1]} ({distance} ML)")
    print(f"Total distance: {total_distance} ML")

if __name__ == "__main__":
    main()
