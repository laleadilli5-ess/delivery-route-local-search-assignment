import math
import random

# =========================================================
# DELIVERY ROUTE IMPROVEMENT USING LOCAL SEARCH HEURISTIC
# =========================================================
#
# DESCRIPTION:
# This program improves a delivery route for a delivery
# company using a Local Search Heuristic approach.
#
# Instead of finding the exact optimal solution
# (which can be computationally expensive),
# the algorithm gradually improves the route by making
# small changes.
#
# APPROACH:
# 1. Start with a random delivery route.
# 2. Randomly swap two delivery locations.
# 3. Calculate the new route distance.
# 4. If the new route is shorter, accept it.
# 5. Otherwise reject it.
# 6. Repeat for many iterations.
#
# This method is a heuristic optimization technique
# commonly used for Traveling Salesman Problems (TSP).
#
# =========================================================


# ---------------------------------------------------------
# RANDOM SEED
# ---------------------------------------------------------
# Using a seed makes results reproducible.
# Every time the program runs, it produces
# the same random behavior.
# ---------------------------------------------------------
random.seed(42)


# ---------------------------------------------------------
# DELIVERY LOCATIONS
# ---------------------------------------------------------
# Each tuple represents a customer location.
#
# Format:
# (x_coordinate, y_coordinate)
# ---------------------------------------------------------
locations = [
    (2, 3),
    (5, 8),
    (1, 1),
    (7, 2),
    (6, 6),
    (8, 3),
    (4, 7)
]


# ---------------------------------------------------------
# FUNCTION: calculate_distance(point1, point2)
# ---------------------------------------------------------
# Calculates Euclidean distance between two points.
#
# Formula:
# distance = sqrt((x2-x1)^2 + (y2-y1)^2)
# ---------------------------------------------------------
def calculate_distance(point1, point2):

    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )


# ---------------------------------------------------------
# FUNCTION: total_route_distance(route, locations)
# ---------------------------------------------------------
# Calculates the total distance of a complete route.
#
# The route contains indices of locations.
#
# Example:
# route = [0, 2, 1]
#
# Means:
# Visit location 0
# Then location 2
# Then location 1
#
# The algorithm also returns to the starting point,
# making the route a complete cycle.
# ---------------------------------------------------------
def total_route_distance(route, locations):

    total_distance = 0

    # Calculate distances between consecutive locations
    for i in range(len(route) - 1):

        current_location = locations[route[i]]
        next_location = locations[route[i + 1]]

        total_distance += calculate_distance(
            current_location,
            next_location
        )

    # -----------------------------------------------------
    # Add distance from last location back to first
    # This creates a complete delivery cycle.
    # -----------------------------------------------------
    first_location = locations[route[0]]
    last_location = locations[route[-1]]

    total_distance += calculate_distance(
        last_location,
        first_location
    )

    return total_distance


# ---------------------------------------------------------
# FUNCTION: local_search(locations, max_iterations)
# ---------------------------------------------------------
# Performs local search optimization.
#
# PARAMETERS:
# locations        -> list of coordinates
# max_iterations   -> number of attempts
#
# RETURNS:
# initial_route
# initial_distance
# best_route
# best_distance
# improvement_count
# ---------------------------------------------------------
def local_search(locations, max_iterations):

    # -----------------------------------------------------
    # Create an initial random route
    # -----------------------------------------------------
    initial_route = list(range(len(locations)))
    random.shuffle(initial_route)

    # -----------------------------------------------------
    # Store current best solution
    # -----------------------------------------------------
    best_route = initial_route[:]

    best_distance = total_route_distance(
        best_route,
        locations
    )

    initial_distance = best_distance

    improvement_count = 0

    # -----------------------------------------------------
    # MAIN LOCAL SEARCH LOOP
    # -----------------------------------------------------
    for iteration in range(max_iterations):

        # Create a copy of current best route
        new_route = best_route[:]

        # -------------------------------------------------
        # Randomly choose two positions in the route
        # -------------------------------------------------
        i, j = random.sample(range(len(new_route)), 2)

        # -------------------------------------------------
        # Swap the two locations
        # -------------------------------------------------
        new_route[i], new_route[j] = (
            new_route[j],
            new_route[i]
        )

        # -------------------------------------------------
        # Calculate new route distance
        # -------------------------------------------------
        new_distance = total_route_distance(
            new_route,
            locations
        )

        # -------------------------------------------------
        # If new route is better, accept it
        # -------------------------------------------------
        if new_distance < best_distance:

            best_route = new_route
            best_distance = new_distance

            improvement_count += 1

            # Print improvement progress
            print(
                f"Improvement #{improvement_count}: "
                f"New Distance = {round(best_distance, 2)}"
            )

    # -----------------------------------------------------
    # Return all important results
    # -----------------------------------------------------
    return (
        initial_route,
        initial_distance,
        best_route,
        best_distance,
        improvement_count
    )


# ---------------------------------------------------------
# PROGRAM EXECUTION
# ---------------------------------------------------------

# Maximum number of iterations
max_iterations = 1000

# Run local search algorithm
(
    initial_route,
    initial_distance,
    best_route,
    best_distance,
    improvement_count
) = local_search(locations, max_iterations)


# ---------------------------------------------------------
# PRINT FINAL RESULTS
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("DELIVERY ROUTE IMPROVEMENT USING LOCAL SEARCH")
print("=" * 60)

print("\nInitial Route:")
print(initial_route)

print("\nInitial Route Distance:")
print(round(initial_distance, 2))

print("\nImproved Route:")
print(best_route)

print("\nImproved Route Distance:")
print(round(best_distance, 2))

print("\nNumber of Improvements Made:")
print(improvement_count)

print("\nMaximum Iterations:")
print(max_iterations)

print("\nOptimization Completed Successfully.")
print("=" * 60)