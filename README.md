# python-chat - a programming assessment

## Description

A minimal single-threaded Python chat.

## Requirements

UDP group chat without threads. Write a script “gchat.py” such that when it is called with an argument, which must be an IP address of a server, it acts as a client, and when it is called without an argument, it acts as a server. Example, “python3 gchat.py 54.38.181.152” is for running a client and “python3 gchat.py” is for running as a server (in this example must be run obviously on a machine with IP address 54.38.181.152). The script provides a kind of a group chat. The communication is in UDP only (so packets sometimes can be lost). You must not use threads or processes. Everything must be in a single main thread. You must use only the low-level modules (no modules where all or almost all is done). The server listens the UDP port 12345. The client sends the keyboard input lines to the server via UDP (one packer per each input line). Both, the client and the server, display every UDP packet coming from the network as a text with a suffix indicating the source, such as “Hello there! by ('54.38.181.152', 12345)”. Whatever text the server receives from keyboard, it transmits the text to all its clients. Whenever the server receives a message from a network, it retransmits the message to all other clients (except to the client where from the message is received). Whenever someone sends a message to the server, the server considers it as a new client.
