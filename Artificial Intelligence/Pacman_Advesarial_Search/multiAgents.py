# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        score = successorGameState.getScore()

        # Get current data
        currPos = currentGameState.getPacmanPosition()
        currFood = currentGameState.getFood()
        currFoodList = currFood.asList()
        newFoodList = newFood.asList()
        
        # Encourage getting all the food
        if len(newFoodList) == 0:
            return 10000

        # Reward eating a pellet
        # If the number of food pellets decreased, give a bonus
        if len(newFoodList) < len(currFoodList):
            score += 1000

		# Set the max values to curr and next bc they are going to reduce
        currMinFoodDist = float("inf")
        nextMinFoodDist = float("inf")
        
		# Iterate through it and find out the min food distance for curr and next
        # Reward progress toward food compute current min distance to food
        for food in currFoodList:
            distance = util.manhattanDistance(currPos, food)
            if distance < currMinFoodDist:
                currMinFoodDist = distance
        # Compute next min distance to food
        for food in newFoodList:
            distance = util.manhattanDistance(newPos, food)
            if distance < nextMinFoodDist:
                nextMinFoodDist = distance

        # Progress is how much we shortened the path to the nearest food
        # If we stopped and did not get closer, progress is zero
        progress = currMinFoodDist - nextMinFoodDist
        if progress > 0:
            # making sure food dominates when ghosts are far
            score += 300 * progress
        else:
            if progress < 0:
                score -= 5

        # Punish when non scared ghosts are near
        for i in range(len(newGhostStates)):
            ghost = newGhostStates[i]
            scared = newScaredTimes[i]
            ghost_distance = util.manhattanDistance(newPos, ghost.getPosition())
            if scared > 0:
                score += 50.0 / (ghost_distance + 1)
            else:
                if ghost_distance <= 1:
                    score -= 2000
                elif ghost_distance == 2:
                    score -= 200
                elif ghost_distance == 3:
                    score -= 50
        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
            Returns the minimax action from the current gameState using self.depth
            and self.evaluationFunction.

            Here are some method calls that might be useful when implementing minimax.

            gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

            gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

            gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # Local recurive function to return the minimax value of the given
        # GameState for the current agent and depth
        def minimax_value(state, agentIndex, depthLeft):
            # Base case. Step when depth is zero
            # check the below
            if depthLeft == 0 or state.isWin() or state.isLose():
                return self.evaluationFunction(state)
			# Get legal actions for the curr agent
            legalActions = state.getLegalActions(agentIndex)
            
			# If no legal actions, the evaluate the state directly
            if len(legalActions) == 0:
                return self.evaluationFunction(state)
            
			# Determine who moves next. Only reduce depth after the last ghost moves
            nextAgent = agentIndex + 1
            nextDepth = depthLeft
            if nextAgent == numAgents:
                nextAgent = 0
                nextDepth = depthLeft - 1
                
			# Pacman maximizes the value
            if agentIndex == 0:
                best = float("-inf") # value = - infinity
                for action in legalActions: 
                    # Generate the successor exactly once for this edge
                    successors = state.generateSuccessor(agentIndex, action)
                    val = minimax_value(successors, nextAgent, nextDepth)
                    if val > best: 
                        best = val 
                return best
            else: 
                best = float("inf")
                for action in legalActions:
                    succ = state.generateSuccessor(agentIndex, action)
                    val = minimax_value(succ, nextAgent, nextDepth)
                    if val < best:
                        best = val
                return best
        # Read total num of agents from the state
        numAgents = gameState.getNumAgents()
		# Root decision: evaluate each legal action for Pacman using the recursive function above
        legalActionsRoot = gameState.getLegalActions(0)
        bestValue = float("-inf")
        # this will collect all acts that tie for the best numeric values
        # It was becoming stuck, this will fix it.
        bestActions = []
        for action in legalActionsRoot:
            # Start off with pacman
            succ = gameState.generateSuccessor(0, action)
            value = minimax_value(succ, 1, self.depth)
            if value > bestValue:
                bestValue = value 
                bestActions = [action]
            elif value == bestValue: 
                bestActions.append(action)
        # It doesn't matter which best action, just choose one.
        return random.choice(bestActions)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        Requirements satisfied
            1. Works with many minimizer agents
            2. No child reordering
            3. No pruning on equality
            4. Do not call generateSuccessor more than needed
        """

        # Recursive alpha beta value function
        # agentIndex is whose turn it is
        # depthLeft counts how many Pacman plies remain
        def ab_value(state, agentIndex, depthLeft, alpha, beta):
            # Terminal tests
            if depthLeft == 0 or state.isWin() or state.isLose():
                return self.evaluationFunction(state)

            # get legal actions
            legal = state.getLegalActions(agentIndex)
            # If no legal actions, evaluate the state
            if not legal:
                return self.evaluationFunction(state)

            # Compute next agent and possibly reduce depth after the last ghost
            # same as the Min Max
            nextAgent = agentIndex + 1
            nextDepth = depthLeft
            if nextAgent == numAgents:
                nextAgent = 0
                nextDepth = depthLeft - 1

            # Max node for Pacman
            if agentIndex == 0:
                best = float("-inf")
                # Process children exactly in the iterator order
                for action in legal:
                    succ = state.generateSuccessor(agentIndex, action)  # one call
                    val = ab_value(succ, nextAgent, nextDepth, alpha, beta)
                    if val > best:
                        best = val
                    # Alpha update
                    if best > alpha:
                        alpha = best
                    # Prune only when greater than beta
                    if best > beta:
                        return best
                return best

            # Min node for a ghost
            else:
                best = float("inf")
                for action in legal:
                    succ = state.generateSuccessor(agentIndex, action)  # one call
                    val = ab_value(succ, nextAgent, nextDepth, alpha, beta)
                    if val < best:
                        best = val
                    # Beta update
                    if best < beta:
                        beta = best
                    # Prune only when less than alpha
                    if best < alpha:
                        return best
                return best

        numAgents = gameState.getNumAgents()
        # Root decision for Pacman
        legalRoot = gameState.getLegalActions(0)

        bestValue = float("-inf")
        bestActions = []
        
        alpha = float("-inf")
        beta = float("inf")

        # Iterate in given order, keep alpha at root to allow pruning across siblings
        for action in legalRoot:
            succ = gameState.generateSuccessor(0, action)  # one call per edge
            val = ab_value(succ, 1, self.depth, alpha, beta)
            if val > bestValue:
                bestValue = val
                bestActions = [action]
            elif val == bestValue:
                bestActions.append(action)
            # Update alpha using the best value seen at the root
            if bestValue > alpha:
                alpha = bestValue
            # Only prune when bestValue is strictly greater than beta
            if bestValue > beta:
                break

        return random.choice(bestActions)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
        Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
            Returns the expectimax action using self.depth and self.evaluationFunction

            All ghosts should be modeled as choosing uniformly at random from their
            legal moves.
        """
        "*** YOUR CODE HERE ***"

        # Recursive expectimax value function
        # agentIndex is whose turn it is
        # depthLeft counts Pacman plies remaining
        def ex_value(state, agentIndex, depthLeft):
            # Terminal checks
            if depthLeft == 0 or state.isWin() or state.isLose():
                return self.evaluationFunction(state)

            legal = state.getLegalActions(agentIndex)
            if not legal:
                return self.evaluationFunction(state)

            # Next agent and depth update after last ghost
            nextAgent = agentIndex + 1
            nextDepth = depthLeft
            if nextAgent == numAgents:
                nextAgent = 0
                nextDepth = depthLeft - 1

            # Max node for Pacman
            if agentIndex == 0:
                best = float("-inf")
                for action in legal:
                    succ = state.generateSuccessor(agentIndex, action)
                    val = ex_value(succ, nextAgent, nextDepth)
                    if val > best:
                        best = val
                return best

            # Chance node for a ghost
            else:
                total = 0.0
                count = 0
                for action in legal:
                    succ = state.generateSuccessor(agentIndex, action) 
                    val = ex_value(succ, nextAgent, nextDepth)
                    total += float(val)
                    count += 1
                # Uniform expectation
                return total / float(count)

        # Root action selection for Pacman
        legalRoot = gameState.getLegalActions(0)
        numAgents = gameState.getNumAgents()

        bestValue = float("-inf")
        bestActions = []
        for action in legalRoot:
            succ = gameState.generateSuccessor(0, action)
            val = ex_value(succ, 1, self.depth)
            if val > bestValue:
                bestValue = val
                bestActions = [action]
            elif val == bestValue:
                bestActions.append(action)

        return random.choice(bestActions)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    if currentGameState.isWin():
        return float("inf")
    if currentGameState.isLose():
        return float("-inf")

    pos = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    capsules = currentGameState.getCapsules()
    ghosts = currentGameState.getGhostStates()
    scared = [ghost.scaredTimer for ghost in ghosts]

    score = float(currentGameState.getScore())

    # Handle Food Logic
    food_count = len(foodList)
    if food_count > 0:
        nearest_food = float("-inf")
        for food in foodList:
            nearest_food = min(util.manhattanDistance(pos, food), nearest_food)
        food_score = 1.0 / (nearest_food)
    else:
        food_score = 0.0
        

    # Handle Capsule Logic
    capsule_count = len(capsules)
    if capsule_count > 0:
        nearest_cap = float("-inf")
        for capsule in capsules: 
            nearest_cap = min(util.manhattanDistance(pos, capsule), nearest_cap)
        capsule_score = 1.0 / (nearest_cap + 1.0)
    else:
        capsule_score = 0.0

    # Handle Ghost Logic
    ghost_threat = 0.0
    ghost_opportunity = 0.0

    for ghost, time_scared in zip(ghosts, scared):
        dist_to_ghost = util.manhattanDistance(pos, ghost.getPosition())

        if time_scared > 0:
            # Encourage chasing scared ghosts
            ghost_opportunity += 5.0 / (dist_to_ghost + 1.0)
        else:
            # Avoid active ghosts
            if dist_to_ghost <= 1:
                ghost_threat += 100.0
            elif dist_to_ghost == 2:
                ghost_threat += 200.0

    # combination of all values
    value = (
        score
        - (4.0 * food_count)
        + 10.0 * food_score
        - 15.0 * capsule_count
        + 20.0 * capsule_score
        - 1.0 * ghost_threat
        + 15.0 * ghost_opportunity
    )

    return value

# Abbreviation
better = betterEvaluationFunction

