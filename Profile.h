#pragma once
#ifndef PROFILE_H
#define PROFILE_H
#include <string>
#include <fstream>
#include <iostream>


class Packet
{
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

    char* SerializeData()
    {

        CRC = CalculateCRC();

        if (TxBuffer)
        {

            delete[] TxBuffer;
        }

        // Set to the total number of bytes
        int TotalSize = sizeof(Header) + Head.Length;

        // Allocate memory to buffer
        TxBuffer = new char[TotalSize];

        // Copy the header information
        memcpy(TxBuffer, &Head, sizeof(Header));

        // Copy the body
        memcpy(TxBuffer + sizeof(Header), &profile, Head.Length);

        // Copy the CRC
		memcpy(TxBuffer + sizeof(Header) + Head.Length, &CRC, sizeof(CRC));

        // Return refence point to the packet
        return TxBuffer;
    };

    // Set up basic initialize the profile with provided data
    Profile(const std::string &uName, const std::string &fName, const std::string &lName,
            const std::string &b, const std::string &uClass, int i, int vCount)
        : userName(uName), firstName(fName), lastName(lName),
          bio(b), userClass(uClass), id(i), voteCount(vCount) {}

    // When the server receives a serialized Profile string from the client, it can be reduced to a Profile object for saving and update data
    static Profile deserialize(const std::string &data)
    {
        std::istringstream dataStream(data);
        std::string userName, firstName, lastName, bio, userClass;
        int id, voteCount;

        std::getline(dataStream, userName, ',');
        std::getline(dataStream, firstName, ',');
        std::getline(dataStream, lastName, ',');
        std::getline(dataStream, bio, ',');
        std::getline(dataStream, userClass, ',');

        dataStream >> id;
        dataStream.ignore(); // Ignore the comma
        dataStream >> voteCount;

        return Profile(userName, firstName, lastName, bio, userClass, id, voteCount);
    }

    unsigned int CalculateCRC()
	{
		//Set the CRC to 0xFF00FF00
		CRC = CONSTCRC;
		return CRC;

	}

}
// Save the profile data into file
void saveToFile(const std::string &filePath) const
{
    std::ofstream outFile(filePath, std::ios::app);
    if (!outFile)
    {
        std::cerr << "Could not open file for writing: " << filePath << std::endl;
        return;
    }
    outFile << serialize() << std::endl;
    outFile.close();
}
}
;

#endif // PROFILE_H
