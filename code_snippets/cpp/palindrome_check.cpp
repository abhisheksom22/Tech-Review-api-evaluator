#include<iostream>
bool isPalindrome(std::string s) {
    return s == std::string(s.rbegin(), s.rend());
}
