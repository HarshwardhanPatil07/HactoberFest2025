// GitHub Username: Pasan11504
// Aim: Check if parentheses/brackets are balanced using Stack
// Date: 2025-10-04

package DataStructures.Stack;

import java.util.Scanner;
import java.util.Stack;

/**
 * Balanced Parentheses Checker
 * 
 * This program checks if an expression has balanced parentheses, brackets, and braces
 * using Stack data structure.
 * 
 * Examples:
 * - "{[()()]}" -> Balanced
 * - "{[(])}" -> Balanced
 * - "{[()}" -> Not Balanced
 * - "(()" -> Not Balanced
 * 
 * Algorithm:
 * 1. Traverse the expression character by character
 * 2. If opening bracket found -> push to stack
 * 3. If closing bracket found -> check if it matches top of stack
 * 4. If stack is empty at end -> balanced, else not balanced
 * 
 * Time Complexity: O(n) where n is length of expression
 * Space Complexity: O(n) for stack in worst case
 */
public class BalancedParentheses {
    
    /**
     * Check if the given character is an opening bracket
     * @param ch Character to check
     * @return true if opening bracket, false otherwise
     */
    private static boolean isOpeningBracket(char ch) {
        return (ch == '(' || ch == '{' || ch == '[');
    }
    
    /**
     * Check if the given character is a closing bracket
     * @param ch Character to check
     * @return true if closing bracket, false otherwise
     */
    private static boolean isClosingBracket(char ch) {
        return (ch == ')' || ch == '}' || ch == ']');
    }
    
    /**
     * Check if opening and closing brackets match
     * @param opening Opening bracket
     * @param closing Closing bracket
     * @return true if they match, false otherwise
     */
    private static boolean isMatchingPair(char opening, char closing) {
        return (opening == '(' && closing == ')') ||
               (opening == '{' && closing == '}') ||
               (opening == '[' && closing == ']');
    }
    
    /**
     * Main method to check if brackets are balanced
     * @param expression String expression to check
     * @return true if balanced, false otherwise
     */
    public static boolean areParenthesesBalanced(String expression) {
        // Create a stack to store opening brackets
        Stack<Character> stack = new Stack<>();
        
        // Traverse each character in the expression
        for (int i = 0; i < expression.length(); i++) {
            char current = expression.charAt(i);
            
            // If opening bracket, push to stack
            if (isOpeningBracket(current)) {
                stack.push(current);
            }
            // If closing bracket, check for matching opening bracket
            else if (isClosingBracket(current)) {
                // If stack is empty, no matching opening bracket
                if (stack.isEmpty()) {
                    return false;
                }
                
                // Pop from stack and check if it matches
                char top = stack.pop();
                if (!isMatchingPair(top, current)) {
                    return false;
                }
            }
            // Ignore other characters (numbers, operators, etc.)
        }
        
        // If stack is empty, all brackets are balanced
        return stack.isEmpty();
    }
    
    /**
     * Method to provide detailed feedback about bracket balance
     * @param expression String expression to check
     */
    public static void checkAndDisplay(String expression) {
        System.out.println("\nExpression: " + expression);
        
        if (areParenthesesBalanced(expression)) {
            System.out.println("Result: ✓ Balanced - All brackets are properly matched!");
        } else {
            System.out.println("Result: ✗ Not Balanced - Brackets are not properly matched!");
        }
    }
    
    /**
     * Main method to demonstrate balanced parentheses checker
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Balanced Parentheses Checker ===");
        System.out.println("This program checks if brackets (), {}, [] are balanced\n");
        
        // Test cases
        System.out.println("--- Test Cases ---");
        String[] testCases = {
            "{[()()]}",
            "{[(])}",
            "((()))",
            "(()",
            "{[}]",
            "()[]{}",
            "",
            "(a+b)*{c-d}",
            "({[()]})",
            "((((("
        };
        
        for (String test : testCases) {
            checkAndDisplay(test);
        }
        
        // User input
        System.out.println("\n--- Check Your Own Expression ---");
        boolean continueChecking = true;
        
        while (continueChecking) {
            System.out.print("\nEnter an expression (or 'exit' to quit): ");
            String userInput = scanner.nextLine();
            
            if (userInput.equalsIgnoreCase("exit")) {
                continueChecking = false;
                System.out.println("Thank you for using Balanced Parentheses Checker!");
            } else {
                checkAndDisplay(userInput);
            }
        }
        
        scanner.close();
    }
}
