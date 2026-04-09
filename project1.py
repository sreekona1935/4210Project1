# Sree Kona : ssk0189
# Zachary Wehbe : zw0140


import random
import math
import sys


def allocate_ops_to_machines(job_sequence, proc_times,M):

    #declare number of jobs and operations based on input data
    numJobs = len(job_sequence)
    numOps = len(proc_times[0])

    #array storing what mechine is available at what time, initialized to 0 for all machines
    machine_available = [0] * M

    #array storing when each job is available to be processed, initialized to 0 for all jobs
    job_available = [0] * len(proc_times)

    schedule = []

    #iterate through the job sequence
    for job in job_sequence:
        for p in range(numOps):
            machine = p % M

            start = max(machine_available[machine], job_available[job])
            end = start + proc_times[job][p]

            schedule.append({
                "job": job,
                "operation": p,
                "machine": machine,
                "start": start,
                "end": end
            })

            #free the machine and job after processing the operation
            machine_available[machine] = end
            job_available[job] = end

    return schedule 

def simulated_annealing(job_sequence, proc_times, M):
    T = 1000  # Initial temperature
    coolingRate = 0.95  # Cooling rate
    iter = 100
    T_min = 0.01

    #randomly swap two jobs in the sequence to create a new candidate solution
    swap_jobs(job_sequence)

    current_sequence = job_sequence[:]
    current_cost = compute_makespan(allocate_ops_to_machines(job_sequence, proc_times, M))
    best_sequence = current_sequence[:]
    best_cost = current_cost

    #main loop of the simulated annealing algorithm, continues until the temperature drops below a minimum threshold
    while T > T_min:

        #iterate a fixed number of times at each temperature level to explore the solution space
        for it in range(iter):
            
            neighbor_sequence = swap_jobs(current_sequence)
            neighbor_cost = compute_makespan(allocate_ops_to_machines(neighbor_sequence, proc_times, M))

            #compare the cost of the current solution with the cost of the neighbor solution
            C = current_cost - neighbor_cost
            if C > 0 or math.exp(C / T) > random.random():
                current_sequence = neighbor_sequence
                current_cost = neighbor_cost
            else:
                #random float from 0 - 1
                r = random.random()
                if r < 2.71828 ** (C / T):
                    current_sequence = neighbor_sequence
                    current_cost = neighbor_cost
            
            #track the best solution found so far
            if current_cost < best_cost:
                best_sequence = current_sequence[:]
                best_cost = current_cost
        #cool down the temperature after each iteration
        T *= coolingRate
    #return best sequence found
    return best_sequence, allocate_ops_to_machines(best_sequence, proc_times, M)

#function to randomly swap two jobs in the sequence to create a new candidate solution
def swap_jobs(job_sequence):
    new_sequence = job_sequence[:]
    idx1, idx2 = random.sample(range(len(job_sequence)), 2)
    new_sequence[idx1], new_sequence[idx2] = new_sequence[idx2], new_sequence[idx1]
    return new_sequence

#function to compute the makespan of a given schedule by finding the maximum end time of all operations in the schedule
def compute_makespan(schedule):
    return max(op["end"] for op in schedule)



def main():
    if len(sys.argv) != 2:
        print("Usage: python project1.py <proc_times.txt>")
        sys.exit(1)
    
    input_file = sys.argv[1]

    # To make results repeatable
    random.seed(11)
    #read processing times from file and store in a 2D list
    proc_times = []
    with open(input_file, "r") as file:
        for line in file:
            proc_times.append(list(map(int, line.split(',')))[1:])
    job_sequence = list(range(len(proc_times)))  #initial job sequence based on the number of jobs
    M = input("Enter the number of machines: ")  #number of machines input by user
    M = int(M)

    current_schedule = allocate_ops_to_machines(job_sequence, proc_times, M)
    print("Current Job Sequence:", job_sequence)
    print("Current Schedule:")
    for op in current_schedule:
        print(f"  Job {op['job']}, Operation {op['operation']}, Machine {op['machine']}, Start {op['start']}, End {op['end']}")
    print("Current Makespan:", compute_makespan(current_schedule))

    print("\n")

    best_sequence, best_schedule = simulated_annealing(job_sequence, proc_times, M)
    print("Best Job Sequence:", best_sequence)
    print("Best Schedule:")
    for op in best_schedule:
        print(f"  Job {op['job']}, Operation {op['operation']}, Machine {op['machine']}, Start {op['start']}, End {op['end']}")
    print("Best Makespan:", compute_makespan(best_schedule))

    print(compute_makespan(current_schedule) - compute_makespan(best_schedule), "less than the initial solution.")

main()
