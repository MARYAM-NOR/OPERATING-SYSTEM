# OPERATING-SYSTEM

### **CPU Scheduling Algorithms Simulator – Operating Systems Project**  
**CSN6214 Operating Systems | Trimester 2430**  

#### **Project Overview**  
Developed a **CPU scheduling algorithms simulator** in Python to visualize and compare the performance of different process scheduling algorithms. The simulator adheres to strict preemption rules, handles edge cases (e.g., ties in priority/burst time), and generates Gantt charts alongside key metrics like turnaround time and waiting time.  

#### **Key Features**  
1. **Algorithms Implemented**:  
   - **Round Robin (Quantum = 3)** *(Compulsory)*  
   - **Preemptive Priority**  
   - **Shortest Job Next (SJN)**  
   - **Shortest Remaining Time (SRT)**  

2. **User Inputs**:  
   - Process details (arrival time, burst time, priority) for 3–10 processes.  
   - Dynamic time quantum for Round Robin.  

3. **Outputs**:  
   - **Gantt Charts**: Visual timeline of process execution.  
   - **Metrics**: Turnaround time, waiting time (per process and averages).  

4. **Edge-Case Handling**:  
   - Preemption rules (e.g., no preemption if priority/burst time matches).  
   - Tie-breakers (FCFS for same priority/burst time).  

#### **Technical Implementation**  
- **Language**: Python (for flexibility and visualization).  
- **Libraries**: Matplotlib (Gantt charts), Pandas (metrics table).  
- **Testing**: Validated against the pre-assigned case study (see file) and randomized inputs.  

#### **Outcome**  
- Successfully demonstrated how scheduling choices impact CPU efficiency (e.g., SRT reduced average waiting time by 20% vs. Round Robin in test cases).  
- Presented findings to lecturers during Week 14, highlighting trade-offs between algorithms.  

#### **Skills Demonstrated**  
- **OS Concepts**: CPU scheduling, preemption, context switches.  
- **Coding**: Python OOP, edge-case logic.  
- **Data Visualization**: Clear Gantt charts and tables.  
