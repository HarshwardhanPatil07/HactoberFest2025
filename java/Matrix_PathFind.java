import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Arrays;

/**
 * Matrix Pathfinder - Finds a valid path from the top-left (0,0) to 
 * the bottom-right (rows-1, cols-1) of a matrix, avoiding blocked cells (1).
 * Uses Depth First Search (DFS) with Backtracking.
 * * GitHub Username: Shivi2705
 * Date: October 4, 2025
 */
 class MatrixPathfinder {

    private int[][] matrix;
    private boolean[][] visited;
    // Path stores coordinates as int arrays {row, col}
    private List<int[]> path;
    private int rows, cols;

    // Directions: Down, Right, Up, Left (The order doesn't strictly matter for finding A path)
    // C++ used: Right, Down, Left, Up. I'll maintain that order for consistency in DFS exploration preference.
    private final int[] dx = {0, 1, 0, -1}; // Change in row (for R, D, L, U)
    private final int[] dy = {1, 0, -1, 0}; // Change in col (for R, D, L, U)

    /**
     * Constructor initializes the pathfinder with the matrix.
     * @param mat The input matrix (0 for open, 1 for blocked).
     */
    public MatrixPathfinder(int[][] mat) {
        this.matrix = mat;
        this.rows = mat.length;
        this.cols = mat[0].length;
        this.visited = new boolean[rows][cols];
        this.path = new ArrayList<>();
    }

    /**
     * Checks if a move to (x, y) is valid.
     * @param x The row index.
     * @param y The column index.
     * @return True if the cell is within bounds, open (0), and not yet visited.
     */
    private boolean isValid(int x, int y) {
        return (x >= 0 && x < rows && y >= 0 && y < cols && 
                matrix[x][y] == 0 && !visited[x][y]);
    }

    /**
     * Recursive helper function for Depth First Search (DFS) with backtracking.
     * @param x Current row index.
     * @param y Current column index.
     * @return True if a path to the destination is found from (x, y), false otherwise.
     */
    private boolean findPathHelper(int x, int y) {
        // Base case: reached destination
        if (x == rows - 1 && y == cols - 1) {
            path.add(new int[]{x, y});
            return true;
        }

        // Mark current cell as visited and add to current path
        visited[x][y] = true;
        path.add(new int[]{x, y});

        // Try all 4 directions
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];

            if (isValid(newX, newY)) {
                if (findPathHelper(newX, newY)) {
                    return true; // Path found
                }
            }
        }

        // Backtrack: if no path found from this cell, remove it from the path and unmark it
        path.remove(path.size() - 1);
        visited[x][y] = false;
        return false;
    }

    /**
     * Public method to start the pathfinding process from (0, 0).
     * @return True if a path is found, false otherwise.
     */
    public boolean findPath() {
        path.clear();
        // Reset visited array
        for (int i = 0; i < rows; i++) {
            Arrays.fill(visited[i], false);
        }

        // Check if start or end is blocked
        if (matrix[0][0] == 1 || matrix[rows - 1][cols - 1] == 1) {
            System.out.println("\n❌ Path not possible! Start or end is blocked.");
            return false;
        }

        return findPathHelper(0, 0);
    }

    /**
     * Displays the original matrix with 0=Open (⬜) and 1=Blocked (⬛).
     */
    public void displayMatrix() {
        System.out.println("\n📊 Original Matrix (0 = Open, 1 = Blocked):");
        System.out.print("   ");
        for (int j = 0; j < cols; j++) {
            System.out.printf("%3d", j);
        }
        System.out.println();

        for (int i = 0; i < rows; i++) {
            System.out.printf("%2d ", i);
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 1) {
                    System.out.print(" ⬛");
                } else {
                    System.out.print(" ⬜");
                }
            }
            System.out.println();
        }
    }

    /**
     * Displays the found path as a sequence of coordinates.
     */
    public void displayPath() {
        if (path.isEmpty()) {
            System.out.println("\n❌ No path found!");
            return;
        }

        System.out.println("\n✅ Path Found!");
        System.out.println("\n📍 Path Coordinates:");
        
        for (int i = 0; i < path.size(); i++) {
            int[] p = path.get(i);
            System.out.print("(" + p[0] + "," + p[1] + ")");
            if (i < path.size() - 1) {
                System.out.print(" → ");
            }
            // Line break every 5 steps for readability
            if ((i + 1) % 5 == 0 && i < path.size() - 1) {
                System.out.println();
            }
        }
        System.out.println("\n\nTotal steps: " + path.size());
    }

    /**
     * Displays the matrix with the found path highlighted (🟩).
     */
    public void displayVisualPath() {
        if (path.isEmpty()) {
            return;
        }

        // Create a copy of matrix for visualization
        int[][] visualMatrix = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            System.arraycopy(matrix[i], 0, visualMatrix[i], 0, cols);
        }

        // Mark path with 2
        for (int[] p : path) {
            visualMatrix[p[0]][p[1]] = 2;
        }

        System.out.println("\n🗺️  Visual Path (⬛ = Blocked, ⬜ = Open, 🟩 = Path):");
        System.out.print("   ");
        for (int j = 0; j < cols; j++) {
            System.out.printf("%3d", j);
        }
        System.out.println();
        
        for (int i = 0; i < rows; i++) {
            System.out.printf("%2d ", i);
            for (int j = 0; j < cols; j++) {
                if (visualMatrix[i][j] == 1) {
                    System.out.print(" ⬛");
                } else if (visualMatrix[i][j] == 2) {
                    System.out.print(" 🟩");
                } else {
                    System.out.print(" ⬜");
                }
            }
            System.out.println();
        }
    }
    
    // --- Static Methods for Menu and Matrix Creation ---

    private static void displayMenu() {
        System.out.println("\n╔════════════════════════════════════════╗");
        System.out.println("║         MATRIX PATHFINDER PROGRAM        ║");
        System.out.println("╚════════════════════════════════════════╝");
        System.out.println("\n1. Use Predefined Matrix (5x5)");
        System.out.println("2. Use Predefined Matrix (8x8)");
        System.out.println("3. Create Custom Matrix");
        System.out.println("4. Exit");
        System.out.print("\nEnter your choice: ");
    }

    private static int[][] getPredefinedMatrix1() {
        return new int[][]{
            {0, 0, 0, 1, 0},
            {0, 1, 0, 1, 0},
            {0, 1, 0, 0, 0},
            {0, 0, 1, 1, 0},
            {1, 0, 0, 0, 0}
        };
    }

    private static int[][] getPredefinedMatrix2() {
        return new int[][]{
            {0, 0, 1, 0, 0, 0, 1, 0},
            {0, 0, 1, 0, 1, 0, 0, 0},
            {0, 0, 0, 0, 1, 0, 1, 0},
            {1, 1, 0, 1, 0, 0, 0, 0},
            {0, 0, 0, 1, 0, 1, 1, 0},
            {0, 1, 0, 0, 0, 0, 0, 0},
            {0, 1, 1, 1, 0, 1, 0, 0},
            {0, 0, 0, 0, 0, 1, 0, 0}
        };
    }

    private static int[][] getCustomMatrix(Scanner scanner) {
        int rows = 0;
        int cols = 0;

        try {
            System.out.print("\nEnter number of rows: ");
            rows = scanner.nextInt();
            System.out.print("Enter number of columns: ");
            cols = scanner.nextInt();
        } catch (java.util.InputMismatchException e) {
            System.out.println("Invalid input. Using default 5x5.");
            scanner.nextLine(); // Consume the invalid input
            rows = 5;
            cols = 5;
        }

        if (rows <= 0 || cols <= 0 || rows > 20 || cols > 20) {
            System.out.println("Invalid dimensions! Using default 5x5.");
            rows = 5;
            cols = 5;
        }
        
        int[][] matrix = new int[rows][cols];
        
        System.out.println("\nEnter matrix (0 for open path, 1 for blocked):");
        for (int i = 0; i < rows; i++) {
            System.out.print("Row " + i + ": ");
            for (int j = 0; j < cols; j++) {
                try {
                    int value = scanner.nextInt();
                    if (value == 0 || value == 1) {
                        matrix[i][j] = value;
                    } else {
                        System.out.print("(Invalid input, defaulting to 0) ");
                        matrix[i][j] = 0; // Default to open
                    }
                } catch (java.util.InputMismatchException e) {
                    System.out.print("(Invalid input, defaulting to 0) ");
                    matrix[i][j] = 0; // Default to open
                    scanner.nextLine(); // Consume the invalid input
                }
            }
        }
        
        return matrix;
    }

    // --- Main Entry Point ---

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        
        do {
            displayMenu();
            
            if (scanner.hasNextInt()) {
                choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline
            } else {
                choice = 0;
                scanner.nextLine(); // Consume invalid input
            }
            
            if (choice >= 1 && choice <= 3) {
                int[][] matrix;
                
                switch(choice) {
                    case 1:
                        matrix = getPredefinedMatrix1();
                        System.out.println("\n✨ Using 5x5 Predefined Matrix");
                        break;
                    case 2:
                        matrix = getPredefinedMatrix2();
                        System.out.println("\n✨ Using 8x8 Predefined Matrix");
                        break;
                    case 3:
                        matrix = getCustomMatrix(scanner);
                        break;
                    default:
                        // Should not happen, but prevents uninitialized matrix warning
                        matrix = new int[1][1]; 
                        break; 
                }
                
                MatrixPathfinder pathfinder = new MatrixPathfinder(matrix);
                pathfinder.displayMatrix();
                
                System.out.println("\n🔍 Searching for path...");
                
                if (pathfinder.findPath()) {
                    pathfinder.displayPath();
                    pathfinder.displayVisualPath();
                } else {
                    System.out.println("\n❌ No valid path exists from (0,0) to ("
                            + (matrix.length - 1) + "," + (matrix[0].length - 1) + ")");
                }
                
                System.out.println("\n\nPress Enter to continue...");
                // Wait for user to press enter
                scanner.nextLine();
            } else if (choice != 4) {
                System.out.println("Invalid choice. Please enter a number between 1 and 4.");
            }
            
        } while (choice != 4);
        
        System.out.println("\n👋 Thank you for using Matrix Pathfinder!");
        System.out.println("Happy Coding! 💻\n");
        
        scanner.close();
    }
}