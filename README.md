# Aruba Streaming API Client Containerized

Aruba Central streaming API follows publish–subscribe model where a topic is subscribed from WebSocket client and Aruba Central will publish continuous data streams to WebSocket client. This approach is different from "polling" where frequent HTTP requests to REST API endpoints are required, in order to get latest data from Aruba Central.

## How to use
Download files to your machine and modify input.json with your values. Issue docker compose up -d to build the image and bring up the container.
