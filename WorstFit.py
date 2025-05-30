class MemoryAllocator:
    def __init__(self, processes, blocks):
        self.processes = processes
        self.blocks = blocks
        self.allocation = [-1] * len(processes)
        self.internal_fragmentation = 0
        self.external_fragmentation = 0

    def worst_fit(self):
        available_blocks = list(self.blocks)

        for i in range(len(self.processes)):
            worst_block_idx = -1
            worst_fit_size = -1

            for j in range(len(available_blocks)):
               
                if available_blocks[j] >= self.processes[i] and available_blocks[j] - self.processes[i] > worst_fit_size:
                    worst_block_idx = j
                    worst_fit_size = available_blocks[j] - self.processes[i]

            
            if worst_block_idx != -1:
                self.allocation[i] = worst_block_idx
                self.internal_fragmentation += available_blocks[worst_block_idx] - self.processes[i]
                available_blocks[worst_block_idx] -= self.processes[i]
            else:
                
                self.external_fragmentation += self.processes[i]

    def display_allocation(self):
        print("\n**************************************************************")
        print("Process ID\tProcess Size\tBlock number")
        for i in range(len(self.processes)):
            print(f"     {i + 1}\t\t  {self.processes[i]}\t\t   ", end="")
            if self.allocation[i] != -1:
                print(self.allocation[i] + 1)
            else:
                print("Not Allocated")

        print(f"\nTotal Internal Fragmentation: {self.internal_fragmentation}")
        print(f"Total External Fragmentation: {self.external_fragmentation}")
        print("**************************************************************\n")


def main():
    num_processes = int(input("---> Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        process_size = int(input(f"---> Enter the size of process {i + 1}: "))
        processes.append(process_size)

    print("**************************************************************")
    num_blocks = int(input("---> Enter the number of memory blocks: "))
    blocks = []
    for i in range(num_blocks):
        block_size = int(input(f"---> Enter the size of memory block {i + 1}: "))
        blocks.append(block_size)

    allocator = MemoryAllocator(processes, blocks)
    allocator.worst_fit()
    allocator.display_allocation()


if __name__ == "__main__":
    main()