# Traveling Salesperson Problem Using Dynamic Programming

## Project Description

This project implements a dynamic programming solution for the Traveling Salesperson Problem (TSP). The scenario is based on routing optimization for a nationwide sales team. A salesperson starts from one regional office, visits every other office exactly once, and then returns to the starting office.

The goal of the program is to find the minimum total distance required to complete the route.

## Algorithm Used

The solution uses the Held-Karp dynamic programming approach. Instead of checking every possible route like brute force, the algorithm stores the best cost for each subset of visited offices and each possible ending office.

The dynamic programming state is:

```text
dp[subset, last]
