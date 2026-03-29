# 4210Project1

## What is Simulated Annealing?
- A hill-climbing algorithm that never makes “downhill” moves toward states with
lower value (or higher cost) is guaranteed to be incomplete, because it can get
stuck on a local maximum.
- In contrast, a purely random walk—that is, moving to a successor chosen
uniformly at random from the set of successors—is complete but extremely
inefficient.
- Therefore, it seems reasonable to try to combine hill climbing with a random walk
in some way that yields both efficiency and completeness.
-  Simulated Annealing is such an algorithm.

## Strategy (What to Implement)
Use Simulated Annealing to search over permutations of jobs. You will define:
- A successor (neighbor) function over permutations (e.g., swap, insertion, 2-opt).
- A value/cost function = makespan of the job sequence.
- A temperature schedule (initial T, cooling rate α, iterations per temperature,
stopping conditions).
