# Stack Data Structure Implementation

This folder contains Stack implementations and practical applications in Java.

## 📚 Contents

### 1. StackImplementation.java
A complete implementation of Stack data structure using arrays.

**Features:**
- ✅ Push operation (add element to top)
- ✅ Pop operation (remove and return top element)
- ✅ Peek operation (view top element without removing)
- ✅ isEmpty() - check if stack is empty
- ✅ isFull() - check if stack is full
- ✅ size() - get current number of elements
- ✅ display() - show all elements
- ✅ search() - find element position from top
- ✅ clear() - remove all elements
- ✅ Interactive menu-driven program

**Time Complexity:**
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

**Space Complexity:** O(n)

### 2. BalancedParentheses.java
Practical application of Stack to check if brackets are balanced in an expression.

**Features:**
- ✅ Checks (), {}, [] brackets
- ✅ Works with complex nested expressions
- ✅ Includes multiple test cases
- ✅ Interactive user input mode
- ✅ Detailed feedback for each expression

**Examples:**
- `{[()()]}` → Balanced ✓
- `{[(])}` → Not Balanced ✗
- `((())` → Not Balanced ✗
- `()[]{}` → Balanced ✓

**Algorithm:**
1. Push opening brackets onto stack
2. When closing bracket found, check if it matches stack top
3. If stack is empty at end → balanced

**Time Complexity:** O(n) where n is expression length  
**Space Complexity:** O(n) for stack

## 🚀 How to Run

### StackImplementation.java
```bash
# Compile
javac java/DataStructures/Stack/StackImplementation.java

# Run
java -cp . DataStructures.Stack.StackImplementation
```

### BalancedParentheses.java
```bash
# Compile
javac java/DataStructures/Stack/BalancedParentheses.java

# Run
java -cp . DataStructures.Stack.BalancedParentheses
```

## 📖 What is a Stack?

A **Stack** is a linear data structure that follows the **LIFO (Last In First Out)** principle. The last element inserted is the first one to be removed.

**Real-world examples:**
- 🥞 Stack of plates
- 📚 Stack of books
- ↩️ Browser back button
- ⌨️ Undo/Redo functionality

**Common Stack Applications:**
1. Function call management (call stack)
2. Expression evaluation (postfix, prefix)
3. Backtracking algorithms
4. Browser history
5. Undo/Redo operations
6. Syntax parsing

## 🎓 Learning Resources

- [Stack Visualization](https://visualgo.net/en/list)
- [GeeksforGeeks - Stack Data Structure](https://www.geeksforgeeks.org/stack-data-structure/)
- [Stack in Java - Oracle Docs](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html)

## 👤 Contributor
- **GitHub**: Pasan11504
- **Date**: October 4, 2025
- **Event**: Hacktoberfest 2025

---
*Part of HactoberFest2025 repository*
