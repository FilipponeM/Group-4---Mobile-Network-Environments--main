# Group-4---Mobile-Network-Environments-
Group project 
## Group Idea: Online Voting System

****************Summary:****************

- this program would allow users to connect to a server, register for candidacy with their name, id, picture, etc
- users could connect to cast their votes upon who they would like to elect
- low level program could be used for a group leader vote, school election, etc

## Online Voting System Concepts

********Two Software Applications********
- the client application could be the voting and submission of participants, while the server can manage the voting process and storing the candidates information

********OOP Principles********
- we will code in C++ and python
- can code the server or client connections/hosts with C++ and use OOP

********Data Transfer With Pre-Defined Structure********
- the structured data packet to be transmitted from client to the server could be
    - voter ID
    - candidate ID
    - other relevant info

********Dynamically Allocated Element in Data Packet********
- not sure, maybe use pointers and dynamically allocated elements to help with certain kinds of data

********Logging of Transmitted and Received Data Packets********
- add a log to record all the votes that were processed

********Operational State Machine in the Server Application********
- maybe something to handle the stages of voting?
    - pre voting (candidates)
    - open voting
    - closed voting

********Large Data Transfer Initiation Command********
- could potentially have the option to upload a picture for the candidates, have a visual representation of what they look like

********Server Requires User Authentication********
- maybe a valid account, password, etc, unsure

## To Do C++
- define data structure
    - classes for voters, candidates, votes, etc
- implement server
    - setup server to handle requests
    - allow comms between client and server
    - handle authentication
    - be able to receive and process/log votes
- client
    - user interface to vote
    - contact and connect with the server
    - users have to authenticate before voting (password, account, key)
    - send info to the servers

## To Do Python
- command line or GUI interface (simple)
- authentication? (may be easier)
- logging data packets
- upload/handle jpeg?