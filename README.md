# delivery-route-local-search-assignment
Delivery Route Improvement Using Local Search Heuristic in Python
# Delivery Route Improvement Using Local Search

## Project Description

This project implements a Local Search Heuristic algorithm to improve a delivery route for a delivery company.

The program starts with a random route between customer locations and repeatedly swaps two locations in the route. If the new route produces a shorter total distance, the algorithm accepts the change; otherwise, it discards it.

The goal of this project is not to find the exact optimal solution, but to improve the route using heuristic optimization techniques commonly used in Traveling Salesman Problems (TSP).

---

# Algorithm Overview

The algorithm works using the following steps:

1. Generate an initial random route
2. Calculate the total route distance
3. Randomly swap two locations
4. Calculate the new route distance
5. If the new distance is shorter:
   - Accept the new route
6. Otherwise:
   - Reject the new route
7. Repeat the process for many iterations

This approach is called a **Local Search Heuristic** because the algorithm improves the current solution step by step.

---

# Features

- Random initial delivery route
- Euclidean distance calculation
- Route optimization using local search
- Random swap heuristic
- Iteration-based improvement
- Improvement tracking
- Fully commented Python code
- Clear and structured output

---

# Technologies Used

- Python 3
- Standard Python Libraries:
  - math
  - random

---

# File Structure

```text
delivery-route-local-search/
│
├── delivery_route.py
└── README.md
```

---

# How to Run the Program

## Step 1
Make sure Python 3 is installed on your computer.

## Step 2
Open terminal or command prompt.

## Step 3
Run the following command:

```bash
python delivery_route.py
```

---

# Example Output

```text
Improvement #1: New Distance = 29.44
Improvement #2: New Distance = 27.31
Improvement #3: New Distance = 24.85

============================================================
DELIVERY ROUTE IMPROVEMENT USING LOCAL SEARCH
============================================================

Initial Route:
[1, 3, 4, 2, 6, 0, 5]

Initial Route Distance:
34.12

Improved Route:
[0, 2, 1, 6, 4, 5, 3]

Improved Route Distance:
21.45

Number of Improvements Made:
8

Maximum Iterations:
1000

Optimization Completed Successfully.
============================================================
```

---

# Distance Formula

The program uses the Euclidean Distance Formula:


::contentReference[oaicite:0]{index=0}


This formula calculates the distance between two coordinate points.

---

# Complexity Analysis

Time Complexity:

:contentReference[oaicite:1]{index=1}

Where:
- `iterations` = number of optimization attempts
- `n` = number of delivery locations

The algorithm becomes more computationally expensive as the number of locations and iterations increases.

---

# Local Search Heuristic Explanation

A Local Search algorithm improves a solution gradually instead of checking every possible route.

Advantages of this approach:
- Faster than exact optimization algorithms
- Easier to implement
- Suitable for large problems
- Produces good approximate solutions

Disadvantages:
- Does not always find the global optimal solution
- Result depends on random swaps and iterations

---

# Conclusion

This project demonstrates how heuristic optimization techniques can improve delivery route planning problems efficiently.

The Local Search approach successfully reduces the total delivery distance by repeatedly testing and accepting better routes.

This type of optimization is widely used in:
- Delivery systems
- Logistics
- Transportation planning
- Vehicle routing problems
- Traveling Salesman Problems (TSP)

---
