#include <iostream>

int main() {
    int variable = 10;
    auto address_of_variable = &variable; // this is a pointer
    auto value_of_variable = variable;

    std::cout << "variable: " << variable << '\n';
    std::cout << "address of variable: " << address_of_variable << '\n';
    std::cout << "value of variable: " << value_of_variable << '\n';
    std::cout << "value with dereference from address: " << *address_of_variable << '\n';
    std::cout << std::endl;
    // since pointers can be dereferenced, the type of a pointer must be declared
    // when declaring a pointer
    int * num_ptr; //recall that the * can be writter as int* num_ptr of int *num_ptr as well
    // here, we declared that num_ptr will point to an int
    int num_value = 15;
    num_ptr = &num_value;
    // char char_value = 'a';
    // num_ptr = &char_value;
    // the above line causes an error
    std::cout << "value of num_value: " << num_value << '\n';
    std::cout << "value with dereference of num_ptr " << *num_ptr << '\n';
    std::cout << "Now change num_value through the pointer.\n";
    *num_ptr = 20;
    std::cout << "new value of num_value: " << num_value << '\n';
    std::cout << "new value with dereference of num_ptr " << *num_ptr << '\n';
    std::cout << std::endl;

    // pointers and arrays
    int test_array[5];
    int * array_ptr = test_array;

    std::cout << "value of first entry of test_array: " << test_array[0] << '\n';
    std::cout << "value with dereference of array_ptr " << *array_ptr << '\n';
    std::cout << "value of third entry of test_array: " << test_array[2] << '\n';
    std::cout << "value with dereference of array_ptr " << *(array_ptr + 2) << '\n';
    

}