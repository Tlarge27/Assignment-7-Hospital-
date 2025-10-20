class Patient:
    def __init__(self, name, urgency):
        self.name = name 
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"
    

class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        min_patient = self.data[0]
        last_patient = self.data.pop()
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)
        return min_patient

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Riley", 2))

    heap.print_heap()
    print("\nNext up:", heap.peek())

    served = heap.remove_min()
    print("\nServed:", served.name)
    heap.print_heap()

# This Queue is a min heap that manages a list of patients based on the urgency there is to see them. 
# Each patient is named and given a score from 1-10 based on how urgent their case is. the lower the urgency number the higher they 
# are placed on the list, meaning a score of 10 would be least urgant and a score of 1 being the most urgent. 
# The use of the Min heap here is to always keep the patient who is most urgent at the top. 
# When a new patient arrives they are inserted into the pool of patients the heap pulls from. 
# When a patient has been treated you can use remove_min to take them off the top of the list 
# You are also able to view the entire list by viewing the heap or just the patient that is next in line by using peek. 
# 
# Heaps help real time systems like an emergency room intake by always keeping the most important thing on a to do list first. 
#
#
#
#
#