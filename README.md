# West Point Coding Portfolio

This repository is a portfolio of coursework and projects completed at West Point. It is organized by course area. Each folder below lists what that project or homework accomplishes in plain language.

## At a glance
- `Algorithms/`: Weekly Scala homework sets focused on algorithm problem solving.
- `Artificial Intelligence/`: Search, inference, and reinforcement learning projects (Pacman and Lunar Lander).
- `Basic Python Problem Sets/`: Intro Python exercises with small datasets and writeups.
- `Building_a_Game/`: A turn-based Treasure Hunt game built in Scala.
- `Databases/`: A Django web app and a database snapshot.
- `Networks/`: UDP pinger, web server, and Scapy/ICMP projects.
- `Programming Languages/`: Scala assignments for language concepts and tooling.

## Projects by course

### Algorithms
Each folder is a standalone Scala homework project with a main solution file, inputs, and tests.
- `hw1-Careless03/`: Implements core algorithms (binary search, fast multiplication), tree traversals (BFS/DFS), and classic graph algorithms (Kruskal/Prim MST, Dijkstra) with a small demo runner.
- `hw2-Careless03/`: Balances groups across a fixed number of tables by binary-searching the smallest feasible table size; merges date ranges to count total reserved days.
- `hw3-Careless03/`: Two binary search variants (index-based and list-chopping) with accompanying analysis.
- `hw4-Careless03/`: Computes the minimum number of rooms needed for overlapping reservations; dynamic approach to maximize donations without taking conflicting entries.
- `hw5-Careless03/`: Brute-force longest alternating up/down subsequence (wiggle-like) from elevation data; weighted interval scheduling to maximize dog-walking pay.
- `hw6-Careless03/`: Counts grid paths with obstacles and limited wall breaches; finds the largest all-1 square in a terrain grid.
- `hw7-Careless03/`: Determines the maximum number of complete card sets possible using sorting, prefix sums, and binary search.
- `hw8-Careless03/`: Reverses a mutable list in two ways (stack-based and pointer reversal).
- `hw9-Careless03/`: Implements lookup and insertion for a 2-3 search tree, including split/merge logic.
- `hw10-Careless03/`: Deduces creature types from battle outcomes using a union-find encoding of type relationships.
- `hw11-Careless03/`: Generates a random maze by treating walls as weighted edges and carving passages via Kruskal's algorithm.

### Artificial Intelligence
- `DFS_BFS_Practice/`: Practice with search basics (depth-first and breadth-first), plus autograder support.
- `Lunar_Landing_Project/`: Deep Q-Network (DQN) agent trained to solve Lunar Lander; includes evaluation script and model code.
- `Pacman_A_Star_Search/`: A* search and heuristic work in the Pacman environment.
- `Pacman_Advesarial_Search/`: Adversarial Pacman agents using minimax and alpha-beta style search.
- `Pacman_Inference_Learning/`: Probabilistic inference and ghost tracking in Pacman.
- `Pacman_Self_Learning/`: Reinforcement learning in Pacman with Q-learning and value iteration.

### Basic Python Problem Sets
- `ps01/`: Intro Python problems on time and simple numeric calculations.
- `ps02/`: Core Python practice problems (single-file submission).
- `ps03/`: Core Python practice problems (single-file submission).
- `ps04/`: File and log processing with multiple input datasets.
- `ps05/`: Word list processing and text-based tasks.
- `ps06/`: Multi-part problem set with example inputs and a main driver.
- `ps07/`: Data processing using text and CSV inputs.
- `ps08/`: Data analysis using a sports dataset CSV.
- `ps09/`: Text processing and utility scripts (eBook and helpers).
- Root level: assignment coversheets in PDF and DOCX format.

### Building_a_Game
- `Building_a_Game/`: A Treasure Hunt game built in Scala with a board, players, movement rules, and distinct player strategies. Includes tests and a rules README.

### Databases
- `Databases/`: A Django web app with models, forms, views, and URLs, plus a SQL backup and setup instructions.

### Networks
- `project 1/`: UDP pinger assignment and analysis writeup.
- `project2/`: A small web server with test pages and a project writeup.
- `project3/`: Scapy-based ICMP client/server work with message and config files.
- `project3_2/`: Starter files for a follow-on network assignment.

### Programming Languages
- `hw1-Careless03/`: Scala warm-up tasks using loops and recursion (product, max, counts, membership, last index).
- `hw2-Careless03/`: Regex and pattern checking exercises with results and a checker tool.
- `hw3-Clymer/`: Writes two CFGs for language constraints and implements an indexed list mapping function.
- `hw4-Clymer/`: Parses and evaluates prefix boolean expressions; also validates input with an Option-based parser.
- `hw5/`: Interprets a robot movement language and implements a tiny stack-based language (BabyGrok).
- `hw8/`: Functional list transformations (expand/squish/filter), max-difference via fold, and Cartesian product pairs.
- `hw10/`: Builds iterators for in-order search tree traversal and level-by-level binary tree traversal.
- `hw11/`: Diagonal traversal of infinite iterators; functional dictionary implemented with closures.
- `hw13/`: Evaluates SKI combinator expressions with a stack-based reducer.

## Notes
This portfolio includes both source files and build artifacts (for example, `target/`, `__pycache__/`, `.metals/`). If you want a cleaned or curated version, those directories can be excluded.
