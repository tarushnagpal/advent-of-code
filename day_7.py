from networkx import DiGraph, lexicographical_topological_sort as lt_sort
with open('files/day_7_input.txt') as f:
    lines = [ inp.strip() for inp in f]


import networkx as nx

def solve(lines):
    G = nx.DiGraph()
    for line in lines:
        parts = line.split(" ")
        G.add_edge(parts[1], parts[7])
    print(''.join(nx.lexicographical_topological_sort(G)))
    task_times = []
    tasks = []
    time = 0
    while task_times or G:
        available_tasks = [t for t in G if t not in tasks and G.in_degree(t) == 0]
        if available_tasks and len(task_times) < 5:
            task = min(available_tasks)  # min gets smallest task alphabetically
            task_times.append(ord(task) - 4)
            tasks.append(task)
        else:
            min_time = min(task_times)
            completed = [tasks[i] for i, v in enumerate(task_times) if v == min_time]
            task_times = [v - min_time for v in task_times if v > min_time]
            tasks = [t for t in tasks if t not in completed]
            time += min_time
            G.remove_nodes_from(completed)

    print(time)

solve(lines)