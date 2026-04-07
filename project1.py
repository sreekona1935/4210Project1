# Sree Kona : ssk0189
# Zachary Wehbe : zw0140


import random
import math


def allocate_ops_to_machines(job_sequence, proc_times,M):

    #declare number of jobs and operations based on input data
    numJobs = len(job_sequence)
    numOps = len(proc_times[0])

    #array storing what mechine is available at what time, initialized to 0 for all machines
    machine_available = [0] * M

    #array storing when each job is available to be processed, initialized to 0 for all jobs
    job_available = [0] * len(proc_times)

    schedule = []

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
    return allocate_ops_to_machines(job_sequence, proc_times, M)


def compute_makespan(schedule):
    return max(op["end"] for op in schedule)



def main():
    # Example usage
    job_sequence = [0, 1, 2]  # Job IDs
    proc_times = [[3, 2, 4], [2, 3, 1], [4, 1, 2]]  #processing times for each job on each machine
    M = 3  #number of machines

    schedule = allocate_ops_to_machines(job_sequence, proc_times, M)
    print("Initial Schedule:", schedule)

    optimized_schedule = simulated_annealing(job_sequence, proc_times, M)
    print("Optimized Schedule:", optimized_schedule)

    makespan = compute_makespan(optimized_schedule)
    print("Makespan of Optimized Schedule:", makespan)

main()
