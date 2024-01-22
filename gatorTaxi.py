import sys
from RBT import RBT
from minHeap import MinHeap,Ride

class gatorTaxi:
    def __init__(self):
        self.min_heap = MinHeap()
        self.rbt = RBT()

    #insert a ride node
    def insert_ride(self, rideNumber, rideCost, tripDuration,output_file):
        if self.rbt.search(rideNumber) is None:
            self.min_heap.insert(rideNumber, rideCost, tripDuration)
            self.rbt.insert(rideNumber, rideCost, tripDuration)
        else:
            # print("Duplicate RideNumber.")
            output_file.write("Duplicate RideNumber\n")
   
    #print a specific ride using ride number
    def print_ride(self, rideNumber, output_file):
        node = self.rbt.search(rideNumber)
        if node is None:
            # print("(0,0,0)")
            output_file.write("(0,0,0)\n")
        else:
            # print(f"({node.rideNumber},{node.rideCost},{node.tripDuration})")
            output_file.write(f"({node.rideNumber},{node.rideCost},{node.tripDuration})\n")
    
    #print rides on a specific range
    def print_rides(self, rideNumber1, rideNumber2, output_file):
        nodes = self.rbt.search_range(rideNumber1, rideNumber2)
        if len(nodes) == 0:
            # print("(0,0,0)")
            output_file.write("(0,0,0)\n")
        else:
            ride_str = ""
            for node in nodes:
                ride_str += f"({node.rideNumber},{node.rideCost},{node.tripDuration}),"
            ride_str = ride_str[:-1]  # remove trailing comma and space
            # print(ride_str)
            output_file.write(ride_str + "\n")
   
    #update the Ride if destination changed
    def update_trip_duration(self, rideNumber, newTripDuration):
        node = self.rbt.search(rideNumber)
        if node is None:
            return
        if newTripDuration <= node.tripDuration:  
            node.tripDuration = newTripDuration
            self.min_heap.update(node.rideNumber, node.rideCost, node.tripDuration)
            return
        elif newTripDuration <= 2 * node.tripDuration:
            node.rideCost += 10
            node.tripDuration = newTripDuration
            self.min_heap.update(node.rideNumber, node.rideCost, node.tripDuration)
        else:
            self.cancel_ride(rideNumber)
    
    #delete the ride using ride number
    def cancel_ride(self, rideNumber):
        node = self.rbt.search(rideNumber)
        if node is None:
            return
        self.rbt.delete(node)
        self.min_heap.delete(rideNumber)

    #get the ride with lowet cost
    def get_next_ride(self, output_file):
        node = self.min_heap.remove_min()
        if node is None:
            # print("No active ride requests")
            output_file.write("No active ride requests\n")
        else:
            # print(f"({node.rideNumber},{node.rideCost},{node.tripDuration})")
            output_file.write(f"({node.rideNumber},{node.rideCost},{node.tripDuration})\n")
            self.rbt.delete(self.rbt.search(node.rideNumber))


def main():
    if len(sys.argv) < 2:
        # print("Enter input and output file names and try again!!")
        return
    input_file= sys.argv[1]
    output_file = "output_file.txt"

    with open(input_file, "r") as f, open(output_file, "w") as output_file:
        lines =f.readlines()

        for line in lines:
            command, args = line.strip().split('(')
            args = (args.replace(')',""))
            
            #using if - else statement to check the commannd
            if command != "GetNextRide":
                argsList = list(map(int, args.split(',')))
            
            if command == "Insert":
                rideNumber = int(argsList[0])
                rideCost = int(argsList[1])
                tripDuration = int(argsList[2])
                gator_taxi.insert_ride(rideNumber, rideCost, tripDuration, output_file)
            elif command == "Print":
                if len(argsList) == 1:
                    rideNumber = int(argsList[0])
                    gator_taxi.print_ride(rideNumber, output_file)
                elif len(argsList) == 2:
                    rideNumber1 = int(argsList[0])
                    rideNumber2 = int(argsList[1])
                    gator_taxi.print_rides(rideNumber1, rideNumber2, output_file)
            elif command == "UpdateTrip":
                rideNumber = int(argsList[0])
                newTripDuration = int(argsList[1])
                gator_taxi.update_trip_duration(rideNumber, newTripDuration)
            elif command == "GetNextRide":
                gator_taxi.get_next_ride(output_file)
            elif command == "CancelRide":
                rideNumber = int(argsList[0])
                gator_taxi.cancel_ride(rideNumber)

if __name__ == "__main__":
    gator_taxi = gatorTaxi()
    main()


