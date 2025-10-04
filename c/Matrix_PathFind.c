/*
GitHub Username: Shivi2705
Aim: Matrix Pathfinder - Find a valid path from top-left to bottom-right avoiding blocked cells
Date: October 4, 2025

Algorithm: Backtracking with DFS
Time Complexity: O(4^(n*m)) worst case
Space Complexity: O(n*m) for recursion stack and visited array
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 20

int rows, cols;
int matrix[MAX][MAX];
int visited[MAX][MAX];
int pathX[MAX*MAX];
int pathY[MAX*MAX];
int pathLen = 0;

// Directions: Right, Down, Left, Up
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int isValid(int x, int y) {
    return (x >= 0 && x < rows && y >= 0 && y < cols &&
            matrix[x][y] == 0 && !visited[x][y]);
}

int findPath(int x, int y) {
    if (x == rows - 1 && y == cols - 1) {
        pathX[pathLen] = x;
        pathY[pathLen++] = y;
        return 1;
    }

    visited[x][y] = 1;
    pathX[pathLen] = x;
    pathY[pathLen++] = y;

    for (int i = 0; i < 4; i++) {
        int newX = x + dx[i];
        int newY = y + dy[i];
        if (isValid(newX, newY)) {
            if (findPath(newX, newY)) return 1;
        }
    }

    // Backtrack
    pathLen--;
    visited[x][y] = 0;
    return 0;
}

void displayMatrix() {
    printf("\n📊 Original Matrix (0 = Open, 1 = Blocked):\n   ");
    for (int j = 0; j < cols; j++) printf("%3d", j);
    printf("\n");
    for (int i = 0; i < rows; i++) {
        printf("%2d ", i);
        for (int j = 0; j < cols; j++) {
            printf(matrix[i][j]==1 ? " ⬛" : " ⬜");
        }
        printf("\n");
    }
}

void displayPath() {
    if (pathLen == 0) {
        printf("\n❌ No path found!\n");
        return;
    }

    printf("\n✅ Path Found!\n📍 Path Coordinates:\n");
    for (int i = 0; i < pathLen; i++) {
        printf("(%d,%d)", pathX[i], pathY[i]);
        if (i < pathLen - 1) printf(" → ");
        if ((i+1) % 5 == 0 && i < pathLen - 1) printf("\n");
    }
    printf("\n\nTotal steps: %d\n", pathLen);
}

void displayVisualPath() {
    if (pathLen == 0) return;
    int visual[MAX][MAX];
    for (int i=0;i<rows;i++)
        for (int j=0;j<cols;j++)
            visual[i][j] = matrix[i][j];
    for (int i=0;i<pathLen;i++)
        visual[pathX[i]][pathY[i]] = 2;

    printf("\n🗺️  Visual Path (⬛=Blocked, ⬜=Open, 🟩=Path):\n   ");
    for (int j=0;j<cols;j++) printf("%3d", j);
    printf("\n");

    for (int i=0;i<rows;i++){
        printf("%2d ", i);
        for (int j=0;j<cols;j++){
            if (visual[i][j]==1) printf(" ⬛");
            else if (visual[i][j]==2) printf(" 🟩");
            else printf(" ⬜");
        }
        printf("\n");
    }
}

void predefinedMatrix5x5() {
    rows = cols = 5;
    int temp[5][5] = {
        {0,0,0,1,0},
        {0,1,0,1,0},
        {0,1,0,0,0},
        {0,0,1,1,0},
        {1,0,0,0,0}
    };
    for(int i=0;i<rows;i++)
        for(int j=0;j<cols;j++)
            matrix[i][j] = temp[i][j];
}

void predefinedMatrix8x8() {
    rows = cols = 8;
    int temp[8][8] = {
        {0,0,1,0,0,0,1,0},
        {0,0,1,0,1,0,0,0},
        {0,0,0,0,1,0,1,0},
        {1,1,0,1,0,0,0,0},
        {0,0,0,1,0,1,1,0},
        {0,1,0,0,0,0,0,0},
        {0,1,1,1,0,1,0,0},
        {0,0,0,0,0,1,0,0}
    };
    for(int i=0;i<rows;i++)
        for(int j=0;j<cols;j++)
            matrix[i][j] = temp[i][j];
}

void customMatrix() {
    printf("\nEnter number of rows (max %d): ", MAX);
    scanf("%d",&rows);
    printf("Enter number of columns (max %d): ", MAX);
    scanf("%d",&cols);
    if(rows<=0 || rows>MAX || cols<=0 || cols>MAX){
        printf("Invalid dimensions! Using default 5x5.\n");
        rows = cols = 5;
    }

    printf("Enter matrix row by row (0=open,1=blocked):\n");
    for(int i=0;i<rows;i++){
        printf("Row %d: ",i);
        for(int j=0;j<cols;j++){
            scanf("%d",&matrix[i][j]);
            if(matrix[i][j]!=0 && matrix[i][j]!=1) matrix[i][j]=0;
        }
    }
}

int main() {
    int choice;

    do {
        printf("\n╔════════════════════════════════════╗\n");
        printf("║         MATRIX PATHFINDER         ║\n");
        printf("╚════════════════════════════════════╝\n");
        printf("1. Use Predefined Matrix (5x5)\n");
        printf("2. Use Predefined Matrix (8x8)\n");
        printf("3. Create Custom Matrix\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d",&choice);

        if(choice==1) predefinedMatrix5x5();
        else if(choice==2) predefinedMatrix8x8();
        else if(choice==3) customMatrix();
        else if(choice==4) break;
        else { printf("❌ Invalid choice! Try again.\n"); continue; }

        // Reset visited and path
        for(int i=0;i<MAX;i++)
            for(int j=0;j<MAX;j++)
                visited[i][j] = 0;
        pathLen = 0;

        displayMatrix();
        printf("\n🔍 Searching for path...\n");
        if(findPath(0,0)){
            displayPath();
            displayVisualPath();
        } else {
            printf("\n❌ No valid path exists from (0,0) to (%d,%d)\n", rows-1, cols-1);
        }

        printf("\nPress Enter to continue...");
        getchar(); getchar(); // pause
    } while(choice!=4);

    printf("\n👋 Thank you for using Matrix Pathfinder!\nHappy Coding! 💻\n");
    return 0;
}
