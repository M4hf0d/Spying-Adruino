# Spying API Documentation (v1)

This document provides a comprehensive guide to the Spying API, detailing its functionalities and how to interact with it.

## Getting Started

This API uses JSON for both request and response bodies. It requires Basic Auth for authentication (details in the Security section).

**Base URL:** http://127.0.0.1:8000/api

## Security

The Spying API utilizes Basic Authentication for access control. You will need to provide a username and password in the authorization header of your requests.

## Data Endpoints

* **GET /data/:** Retrieves a list of data objects. 
    * Response: Array of `Data` objects (see Data Model definition).
* **POST /data/:** Creates a new data object.
    * Request Body: JSON object representing the new `Data` object (see Data Model definition).
    * Response: The created `Data` object.
* **GET /data/{id}/:** Retrieves a specific data object by its ID.
    * Path Parameter: `id` (integer) - Unique identifier of the data object.
    * Response: The `Data` object with the corresponding ID.
* **PUT /data/{id}/:** Updates a data object completely.
    * Path Parameter: `id` (integer) - Unique identifier of the data object.
    * Request Body: JSON object representing the updated `Data` object (see Data Model definition).
    * Response: The updated `Data` object.
* **PATCH /data/{id}/:** Updates a data object partially.
    * Path Parameter: `id` (integer) - Unique identifier of the data object.
    * Request Body: JSON object containing the properties to be updated (see Data Model definition).
    * Response: The updated `Data` object.
* **DELETE /data/{id}/:** Deletes a data object.
    * Path Parameter: `id` (integer) - Unique identifier of the data object to be deleted.
    * Response: No content (status code 204).

## GPS Endpoints

* **GET /gps/:** Retrieves a list of GPS points.
    * Optional Query Parameter: `ordering` (string) - Field to use for ordering results (e.g., "latitude", "longitude").
    * Response: Array of `GpsPoint` objects (see GPS Point Model definition).
* **POST /gps/:** Creates a new GPS point.
    * Request Body: JSON object representing the new `GpsPoint` object (see GPS Point Model definition).
    * Response: The created `GpsPoint` object.
* **GET /gps/{id}/:** Retrieves a specific GPS point by its ID.
    * Path Parameter: `id` (integer) - Unique identifier of the GPS point.
    * Response: The `GpsPoint` object with the corresponding ID.
* **PUT /gps/{id}/:** Updates a GPS point completely.
    * Path Parameter: `id` (integer) - Unique identifier of the GPS point.
    * Request Body: JSON object representing the updated `GpsPoint` object (see GPS Point Model definition).
    * Response: The updated `GpsPoint` object.
* **PATCH /gps/{id}/:** Updates a GPS point partially.
    * Path Parameter: `id` (integer) - Unique identifier of the GPS point.
    * Request Body: JSON object containing the properties to be updated (see GPS Point Model definition).
    * Response: The updated `GpsPoint` object.
* **DELETE /gps/{id}/:** Deletes a GPS point.
    * Path Parameter: `id` (integer) - Unique identifier of the GPS point to be deleted.
    * Response: No content (status code 204).

## Data Model

* **id (integer, read-only):** Unique identifier of the data object.
* **cid (integer, nullable):** An optional integer value associated with the data.
* **message (string, max length 900, nullable):** A message string associated with the data, with a maximum length of 900 characters.

## GPS Point Model

* **id (integer, read-only):** Unique identifier of the GPS point.
* **latitude (string, decimal format):** Latitude coordinate of the GPS point.
* **longitude (string, decimal format):** Longitude coordinate of the GPS point.
* **timestamp (string, date-time format, nullable):** Optional timestamp associated with the GPS point.

## Additional Notes

* This API documentation is intended to provide a clear and comprehensive overview of the available functionalities.
* Consider including code samples for common use cases to further enhance developer experience.
* Error handling and specific
