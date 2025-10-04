/*
GitHub Username: Shivi2705
Aim: Generate secure random passwords with user-defined options
Date: October 4, 2025
*/

import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.Collections;

public class SecurePasswordGenerator {

    public static String generatePassword(int length, boolean useUpper, boolean useLower, boolean useDigits, boolean useSpecial) {
        if (length <= 0) {
            throw new IllegalArgumentException("Password length must be greater than 0");
        }

        String upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lower = "abcdefghijklmnopqrstuvwxyz";
        String digits = "0123456789";
        String special = "!@#$%^&*()-_=+[]{}|;:,.<>?/";

        String allChars = "";
        ArrayList<Character> password = new ArrayList<>();

        if (useUpper) {
            allChars += upper;
            password.add(upper.charAt(new Random().nextInt(upper.length())));
        }
        if (useLower) {
            allChars += lower;
            password.add(lower.charAt(new Random().nextInt(lower.length())));
        }
        if (useDigits) {
            allChars += digits;
            password.add(digits.charAt(new Random().nextInt(digits.length())));
        }
        if (useSpecial) {
            allChars += special;
            password.add(special.charAt(new Random().nextInt(special.length())));
        }

        if (allChars.isEmpty()) {
            throw new IllegalArgumentException("At least one character type must be selected");
        }

        Random rand = new Random();
        while (password.size() < length) {
            password.add(allChars.charAt(rand.nextInt(allChars.length())));
        }

        // Shuffle the password to avoid predictable patterns
        Collections.shuffle(password);

        // Convert ArrayList<Character> to String
        StringBuilder result = new StringBuilder();
        for (char c : password) {
            result.append(c);
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Secure Random Password Generator ===");
        System.out.print("Enter password length: ");
        int length = sc.nextInt();
        sc.nextLine(); // consume newline

        System.out.print("Include uppercase letters? (y/n): ");
        boolean useUpper = sc.nextLine().trim().equalsIgnoreCase("y");

        System.out.print("Include lowercase letters? (y/n): ");
        boolean useLower = sc.nextLine().trim().equalsIgnoreCase("y");

        System.out.print("Include numbers? (y/n): ");
        boolean useDigits = sc.nextLine().trim().equalsIgnoreCase("y");

        System.out.print("Include special characters? (y/n): ");
        boolean useSpecial = sc.nextLine().trim().equalsIgnoreCase("y");

        try {
            String password = generatePassword(length, useUpper, useLower, useDigits, useSpecial);
            System.out.println("\n🔐 Generated Password: " + password);
        } catch (IllegalArgumentException e) {
            System.out.println("\n❌ Error: " + e.getMessage());
        }

        sc.close();
    }
}
