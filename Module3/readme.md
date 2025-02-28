# Spring Boot REST API

This is a simple Spring Boot REST API that provides basic endpoints for greeting users.

## Project Setup

### Prerequisites
Ensure you have the following installed:
- Java 17 or later
- Maven
- Git

### Clone the Repository
git clone https://github.com/JuanBarrera0305/CMPS360.git
cd CMPS360/Module3


### Build and Run the Project
To build and run the application, use:
mvn clean install
mvn spring-boot:run


## API Endpoints

### 1. Welcome Message
**GET /welcome**
Returns a static welcome message.

**Example Request:**
curl http://localhost:8080/welcome


**Example Response:**
"Welcome to Spring Boot!"


### 2. Greet User
**GET /greet?name={name}**
Returns a personalized greeting. If no name is provided, it defaults to "Guest." The name parameter must only contain letters.

**Example Requests:**
curl http://localhost:8080/greet?name=Alice
curl http://localhost:8080/greet


**Example Responses:**
"Hello, Alice!"
"Hello, Guest!"


### Invalid Request Handling for /greet
If the name parameter contains numbers or special characters, the API will return a 400 Bad Request error with a custom message indicating invalid input.

**Example Request (Invalid Name):**
curl http://localhost:8080/greet?name=John123


**Example Response (Invalid Name):**
{
  "error": "Invalid name format. Only letters are allowed."
}


## Error Handling
- If required parameters are missing (e.g., if the name parameter is not provided when it is required), the API will return a 400 Bad Request error.
- If an invalid name is provided (such as one containing numbers or special characters), the API will return a 400 Bad Request error with the message "Invalid name format. Only letters are allowed."
- All error responses follow a JSON format for consistency.

**Example Error Response:**
{
  "error": "An unexpected error occurred: Required request parameter 'name' for method parameter type String is not present"
}


## Conclusion
This API demonstrates a basic Spring Boot application with simple endpoints and error handling for invalid inputs.

