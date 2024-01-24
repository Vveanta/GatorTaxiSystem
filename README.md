# README: Gator Taxi System

## Introduction
The Gator Taxi System is a sophisticated ride-hailing application designed to efficiently manage and process ride requests. Utilizing advanced data structures such as the Min Heap and Red-Black Tree (RBT), the system offers an optimized approach for handling ride allocations and driver assignments. This project demonstrates the practical application of these data structures in a real-world scenario, showcasing their effectiveness in optimizing operations and improving overall service quality.

## Objectives
The primary objectives of the Gator Taxi System are:
- To efficiently manage ride requests and driver allocations.
- To demonstrate the practical use of Min Heaps and Red-Black Trees in a real-world application.
- To provide a user-friendly interface for both riders and drivers.
- To ensure timely and efficient ride services.

## Installation and Setup
To set up the Gator Taxi System, follow these steps:
1. Clone the repository from GitHub
2. Navigate to the cloned directory
3. Ensure Python 3 is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
```zsh
git clone git@github.com:Vveanta/GatorTaxiSystem.git
cd GatorTaxiSystem
```

## Running the Code
To run the Gator Taxi System, execute the following steps:
1. Open a terminal or command prompt in the GatorTaxiSystem directory.
2. Use the Makefile to compile and run the program:
```zsh
make run input_file_name=input.txt
```
3. The system will process the input file and generate an output in "output_file.txt".

## Usage

### Input Format
The input file (e.g., "input.txt") should contain ride requests in the following format:
- &lt;RequestID&gt; &lt;PickupTime&gt; &lt;PickupLocation&gt; &lt;DropoffLocation&gt; &lt;RiderID&gt;

### Output Format
The output file ("output_file.txt") will include the details of ride allocations:
- &lt;RequestID&gt; &lt;DriverID&gt; &lt;PickupTime&gt; &lt;DropoffTime&gt;

