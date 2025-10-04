/*
 * Matrix Pathfinder - Find path from top-left to bottom-right
 * GitHub Username:Shivi2705
 * Aim: Find a valid path through a matrix avoiding blocked cells
 * Date: October 4, 2025
 * 
 * Algorithm: Backtracking with DFS
 * Time Complexity: O(4^(n*m)) worst case
 * Space Complexity: O(n*m) for recursion stack and visited array
 */

#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

class MatrixPathfinder {
private:
    vector<vector<int>> matrix;
    vector<vector<bool>> visited;
    vector<pair<int, int>> path;
    int rows, cols;
    
    // Directions: Right, Down, Left, Up
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    string directions[4] = {"Right", "Down", "Left", "Up"};
    
    bool isValid(int x, int y) {
        return (x >= 0 && x < rows && y >= 0 && y < cols && 
                matrix[x][y] == 0 && !visited[x][y]);
    }
    
    bool findPathHelper(int x, int y) {
        // Base case: reached destination
        if (x == rows - 1 && y == cols - 1) {
            path.push_back({x, y});
            return true;
        }
        
        // Mark current cell as visited
        visited[x][y] = true;
        path.push_back({x, y});
        
        // Try all 4 directions
        for (int i = 0; i < 4; i++) {
            int newX = x + dx[i];
            int newY = y + dy[i];
            
            if (isValid(newX, newY)) {
                if (findPathHelper(newX, newY)) {
                    return true;
                }
            }
        }
        
        // Backtrack
        path.pop_back();
        visited[x][y] = false;
        return false;
    }
    
public:
    MatrixPathfinder(vector<vector<int>>& mat) {
        matrix = mat;
        rows = mat.size();
        cols = mat[0].size();
        visited.assign(rows, vector<bool>(cols, false));
    }
    
    bool findPath() {
        path.clear();
        visited.assign(rows, vector<bool>(cols, false));
        
        // Check if start or end is blocked
        if (matrix[0][0] == 1 || matrix[rows-1][cols-1] == 1) {
            cout << "\n❌ Path not possible! Start or end is blocked.\n";
            return false;
        }
        
        return findPathHelper(0, 0);
    }
    
    void displayMatrix() {
        cout << "\n📊 Original Matrix (0 = Open, 1 = Blocked):\n";
        cout << "   ";
        for (int j = 0; j < cols; j++) {
            cout << setw(3) << j;
        }
        cout << "\n";
        
        for (int i = 0; i < rows; i++) {
            cout << setw(2) << i << " ";
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 1) {
                    cout << " ⬛";
                } else {
                    cout << " ⬜";
                }
            }
            cout << "\n";
        }
    }
    
    void displayPath() {
        if (path.empty()) {
            cout << "\n❌ No path found!\n";
            return;
        }
        
        cout << "\n✅ Path Found!\n";
        cout << "\n📍 Path Coordinates:\n";
        for (size_t i = 0; i < path.size(); i++) {
            cout << "(" << path[i].first << "," << path[i].second << ")";
            if (i < path.size() - 1) {
                cout << " → ";
            }
            if ((i + 1) % 5 == 0 && i < path.size() - 1) {
                cout << "\n";
            }
        }
        cout << "\n\nTotal steps: " << path.size() << "\n";
    }
    
    void displayVisualPath() {
        if (path.empty()) {
            return;
        }
        
        // Create a copy of matrix for visualization
        vector<vector<int>> visualMatrix = matrix;
        
        // Mark path with 2
        for (auto& p : path) {
            visualMatrix[p.first][p.second] = 2;
        }
        
        cout << "\n🗺️  Visual Path (⬛ = Blocked, ⬜ = Open, 🟩 = Path):\n";
        cout << "   ";
        for (int j = 0; j < cols; j++) {
            cout << setw(3) << j;
        }
        cout << "\n";
        
        for (int i = 0; i < rows; i++) {
            cout << setw(2) << i << " ";
            for (int j = 0; j < cols; j++) {
                if (visualMatrix[i][j] == 1) {
                    cout << " ⬛";
                } else if (visualMatrix[i][j] == 2) {
                    cout << " 🟩";
                } else {
                    cout << " ⬜";
                }
            }
            cout << "\n";
        }
    }
};

void displayMenu() {
    cout << "\n╔════════════════════════════════════════╗\n";
    cout << "║     MATRIX PATHFINDER PROGRAM         ║\n";
    cout << "╚════════════════════════════════════════╝\n";
    cout << "\n1. Use Predefined Matrix (5x5)\n";
    cout << "2. Use Predefined Matrix (8x8)\n";
    cout << "3. Create Custom Matrix\n";
    cout << "4. Exit\n";
    cout << "\nEnter your choice: ";
}

vector<vector<int>> getPredefinedMatrix1() {
    return {
        {0, 0, 0, 1, 0},
        {0, 1, 0, 1, 0},
        {0, 1, 0, 0, 0},
        {0, 0, 1, 1, 0},
        {1, 0, 0, 0, 0}
    };
}

vector<vector<int>> getPredefinedMatrix2() {
    return {
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

vector<vector<int>> getCustomMatrix() {
    int rows, cols;
    cout << "\nEnter number of rows: ";
    cin >> rows;
    cout << "Enter number of columns: ";
    cin >> cols;
    
    if (rows <= 0 || cols <= 0 || rows > 20 || cols > 20) {
        cout << "Invalid dimensions! Using default 5x5.\n";
        rows = cols = 5;
    }
    
    vector<vector<int>> matrix(rows, vector<int>(cols));
    
    cout << "\nEnter matrix (0 for open path, 1 for blocked):\n";
    for (int i = 0; i < rows; i++) {
        cout << "Row " << i << ": ";
        for (int j = 0; j < cols; j++) {
            cin >> matrix[i][j];
            if (matrix[i][j] != 0 && matrix[i][j] != 1) {
                matrix[i][j] = 0; // Default to open
            }
        }
    }
    
    return matrix;
}

int main() {
    // GitHub Username: [Your GitHub Username]
    // Aim: Demonstrate pathfinding in a matrix using backtracking
    // Date: October 4, 2025
    
    int choice;
    
    do {
        displayMenu();
        cin >> choice;
        
        if (choice >= 1 && choice <= 3) {
            vector<vector<int>> matrix;
            
            switch(choice) {
                case 1:
                    matrix = getPredefinedMatrix1();
                    cout << "\n✨ Using 5x5 Predefined Matrix\n";
                    break;
                case 2:
                    matrix = getPredefinedMatrix2();
                    cout << "\n✨ Using 8x8 Predefined Matrix\n";
                    break;
                case 3:
                    matrix = getCustomMatrix();
                    break;
            }
            
            MatrixPathfinder pathfinder(matrix);
            pathfinder.displayMatrix();
            
            cout << "\n🔍 Searching for path...\n";
            
            if (pathfinder.findPath()) {
                pathfinder.displayPath();
                pathfinder.displayVisualPath();
            } else {
                cout << "\n❌ No valid path exists from (0,0) to ("
                     << matrix.size()-1 << "," << matrix[0].size()-1 << ")\n";
            }
            
            cout << "\n\nPress Enter to continue...";
            cin.ignore();
            cin.get();
        }
        
    } while (choice != 4);
    
    cout << "\n👋 Thank you for using Matrix Pathfinder!\n";
    cout << "Happy Coding! 💻\n\n";
    
    return 0;
}