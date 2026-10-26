
class Patient:
    def __init__(self, name, urgency):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name must be a non-empty string.")

        if isinstance(urgency, bool) or not isinstance(urgency, int):
            raise TypeError("Urgency must be an integer from 1 to 10.")

        if urgency < 1 or urgency > 10:
            raise ValueError("Urgency must be between 1 and 10.")

        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = (
                    self.data[parent],
                    self.data[index],
                )
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and self.data[left].urgency < self.data[smallest].urgency
            ):
                smallest = left

            if (
                right < size
                and self.data[right].urgency < self.data[smallest].urgency
            ):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            index = smallest

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be inserted.")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            raise IndexError("Cannot peek at an empty queue.")

        return self.data[0]

    def remove_min(self):
        if not self.data:
            raise IndexError("Cannot remove from an empty queue.")

        if len(self.data) == 1:
            return self.data.pop()

        highest_priority = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return highest_priority

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0


heap = MinHeap()

# Insert patients into the emergency queue.
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.insert(Patient("Riley", 2))

# Display the queue.
heap.print_heap()

# Check the next patient without removing them.
next_up = heap.peek()
print(f"\nNext patient: {next_up.name} ({next_up.urgency})")

# Remove and serve the highest-priority patient.
served = heap.remove_min()
print(f"\nPatient served: {served.name}")

# Display the remaining queue.
heap.print_heap()

# Remove all remaining patients in priority order.
print("\nServing remaining patients:")
while not heap.is_empty():
    patient = heap.remove_min()
    print(f"- {patient.name} ({patient.urgency})")
