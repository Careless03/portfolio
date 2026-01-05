# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack, Queue, PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Getting the start state
    start = problem.getStartState()
    # Check if the start state is the Goal state
    if problem.isGoalState(start):
        return []
    # For DFS we operate with a FILO, and us a Stack to push on the intial node, with zero actions
    nodes = Stack()
    nodes.push((start, []))
    # Visited is a set so that there is only ever one variable. 
    visited = set()
    # Loop through the stack until there are no more nodes to iterate through
    while not nodes.isEmpty():
        # Get the state and the path so far for each node
        curr_state, path = nodes.pop()
        # Check to see if we have already visited, if so then move on to the next node and pop that one
        if curr_state in visited: 
            continue 
        # Add the current state to the visited
        visited.add(curr_state)
        # If we have reached the goal state then return the path (list of action) that it took to get ther
        if problem.isGoalState(curr_state):
            return path 
        # getSuccessors = list of successors, the actions available, and the step cost to get there
        for successor, action, stepCost in problem.getSuccessors(curr_state):
            # As long as we dont create a cycle we are going to push it onto the stack with the actions it took to get there
            if successor not in visited:
                nodes.push((successor, path + [action]))
    # If by the time we have gone through the stack we have not find the goal, return nothing
    return []



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Grab the starting node
    start = problem.getStartState()
    # Check to see if the start is the goal, if so stop code
    if problem.isGoalState(start):
        return []
    # FIFO Policy, use a Queue
    nodes = Queue()
    nodes.push((start, []))
    # Ensure we don't create cycles
    visited = set()
    # Go through all the nodes
    while not nodes.isEmpty():
        curr_state, path = nodes.pop()
        # see if we have visited then node, if so skip
        if curr_state in visited: 
            continue 
        # track where we are at
        visited.add(curr_state)
        # If goal then stop 
        if problem.isGoalState(curr_state):
            return path 
        # add all successors with the action it took to get there onto the stack.
        for successor, action, stepCost in problem.getSuccessors(curr_state):
            if successor not in visited:
                nodes.push((successor, path + [action]))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Get the start state and check if it is the start of it
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    # Since this is cost we now have to consider that in the tuple, and we need to organize it by path
    path_cost = 0
    nodes = PriorityQueue()
    nodes.push((start, [], path_cost), path_cost) #state, path, path_cost with path_cost being the priority
    visited = set()
    # Iterate through the entire graph (while avoiding cycles  )
    while not nodes.isEmpty():
        # Grab all the data and check if we have visited the node
        curr_state, path, path_cost = nodes.pop()
        if curr_state in visited: 
            continue 
        visited.add(curr_state)
        # See if we have solved it
        if problem.isGoalState(curr_state):
            return path 
        # Now add onto queue, adding path cost
        for successor, action, stepCost in problem.getSuccessors(curr_state):
            new_path = path_cost + stepCost 
            nodes.push((successor, path + [action], new_path), new_path)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    g_start = 0  # path cost is g(n) according to video
    f_start = g_start + heuristic(start, problem) # logic behind A*
    nodes = PriorityQueue()
    nodes.push((start, [], g_start), f_start) #state, path, path_cost
    visited = set()
    # Go through queue
    while not nodes.isEmpty():
        curr_state, path, g_cost = nodes.pop()
        if curr_state in visited: 
            continue 
        visited.add(curr_state)
        if problem.isGoalState(curr_state):
            return path 
        # Calculating with the heuristic. 
        for successor, action, stepCost in problem.getSuccessors(curr_state):
            new_g = g_cost + stepCost
            f = new_g + heuristic(successor, problem)
            nodes.push((successor, path + [action], new_g), f)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
