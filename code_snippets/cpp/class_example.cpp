#include<iostream>
class Person {
public:
    std::string name;
    Person(std::string n) : name(n) {}
    void greet() {
        std::cout << "Hello, " << name << std::endl;
    }
};
