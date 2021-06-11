#include <iostream>
// ofstream is write
// ifstream is read
// this is both read and write
#include <fstream>
using namespace std;

int main() {
    // ofstream myfile;
    // myfile.open("example.txt");
    // if (myfile.is_open()) {
    //     myfile << "This is a line. \n";
    //     myfile << "This is another line. \n";
    //     myfile.close();
    // }
    // else cout << "Unable to open file.";

    string line;
    ifstream myfile("example.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            cout << line << '\n';
        }
        myfile.close();
    }
    else cout << "Unable to open file.";
    return 0;
}

// ios::in	    Open for input operations.
// ios::out	    Open for output operations.
// ios::binary	Open in binary mode.
// ios::ate	    Set the initial position at the end of the file.
//              If this flag is not set, the initial position is the beginning of the file.
// ios::app	    All output operations are performed at the end of the file, appending the content to the current content of the file.
// ios::trunc	If the file is opened for output operations and it already existed, its previous content is deleted and replaced by the new one.

// https://www.cplusplus.com/doc/tutorial/files/