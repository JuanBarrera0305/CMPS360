package com.example.springbootrest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/welcome")
    public String welcome() {
        return "Welcome to Spring Boot!";
    }

    @GetMapping("/greet")
    public String greet(@RequestParam(value = "name", defaultValue = "Guest") String name) {
        // Validate that 'name' only contains letters (no numbers or special characters)
        if (!name.matches("[a-zA-Z]+")) {
            // Throw an IllegalArgumentException with a custom error message
            throw new IllegalArgumentException("Invalid name format. Only letters are allowed.");
        }
        
        return "Hello, " + name + "!";
    }
}
