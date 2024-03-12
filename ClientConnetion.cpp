// Client Connection Class
// Matteo Filippone

#include <windows.networking.sockets.h>
#pragma comment(lib, "Ws2_32.lib")


class ClientConnection{

    SOCKET startConnection(){

    
	//starts Winsock DLLs
	WSADATA wsaData;
	if ((WSAStartup(MAKEWORD(2, 2), &wsaData)) != 0) {
		return 0;
	}

	//initializes socket. SOCK_STREAM: TCP
	SOCKET ClientSocket;
	ClientSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (ClientSocket == INVALID_SOCKET) {
		WSACleanup();
		return 0;
	}

	//Connect socket to specified server
	sockaddr_in SvrAddr;
	SvrAddr.sin_family = AF_INET;						//Address family type itnernet
	SvrAddr.sin_port = htons(27000);					//port (host to network conversion)
	SvrAddr.sin_addr.s_addr = inet_addr("127.0.0.1");	//IP address
	if ((connect(ClientSocket, (struct sockaddr*)&SvrAddr, sizeof(SvrAddr))) == SOCKET_ERROR) {
		closesocket(ClientSocket);
		WSACleanup();
		return 0;
	}

    return ClientSocket;

    }

    void closeConnection(SOCKET ClientSocket){

    closesocket(ClientSocket);
	WSACleanup();

    }

    void sendPacket(SOCKET ClientSocket, char* Tx, int Size){

        send(ClientSocket, Tx, Size, 0);

    }

    void recvPacket(SOCKET RecvSocket, char* Rx, int Size){

        recv(RecvSocket, Rx, Size, 0);

    }

    
}