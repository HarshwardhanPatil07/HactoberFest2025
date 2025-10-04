// GitHub Username: Pasan11504
// Aim: Implement Stack Data Structure with all basic operations
// Date: 2025-10-04

package DataStructures.Stack;

import java.util.Scanner;

/**
 * Stack Implementation using Array
 * A Stack is a linear data structure that follows LIFO (Last In First Out) principle
 * 
 * Time Complexity:
 * - Push: O(1)
 * - Pop: O(1)
 * - Peek: O(1)
 * - Search: O(n)
 * 
 * Space Complexity: O(n) where n is the size of the stack
 */
public class StackImplementation {
    private int maxSize;        // Maximum size of stack
    private int top;            // Index of top element
    private int[] stackArray;   // Array to store stack elements
    
    /**
     * Constructor to initialize stack with given size
     * @param size Maximum size of the stack
     */
    public StackImplementation(int size) {
        this.maxSize = size;
        this.stackArray = new int[maxSize];
        this.top = -1;  // Stack is empty initially
    }
    
    /**
     * Push operation - Add element to top of stack
     * @param value Element to be pushed
     * @return true if push is successful, false if stack is full
     */
    public boolean push(int value) {
        if (isFull()) {
            System.out.println("Stack Overflow! Cannot push " + value);
            return false;
        }
        stackArray[++top] = value;
        System.out.println("Pushed: " + value);
        return true;
    }
    
    /**
     * Pop operation - Remove and return top element
     * @return Top element if stack is not empty, -1 otherwise
     */
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Underflow! Cannot pop from empty stack");
            return -1;
        }
        int poppedValue = stackArray[top--];
        System.out.println("Popped: " + poppedValue);
        return poppedValue;
    }
    
    /**
     * Peek operation - Return top element without removing it
     * @return Top element if stack is not empty, -1 otherwise
     */
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty! No top element");
            return -1;
        }
        return stackArray[top];
    }
    
    /**
     * Check if stack is empty
     * @return true if stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return (top == -1);
    }
    
    /**
     * Check if stack is full
     * @return true if stack is full, false otherwise
     */
    public boolean isFull() {
        return (top == maxSize - 1);
    }
    
    /**
     * Get current size of stack
     * @return Number of elements in stack
     */
    public int size() {
        return top + 1;
    }
    
    /**
     * Display all elements in stack
     */
    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return;
        }
        System.out.print("Stack elements (top to bottom): ");
        for (int i = top; i >= 0; i--) {
            System.out.print(stackArray[i] + " ");
        }
        System.out.println();
    }
    
    /**
     * Search for an element in stack
     * @param value Element to search
     * @return Position from top (1-based) if found, -1 otherwise
     */
    public int search(int value) {
        for (int i = top; i >= 0; i--) {
            if (stackArray[i] == value) {
                return (top - i + 1);  // Return position from top
            }
        }
        return -1;  // Element not found
    }
    
    /**
     * Clear all elements from stack
     */
    public void clear() {
        top = -1;
        System.out.println("Stack cleared!");
    }
    
    /**
     * Main method to demonstrate stack operations
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Stack Implementation Demo ===");
        System.out.print("Enter stack size: ");
        int size = scanner.nextInt();
        
        StackImplementation stack = new StackImplementation(size);
        
        boolean running = true;
        
        while (running) {
            System.out.println("\n--- Stack Operations Menu ---");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Check if Empty");
            System.out.println("6. Check if Full");
            System.out.println("7. Get Size");
            System.out.println("8. Search Element");
            System.out.println("9. Clear Stack");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter value to push: ");
                    int pushValue = scanner.nextInt();
                    stack.push(pushValue);
                    break;
                    
                case 2:
                    stack.pop();
                    break;
                    
                case 3:
                    int topElement = stack.peek();
                    if (topElement != -1) {
                        System.out.println("Top element: " + topElement);
                    }
                    break;
                    
                case 4:
                    stack.display();
                    break;
                    
                case 5:
                    System.out.println("Stack is " + (stack.isEmpty() ? "empty" : "not empty"));
                    break;
                    
                case 6:
                    System.out.println("Stack is " + (stack.isFull() ? "full" : "not full"));
                    break;
                    
                case 7:
                    System.out.println("Current stack size: " + stack.size());
                    break;
                    
                case 8:
                    System.out.print("Enter value to search: ");
                    int searchValue = scanner.nextInt();
                    int position = stack.search(searchValue);
                    if (position != -1) {
                        System.out.println("Element found at position " + position + " from top");
                    } else {
                        System.out.println("Element not found in stack");
                    }
                    break;
                    
                case 9:
                    stack.clear();
                    break;
                    
                case 0:
                    System.out.println("Exiting... Thank you!");
                    running = false;
                    break;
                    
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
        
        scanner.close();
    }
}
