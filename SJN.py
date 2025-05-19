import math

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



def SJN(process_list, available_process):
    print("\n Shortest Job Next (SJN) Scheduling \n")
    current_time = 0
    completed_count = 0
    gantt_chart = []

    while completed_count < len(process_list):
        # Get processes that have arrived and are available
        ready_processes = [
           p for p in process_list if p['arrival_time'] <= current_time and p['process'] in available_process
        ]

        if ready_processes:
            # Select the process with the shortest burst time
            next_process = min(ready_processes, key=lambda x: x['burst_time'])
            process_index = next_process['process']

            # Execute the selected process
            start_time = current_time
            end_time = start_time + next_process['burst_time']
            current_time = end_time

            # Update the process data
            next_process['final_time'] = end_time
            next_process['turnaround_time'] = end_time - next_process['arrival_time']
            next_process['waiting_time'] = next_process['turnaround_time'] - next_process['burst_time']

            # Add the process to Gantt chart
            gantt_chart.append({'process': process_index, 'start_time': start_time, 'end_time': end_time})

            # Mark the process completed (remove it from available_process)
            available_process.remove(process_index)
            completed_count += 1
            
        else:
            # No process is ready, check if the last entry is a gap
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

    Gantt_chart_display(gantt_chart)
    # Print process table
    print_process_result(process_list)

    print("\n")

    # Calculate and print average turnaround time and waiting time
    total_turnaround_time = sum(p['turnaround_time'] for p in process_list)
    total_waiting_time = sum(p['waiting_time'] for p in process_list)
    num_processes = len(process_list)

    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes

    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Total Waiting Time: {total_waiting_time}")

    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.3f}")
    print(f"Average Waiting Time: {avg_waiting_time:.3f}\n")

    print("\n Shortest Job Next (SJN) Scheduling Ended \n")

