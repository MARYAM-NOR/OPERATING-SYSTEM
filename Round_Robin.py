import math
from collections import deque
import copy

from main import print_process_result

def checkArrivalTime(process_list, current_time, ready_queue):
    unarranged_process = []

    for process in process_list:
        if process['arrival_time'] == current_time:
            unarranged_process.append(process)
            
    if unarranged_process:
        unarranged_process = [proc for proc in unarranged_process if proc['process'] not in ready_queue]

        if unarranged_process:
            arranged_process = sorted(unarranged_process, key=lambda x: x['priority'])

            for proc in arranged_process:
                ready_queue.append(proc['process'])

    return ready_queue

def Gantt_chart_display(gantt_chart):
    print("\nGantt Chart:")
    
    # Define the border components
    first_border = "|" + "-" * 12 + "|"
    middle_border = "-" * 12 + "|"
    end_border = "-" * 12 + "|"

    # Create the top border (a lot of dashes)
    print("-" * (13 * len(gantt_chart)))

    for index, entry in enumerate(gantt_chart):
        if index == 0:
            if entry['process'] == '-':
                print(f"|{' ' * 5}{'--'}{' ' * 5}", end="|")
            else:
                print(f"|{' ' * 5}P{entry['process']}{' ' * 5}|", end="")
        elif index == len(gantt_chart) - 1:
            if entry['process'] == '-':
                print(f" " * 5 + f"{'-'}" + f" " * 5 + "|", end="")
            else:
                print(f" " * 5 + f"P{entry['process']}" + f" " * 5 + "|", end="")
        else:
            if entry['process'] == '-':
                print(f" " * 5 + f"{'-'}" + f" " * 5 + "|", end="")
            else:
                print(f" " * 5 + f"P{entry['process']}" + f" " * 5 + "|", end="")
    
    print("") 

    process_string = ""# Print the bottom border (a lot of dashes)
    print("-" * (13 * len(gantt_chart)))

    for index, entry in enumerate(gantt_chart):
        if index == 0:
            process_string += f"{entry['start_time']}" + " " * 12 + f"{entry['end_time']}"
        elif index == len(gantt_chart) - 1:
            if len(str(entry['end_time'])) == 1:  # Convert to string before checking length
                process_string += " " * 12 + f"{entry['end_time']}"
            else:
                process_string += " " * 11 + f"{entry['end_time']}"
        else:
            if len(str(entry['end_time'])) == 1:  # Convert to string before checking length
                process_string += " " * 12 + f"{entry['end_time']}"
            else:
                process_string += " " * 11 + f"{entry['end_time']}"

    print(process_string)
    print("\n")


def Round_Robin(process_list, available_process, quantumMax):
    ready_queue = deque()
    current_time = 0
    ready_queue = checkArrivalTime(process_list, current_time, ready_queue)

    current_quantum = 0
    temp_process_list = copy.deepcopy(process_list)
    gantt_chart = []
    
    while available_process:
        if ready_queue:
            current_quantum += 1
            current_time += 1

            current_process = int(ready_queue[0])
            temp_process_list[current_process]['burst_time'] -= 1

            if temp_process_list[current_process]['burst_time'] == 0:
                available_process.remove(current_process)

            if current_quantum == quantumMax or temp_process_list[current_process]['burst_time'] == 0:
                gantt_chart.append({
                    'process': current_process,
                    'start_time': current_time - current_quantum,
                    'end_time': current_time
                })

            if temp_process_list[current_process]['burst_time'] == 0:
                process_list[current_process]['final_time'] = current_time
                process_list[current_process]['turnaround_time'] = process_list[current_process]['final_time'] - process_list[current_process]['arrival_time']
                process_list[current_process]['waiting_time'] = process_list[current_process]['turnaround_time'] - process_list[current_process]['burst_time']

            ready_queue = checkArrivalTime(process_list, current_time, ready_queue)

            if current_quantum == quantumMax or temp_process_list[current_process]['burst_time'] == 0:
                ready_queue.popleft()
                current_quantum = 0

            if temp_process_list[current_process]['burst_time'] != 0 and current_quantum == 0:
                ready_queue.append(current_process)
        else:
            idle_start = current_time
            while not ready_queue and available_process:
                current_time += 1
                ready_queue = checkArrivalTime(process_list, current_time, ready_queue)
            gantt_chart.append({
                'process': '-',
                'start_time': idle_start,
                'end_time': current_time
            })
    
    print("\n")
    Gantt_chart_display(gantt_chart)
    print_process_result(process_list)
    print("\n")
    
    # Calculate and print average turnaround time and waiting time
    total_turnaround_time = sum(p['turnaround_time'] for p in process_list)
    total_waiting_time = sum(p['waiting_time'] for p in process_list)
    num_processes = len(process_list)

    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes

    print(f"Total turnaround time: {total_turnaround_time}")
    print(f"Total waiting time: {total_waiting_time}")
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.3f}")
    print(f"Average Waiting Time: {avg_waiting_time:.3f}\n")
