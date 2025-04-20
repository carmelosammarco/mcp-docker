# MCP Server with Docker

This project demonstrates how to run an MCP (Model Control Protocol) server using Docker throght stdio protocol (locally) and SSE protocol (remotelly). However you can run the SEE protocol remotelly if you set active and remove the comment on the host adress to 0.0.0.0 (Localhost). In any case for sse protocol be sure that the port exposed in the docker file and the one set in the server.py file are identical.

## Prerequisites

- Docker installed on your system
- Acount on Render VPS service (for the remote setting)

## General Project Structure (for both stdio and sse case)

- `server.py`: The MCP server implementation with a simple calculator tool
- `Dockerfile`: Instructions for building the Docker image
- `requirements.txt`: Python dependencies for the project

