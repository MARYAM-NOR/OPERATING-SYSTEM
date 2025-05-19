import copy

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

def non_preemptive_priority(process_list, available_process):
    temp_process_list = copy.deepcopy(process_list)
    
    temp_process_list.sort(key=lambda x: x['arrival_time'])
    
    current_time = 0
    completed_processes = []
    gantt_chart = []  
    
    while available_process:
        ready_processes = [p for p in temp_process_list if p['arrival_time'] <= current_time and p['burst_time'] > 0]
        
        if not ready_processes:
            # No process is ready, check if the last Gantt entry is a gap
            if gantt_chart and gantt_chart[-1]['process'] == '-':
                gantt_chart[-1]['end_time'] = current_time + 1  # Extend the existing gap
            else:
                # Add a new gap if none exists
                gantt_chart.append({
                    'process': '-',
                    'start_time': current_time,
                    'end_time': current_time + 1
                })
            current_time += 1
            continue

        selected_process = min(ready_processes, key=lambda x: x['priority'])
        
        start_time = current_time
        
        current_time += selected_process['burst_time']
        end_time = current_time
        
        selected_process['final_time'] = current_time
        selected_process['turnaround_time'] = selected_process['final_time'] - selected_process['arrival_time']
        selected_process['waiting_time'] = selected_process['turnaround_time'] - selected_process['burst_time']
        
        selected_process['burst_time'] = 0
        
        available_process.remove(selected_process['process'])
        
        completed_processes.append(selected_process)
        
        gantt_chart.append({
            'process': selected_process['process'],
            'start_time': start_time,
            'end_time': end_time
        })
    
    Gantt_chart_display(gantt_chart)
    print_process_result(temp_process_list)

    print("\n")

    # Calculate and print average turnaround time and waiting time
    total_turnaround_time = sum(p['turnaround_time'] for p in temp_process_list)
    total_waiting_time = sum(p['waiting_time'] for p in temp_process_list)
    num_processes = len(temp_process_list)

    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes

    print(f"total turnaround time: {total_turnaround_time}")
    print(f"total waiting time: {total_waiting_time}")

    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.3f}")
    print(f"Average Waiting Time: {avg_waiting_time:.3f}\n")

    print("\n NP Priority Scheduling Ended \n")
