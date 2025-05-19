import math
from collections import deque
import copy
from Round_Robin import *
from SJN import SJN
from SRT import SRT
from NP_Priority import non_preemptive_priority

# Function to get inputs for processes
def get_process_list(processes):
    while True:
        try:
            arrival_times_input = input("Enter the arrival times (space-separated): ")
            arrival_times = [int(x) for x in arrival_times_input.split()]
            if len(arrival_times) != processes:
                raise ValueError("Number of arrival times must match the number of processes.")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            burst_times_input = input("Enter the burst times (space-separated): ")
            burst_times = [int(x) for x in burst_times_input.split()]
            if len(burst_times) != processes:
                raise ValueError("Number of burst times must match the number of processes.")
            if any(bt <= 0 for bt in burst_times):
                raise ValueError("Burst times must be positive integers.")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            priorities_input = input("Enter the priorities (space-separated): ")
            priorities = [int(x) for x in priorities_input.split()]
            if len(priorities) != processes:
                raise ValueError("Number of priorities must match the number of processes.")
            if any(p <= 0 for p in priorities):
                raise ValueError("Priorities must be positive integers.")
            break
        except ValueError as e:
            print(e)

    process_list = []

    for i in range(processes):
        process_list.append({
            'process': i,
            'arrival_time': arrival_times[i],
            'burst_time': burst_times[i],
            'final_time': 0,  # placeholder
            'priority': priorities[i],
            'turnaround_time': 0,
            'waiting_time': 0
        })
    
    return process_list

def print_process_list(process_list):
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority':<10}")
    for idx, process in enumerate(process_list):
        print(f"{idx :<10}{process['arrival_time']:<15}{process['burst_time']:<15}{process['priority']:<10}")

def print_process_result(process_list):
    # Print headers
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Priority':<10}{'Final Time':<15}{'Turnaround Time':<20}{'Waiting Time':<15}")
    print("-" * 90)
    
    # Print each process in the table
    for p in process_list:
        print(f"{p['process']:<10}{p['arrival_time']:<15}{p['burst_time']:<15}{p['priority']:<10}{p['final_time']:<15}{p['turnaround_time']:<20}{p['waiting_time']:<15}")

def choose_algorithm(process_list, available_process):
    while True:
        print("\nChoose a scheduling algorithm or other options:")
        print("\n")
        print("1. Shortest Job Next (SJN)")
        print("2. Shortest Remaining Time (SRT)")
        print("3. Round Robin")
        print("4. Non-preemptive Priority")
        print("5. Change Process (Input new processes)")
        print("6. Exit")
        print("\n")
        
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("\nYou chose Shortest Job Next (SJN)")
            SJN(process_list, available_process)
        elif choice == '2':
            print("\nYou chose Shortest Remaining Time (SRT)")
            SRT(process_list, available_process)
        elif choice == '3':
            print("\nYou chose Round Robin")
            
            while True:  # Loop until a valid integer is entered
                try:
                    quantumMax = int(input("Enter the quantumMax value (integer only): "))
                    if quantumMax > 0:
                        break
                    else:
                        print("Quantum time must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            Round_Robin(process_list, available_process, quantumMax)
        elif choice == '4':
            print("\nYou chose Non-preemptive Priority")
            non_preemptive_priority(process_list, available_process)
        elif choice == '5':
            print("\nYou chose to change the process list.")
            return 'change_process'  # Signal to change the process list
        elif choice == '6':
            print("\nExiting the program. Goodbye!")
            return 'exit'  # Signal to exit the program
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def main():
    while True:  # Main loop to keep the program running
        processes = 0

        while True:
            try:
                processes = int(input("Enter the number of processes (3 to 10): "))
                if processes < 3 or processes > 10:
                    raise ValueError("Number of processes must be between 3 and 10.")
                break
            except ValueError as e:
                print(e)

        process_list = get_process_list(processes)
        print("\nInitial process list:")
        print_process_result(process_list)

        available_process = [i for i in range(processes)]

        while True:
            result = choose_algorithm(process_list, available_process)
            if result == 'change_process':
                break  # Go back to the start of the main loop to get new processes
            elif result == 'exit':
                return  # Exit the program

if __name__ == "__main__":
    main()