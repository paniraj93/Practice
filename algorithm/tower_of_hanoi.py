def hanoi(n, source, auxiliary, destination, source_rod, auxiliary_rod, destination_rod):
    if n == 1:
        disk = source_rod.pop()
        destination_rod.append(disk)
        print(f"Move disk {disk} from {source} to {destination}")
        return
    hanoi(n-1, source, destination, auxiliary, source_rod, destination_rod, auxiliary_rod)
    disk = source_rod.pop()
    destination_rod.append(disk)
    print(f"Move disk {disk} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination, auxiliary_rod, source_rod, destination_rod)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    
    source_rod = list(range(n, 0, -1))
    auxiliary_rod = []
    destination_rod = []
    
    hanoi(n, 'A', 'B', 'C', source_rod, auxiliary_rod, destination_rod)
    
    print("Final state of destination rod:", destination_rod)
