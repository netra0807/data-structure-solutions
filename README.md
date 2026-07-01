# Data Structures Solutions in Python

This repository contains clear Python implementations for foundational data structure problems.

## 📋 Problems & Challenges

### C1) The Attendance System (Direct Access Array)
* *Problem:* Design a system where every student has a fixed slot (index). The teacher must be able to directly log or view any student's attendance without checking previous records.
* *Core Concept:* Array Direct Access with O(1) efficiency.

### C2) The Undo Machine (LIFO Stack)
* *Problem:* Build a lightweight text editor backend where actions can be reversed when a user triggers an undo action.
* *Core Concept:* Stack Data Structure (Last-In, First-Out).

### C3) The Smart Printer Queue (Priority/Dual Queue)
* *Problem:* Design an office printer system that processes documents in order, but forces jobs marked as URGENT to leapfrog standard files.
* *Core Concept:* Queue Data Structure (First-In, First-Out) using independent queues.
*

## Python Data Structure Solutions

This repository now features beginner-friendly Python implementations for three distinct situational problems using fundamental data structures.

### 1. Amazon Conveyor Belt (Fixed Array)
* *File:* conveyor_belt.py
* *Concept:* Uses a fixed-size array (List initialized to 8 slots) to store product strings or None values.
* *Operations:* 
  * Direct index access ($O(1)$ time complexity) to check or update slots.
  * Linear search ($O(N)$ time complexity) to find specific products.

### 2. Toll Plaza Simulation (Circular Queue)
* *File:* toll_plaza.py
* *Concept:* Utilizes fixed memory sizing for 5 vehicles by leveraging front and rear pointers.
* *Key Logic:* Employs the modulo operator (%) to enable pointers to circularly wrap around the array slots, efficiently reusing memory as cars exit the queue.

### 3. GPS Navigation Trail (Two-Stack History)
* *File:* gps_navigation.py
* *Concept:* Tracks forward and backward movement seamlessly like a standard web browser.
* *Key Logic:* Implements an asynchronous tracking workflow using history_stack for backtracking and forward_stack to hold alternative paths. Moving to a new location explicitly clears out the forward stack history.
*