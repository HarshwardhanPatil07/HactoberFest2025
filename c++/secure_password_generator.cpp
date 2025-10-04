/*
GitHub Username: Shivi2705
Aim: Generate secure random passwords with user-defined options
Date: October 4, 2025
*/

#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <algorithm>

using namespace std;

// Function to generate a secure random password
string generatePassword(int length, bool useUpper, bool useLower, bool useDigits, bool useSpecial) {
    if(length <= 0) {
        throw invalid_argument("Password length must be greater than 0");
    }

    string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string lower = "abcdefghijklmnopqrstuvwxyz";
    string digits = "0123456789";
    string special = "!@#$%^&*()-_=+[]{}|;:,.<>?/";
    string allChars = "";

    if(useUpper) allChars += upper;
    if(useLower) allChars += lower;
    if(useDigits) allChars += digits;
    if(useSpecial) allChars += special;

    if(allChars.empty()) {
        throw invalid_argument("At least one character type must be selected");
    }

    vector<char> password;

    // Ensure at least one character from each selected type
    if(useUpper) password.push_back(upper[rand() % upper.size()]);
    if(useLower) password.push_back(lower[rand() % lower.size()]);
    if(useDigits) password.push_back(digits[rand() % digits.size()]);
    if(useSpecial) password.push_back(special[rand() % special.size()]);

    // Fill remaining length
    while(password.size() < static_cast<size_t>(length)) {
        password.push_back(allChars[rand() % allChars.size()]);
    }

    // Shuffle password to avoid predictable patterns
    random_shuffle(password.begin(), password.end());

    return string(password.begin(), password.end());
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    cout << "=== Secure Random Password Generator ===\n";
    int length;
    cout << "Enter password length: ";
    cin >> length;

    char choice;
    bool useUpper, useLower, useDigits, useSpecial;

    cout << "Include uppercase letters? (y/n): ";
    cin >> choice;
    useUpper = (choice == 'y' || choice == 'Y');

    cout << "Include lowercase letters? (y/n): ";
    cin >> choice;
    useLower = (choice == 'y' || choice == 'Y');

    cout << "Include numbers? (y/n): ";
    cin >> choice;
    useDigits = (choice == 'y' || choice == 'Y');

    cout << "Include special characters? (y/n): ";
    cin >> choice;
    useSpecial = (choice == 'y' || choice == 'Y');

    try {
        string password = generatePassword(length, useUpper, useLower, useDigits, useSpecial);
        cout << "\n🔐 Generated Password: " << password << "\n";
    } catch(const invalid_argument &e) {
        cout << "\n❌ Error: " << e.what() << "\n";
    }

    return 0;
}
