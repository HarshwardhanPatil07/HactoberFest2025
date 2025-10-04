"""
GitHub Username: Shivi2705
Aim: Matrix Pathfinder - Find a valid path from top-left to bottom-right avoiding blocked cells
Date: October 4, 2025
"""

# ------------------------- Matrix Pathfinder Class -------------------------

class MatrixPathfinder:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
        self.visited = [[False]*self.cols for _ in range(self.rows)]
        self.path = []
        # Directions: Right, Down, Left, Up
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        return (
            0 <= x < self.rows and
            0 <= y < self.cols and
            self.matrix[x][y] == 0 and
            not self.visited[x][y]
        )

    def find_path_helper(self, x, y):
        if x == self.rows - 1 and y == self.cols - 1:
            self.path.append((x, y))
            return True

        self.visited[x][y] = True
        self.path.append((x, y))

        for dx, dy in self.directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y):
                if self.find_path_helper(new_x, new_y):
                    return True

        # Backtrack
        self.path.pop()
        self.visited[x][y] = False
        return False

    def find_path(self):
        self.path.clear()
        self.visited = [[False]*self.cols for _ in range(self.rows)]
        if not self.rows or not self.cols:
            print("\n❌ Matrix is empty!")
            return False
        if self.matrix[0][0] == 1 or self.matrix[self.rows-1][self.cols-1] == 1:
            print("\n❌ Path not possible! Start or end is blocked.")
            return False
        return self.find_path_helper(0, 0)

    def display_matrix(self):
        print("\n📊 Original Matrix (0 = Open, 1 = Blocked):")
        print("   ", end="")
        for j in range(self.cols):
            print(f"{j:3}", end="")
        print()
        for i in range(self.rows):
            print(f"{i:2} ", end="")
            for j in range(self.cols):
                print(" ⬜" if self.matrix[i][j]==0 else " ⬛", end="")
            print()

    def display_path(self):
        if not self.path:
            print("\n❌ No path found!")
            return
        print("\n✅ Path Found!\n📍 Path Coordinates:")
        for i, (x, y) in enumerate(self.path):
            print(f"({x},{y})", end=" → " if i < len(self.path)-1 else "")
            if (i+1) % 5 == 0 and i < len(self.path)-1:
                print()
        print(f"\n\nTotal steps: {len(self.path)}")

    def display_visual_path(self):
        if not self.path:
            return
        visual = [row[:] for row in self.matrix]
        for x, y in self.path:
            visual[x][y] = 2
        print("\n🗺️  Visual Path (⬛ = Blocked, ⬜ = Open, 🟩 = Path):")
        print("   ", end="")
        for j in range(self.cols):
            print(f"{j:3}", end="")
        print()
        for i in range(self.rows):
            print(f"{i:2} ", end="")
            for j in range(self.cols):
                if visual[i][j] == 1:
                    print(" ⬛", end="")
                elif visual[i][j] == 2:
                    print(" 🟩", end="")
                else:
                    print(" ⬜", end="")
            print()

# ------------------------- Predefined & Custom Matrices -------------------------

def get_predefined_matrix_5x5():
    return [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0]
    ]

def get_predefined_matrix_8x8():
    return [
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0]
    ]

def get_custom_matrix():
    rows = int(input("\nEnter number of rows: "))
    cols = int(input("Enter number of columns: "))
    if rows<=0 or cols<=0 or rows>20 or cols>20:
        print("Invalid dimensions! Using default 5x5.")
        rows = cols = 5
    matrix = []
    print("\nEnter matrix row by row (0=open, 1=blocked):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i}: ").split()))
        row = [0 if x not in (0,1) else x for x in row]
        if len(row)<cols:
            row += [0]*(cols-len(row))
        matrix.append(row)
    return matrix

# ------------------------- Menu -------------------------

def display_menu():
    print("\n╔════════════════════════════════════╗")
    print("║        MATRIX PATHFINDER          ║")
    print("╚════════════════════════════════════╝")
    print("1. Use Predefined Matrix (5x5)")
    print("2. Use Predefined Matrix (8x8)")
    print("3. Create Custom Matrix")
    print("4. Exit")
    return input("\nEnter your choice: ")

# ------------------------- Main -------------------------

def main():
    while True:
        choice = display_menu()
        if choice=='1':
            matrix = get_predefined_matrix_5x5()
            print("\n✨ Using 5x5 Predefined Matrix")
        elif choice=='2':
            matrix = get_predefined_matrix_8x8()
            print("\n✨ Using 8x8 Predefined Matrix")
        elif choice=='3':
            matrix = get_custom_matrix()
        elif choice=='4':
            print("\n👋 Thank you for using Matrix Pathfinder!\nHappy Coding! 💻\n")
            break
        else:
            print("\n❌ Invalid choice. Try again.")
            continue

        pathfinder = MatrixPathfinder(matrix)
        pathfinder.display_matrix()

        print("\n🔍 Searching for path...\n")
        if pathfinder.find_path():
            pathfinder.display_path()
            pathfinder.display_visual_path()
        else:
            print(f"\n❌ No valid path exists from (0,0) to ({len(matrix)-1},{len(matrix[0])-1})")

        input("\nPress Enter to continue...")

if __name__=="__main__":
    main()
