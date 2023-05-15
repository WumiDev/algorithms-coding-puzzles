from itertools import combinations

def find_group_efficiency(worker_efficiencies):
    num_workers = len(workers)
    min_task_cost = float('inf')

    for i in range(num_workers):
        excluded_worker = workers[i]
        remaining_workers = workers[:i] + workers[i+1:]
        num_pairs = len(remaining_workers) // 2
        all_pairs = list(combinations(remaining_workers, 2))
        pair_costs = [abs(pair[0]-pair[1]) for pair in all_pairs]
        sorted_pairs = [p for _, p in sorted(zip(pair_costs, all_pairs))]
        best_pairs = sorted_pairs[:num_pairs]
        best_pairs_cost = sum([abs(pair[0]-pair[1]) for pair in best_pairs])
        print(f"\nExcluded worker: {excluded_worker}")
        # print(f"All pairs: {all_pairs}")
        print(f"Best pairs: {best_pairs}")
        print(f"Best pairs cost: {best_pairs_cost}")
        if best_pairs_cost < min_task_cost:
            min_task_cost = best_pairs_cost
            
    print(f"\nMinimum cost: {min_task_cost}")
    
    return min_task_cost

# Test Codes:
# worker_efficiencies = [1,2,4]
# worker_efficiencies = [4,2,8,1,9]
worker_efficiencies = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
min_cost = find_group_efficiency(worker_efficiencies)
# print(f"Minimum cost: {min_cost}")

    