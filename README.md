# MCP Server with Docker

This project demonstrates how to run an MCP (Model Control Protocol) server using Docker throght stdio protocol (locally) and SSE protocol (locally and in remote). 

NOTE:  you can run the SEE protocol locally if you remove the comment on the host adress = 0.0.0.0 (which means Localhost) or comment it if you plan to deploy the web service somewhere so you can access it remotely. In any case for both cases be sure that the port exposed in the docker file and the one set in the server.py file are identical so to allow the SSE communication.

## Prerequisites

- Docker installed on your system
- Acount on Render VPS service (for the external deployment and then remotely access)

## General Project Structure (for both stdio and sse case)

- `server.py`: The MCP server implementation with a simple tool
- `Dockerfile`: Instructions for building the Docker image
- `requirements.txt`: Python dependencies for the project

