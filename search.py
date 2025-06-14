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
from game import Directions
from typing import List


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


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    current_state = problem.getStartState()

    if problem.isGoalState(current_state):
        return []

    stack = util.Stack()
    visited = set()

    for i in problem.getSuccessors(current_state):
        stack.push([i])

    while not stack.isEmpty():
        path = stack.pop()
        successor = path[-1]

        if problem.isGoalState(successor[0]):
            return [node[1] for node in path]

        if successor[0] not in visited:
            visited.add(successor[0])

            for next_node in problem.getSuccessors(successor[0]):
                if next_node[0] not in visited:
                    new_path = path.copy()
                    new_path.append(next_node)

                    stack.push(new_path)
    return []


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []

    queue = util.Queue()
    visited = set()

    visited.add(start_state)
    for successor in problem.getSuccessors(start_state):
        visited.add(successor[0])
        queue.push([successor])

    while not queue.isEmpty():
        path = queue.pop()
        successor = path[-1]

        if problem.isGoalState(successor[0]):
            return [succ[1] for succ in path]

        for next_node in problem.getSuccessors(successor[0]):
            if next_node[0] not in visited:
                visited.add(next_node[0])

                new_path = path.copy()
                new_path.append(next_node)
                queue.push(new_path)

    return []


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    start_state = problem.getStartState()

    if problem.isGoalState(start_state):
        return []

    priority_queue = util.PriorityQueue()
    visited = set()

    priority_queue.push((start_state, [], 0), 0)

    while not priority_queue.isEmpty():
        state, path, cost = priority_queue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for next_node in problem.getSuccessors(state):
                if next_node[0] not in visited:
                    new_path = path.copy()
                    new_path.append(next_node[1])

                    new_cost = cost + next_node[2]

                    priority_queue.push((next_node[0], new_path, new_cost), new_cost)


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    start_state = problem.getStartState()

    if problem.isGoalState(start_state):
        return []

    priority_queue = util.PriorityQueue()
    visited = {}

    priority_queue.push((start_state, [], 0), heuristic(start_state, problem))

    while not priority_queue.isEmpty():
        state, path, cost = priority_queue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited.keys() or cost < visited[state]:
            visited[state] = cost
            for next_node in problem.getSuccessors(state):
                next_state, action, step_cost = next_node
                new_cost = cost + step_cost

                if next_state not in visited or new_cost < visited[next_state]:
                    new_path = path.copy()
                    new_path.append(action)

                    priority = new_cost + heuristic(next_state, problem)
                    priority_queue.push((next_state, new_path, new_cost), priority)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
