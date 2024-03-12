#include <windows.networking.sockets.h>
#include <iostream>
#include "Profile.h"
#pragma comment(lib, "Ws2_32.lib")

using namespace std;
int main()
{
	WSAData wsaData;
	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
		return 0;
	}

	SOCKET serverSocket;
	if ((serverSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == INVALID_SOCKET) {
		WSACleanup();
		return 0;
	}

	sockaddr_in SvrAddr;
	SvrAddr.sin_family = AF_INET;
	SvrAddr.sin_addr.s_addr = INADDR_ANY;
	SvrAddr.sin_port = htons(27000);

	if (bind(serverSocket, (struct sockaddr*)&SvrAddr, sizeof(SvrAddr)) == SOCKET_ERROR)
	{
		closesocket(serverSocket);
		WSACleanup();
		return 0;
	}

	if (listen(serverSocket, 1) == SOCKET_ERROR)
	{
		closesocket(serverSocket);
		WSACleanup();
		return 0;
	}

	SOCKET connectionSocket;
	if ((connectionSocket = accept(serverSocket, NULL, NULL)) == SOCKET_ERROR) 
	{
		closesocket(serverSocket);
		WSACleanup();
		return 0;
	}

	char RxBuffer[128] = {};
	int bytesReceived = recv(connectionSocket, RxBuffer, sizeof(RxBuffer), 0);
	if (bytesReceived > 0) 
	{
		RxBuffer[bytesReceived] = '\0';
		// Deserialize the received data into a Profile object and save/update
		Profile profile = Profile::deserialize(string(RxBuffer));
		profile.saveToFile("profiles.txt"); // Save to prifile.txt, if need we can change the path
	}
	recv(connectionSocket, RxBuffer, sizeof(RxBuffer), 0);

	closesocket(connectionSocket);
	closesocket(serverSocket);
	WSACleanup();
	return 1;
}