import copy
#from main import print_process_result


def print_process_result(process_list):
    # Print headers
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority':<10}{'Final Time':<15}{'Turnaround Time':<20}{'Waiting Time':<15}")
    print("-" * 90)
    
    # Print each process in the table
    for p in process_list:
        print(f"{p['process']:<10}{p['arrival_time']:<15}{p['burst_time']:<15}{p['priority']:<10}{p['final_time']:<15}{p['turnaround_time']:<20}{p['waiting_time']:<15}")


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

def checkArrivalTime(process_list, current_time, ready_queue):
    unarranged_process = []

    for process in process_list:
        if process['arrival_time'] == current_time:
            unarranged_process.append(process)

    if unarranged_process:
        arranged_process = sorted(unarranged_process, key=lambda x: x['arrival_time'])

        for proc in arranged_process:
            ready_queue.append(proc['process'])
    
    return ready_queue

def SRT(process_list, available_process):
    ready_queue = []
    current_time = 0
    temp_process_list = copy.deepcopy(process_list)
    gantt_chart = []
    last_process = None  # Track the last process executed

    while available_process:
        ready_queue = checkArrivalTime(process_list, current_time, ready_queue)

        ready_queue.sort(key=lambda x: (temp_process_list[x]['burst_time'], process_list[x]['arrival_time']))

        if ready_queue:

            current_process = ready_queue[0]
            if last_process != current_process:
                if last_process is not None:
                    gantt_chart[-1]['end_time'] = current_time

                gantt_chart.append({
                    'process': current_process,
                    'start_time': current_time,
                    'end_time': current_time + 1
                })
                last_process = current_process

            temp_process_list[current_process]['burst_time'] -= 1

            if temp_process_list[current_process]['burst_time'] == 0:

                process_list[current_process]['final_time'] = current_time + 1
                process_list[current_process]['turnaround_time'] = process_list[current_process]['final_time'] - process_list[current_process]['arrival_time']
                process_list[current_process]['waiting_time'] = process_list[current_process]['turnaround_time'] - process_list[current_process]['burst_time']

                available_process.remove(current_process)
                ready_queue.remove(current_process)

                gantt_chart[-1]['end_time'] = current_time + 1
                last_process = None  # Reset last process

        else:
            if gantt_chart and gantt_chart[-1]['process'] == '-':
                gantt_chart[-1]['end_time'] = current_time + 1  # Extend the existing gap
            else:
                # Add a new gap
                gantt_chart.append({
                    'process': '-',
                    'start_time': current_time,
                    'end_time': current_time + 1
                })

        current_time += 1


    Gantt_chart_display(gantt_chart)
    print_process_result(process_list)

    print("\n")

    total_turnaround_time = sum(p['turnaround_time'] for p in process_list)
    total_waiting_time = sum(p['waiting_time'] for p in process_list)
    num_processes = len(process_list)

    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes

    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Total Waiting Time: {total_waiting_time}")

    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.3f}")
    print(f"Average Waiting Time: {avg_waiting_time:.3f}\n")

    print("\nSRT Scheduling Ended\n")
