# Sree Kona : ssk0189
# Zachary Wehbe : zw0140


import random
import math


def allocate_ops_to_machines(job_sequence, proc_times,M):
    numJobs = len(job_sequence)
    numOps = len(process_times[0])

    machine_available = [0] * M

    job_available = [0] * len(process_times)

    schedule = []

    for job in job_sequence:
        for p in range(ops):
            machine = p % M

            start = max(machine_available[machine], job_available[job])
            end = start + process_times[job][p]

            schedule.append({
                "job": job,
                "operation": p,
                "machine": machine,
                "start": start,
                "end": end
            })

            machine_available[machine] = end
            job_available[job] = end

    return schedule 

def simulated_annealing(job_sequence, proc_times, M):
    pass

def compute_makespan(schedule):
    pass







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
