/*
GitHub Username: Shivi2705
Aim: Generate secure random passwords with user-defined options
Date: October 4, 2025
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void shuffle(char *array, int n) {
    if (n > 1) {
        for (int i = n - 1; i > 0; i--) {
            int j = rand() % (i + 1);
            char temp = array[j];
            array[j] = array[i];
            array[i] = temp;
        }
    }
}

void generatePassword(int length, int useUpper, int useLower, int useDigits, int useSpecial) {
    if (length <= 0) {
        printf("❌ Password length must be greater than 0\n");
        return;
    }

    char upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char lower[] = "abcdefghijklmnopqrstuvwxyz";
    char digits[] = "0123456789";
    char special[] = "!@#$%^&*()-_=+[]{}|;:,.<>?/";

    char allChars[256] = "";
    char password[256] = "";
    int index = 0;

    if (useUpper) {
        strcat(allChars, upper);
        password[index++] = upper[rand() % strlen(upper)];
    }
    if (useLower) {
        strcat(allChars, lower);
        password[index++] = lower[rand() % strlen(lower)];
    }
    if (useDigits) {
        strcat(allChars, digits);
        password[index++] = digits[rand() % strlen(digits)];
    }
    if (useSpecial) {
        strcat(allChars, special);
        password[index++] = special[rand() % strlen(special)];
    }

    if (strlen(allChars) == 0) {
        printf("❌ At least one character type must be selected\n");
        return;
    }

    while (index < length) {
        password[index++] = allChars[rand() % strlen(allChars)];
    }

    shuffle(password, length);
    password[length] = '\0';

    printf("\n🔐 Generated Password: %s\n", password);
}

int main() {
    srand((unsigned int)time(NULL));

    int length;
    char choice;
    int useUpper, useLower, useDigits, useSpecial;

    printf("=== Secure Random Password Generator ===\n");
    printf("Enter password length: ");
    scanf("%d", &length);

    printf("Include uppercase letters? (y/n): ");
    scanf(" %c", &choice);
    useUpper = (choice == 'y' || choice == 'Y');

    printf("Include lowercase letters? (y/n): ");
    scanf(" %c", &choice);
    useLower = (choice == 'y' || choice == 'Y');

    printf("Include numbers? (y/n): ");
    scanf(" %c", &choice);
    useDigits = (choice == 'y' || choice == 'Y');

    printf("Include special characters? (y/n): ");
    scanf(" %c", &choice);
    useSpecial = (choice == 'y' || choice == 'Y');

    generatePassword(length, useUpper, useLower, useDigits, useSpecial);

    return 0;
}
