// Read Incoming Data
// Matteo Filippone

#include <string>
#include <fstream>
#include <iostream>

class ReadDataClient{

    struct Header
    {
        int Length; // Length of packet
    } Head;

    struct Profile
    {
        // Basic Account setting
        std::string userName;
        std::string firstName;
        std::string lastName;
        std::string bio;
        std::string userClass;
        int id;
        int voteCount;

    } profile;

    char *TxBuffer;

    unsigned int CRC;

    const unsigned int CONSTCRC = 0xFF00FF00;

public:



}