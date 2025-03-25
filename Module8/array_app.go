package main

import "fmt"

func main() {
	const conferenceTickets int = 50
	var remainingTickets uint = 50
	conferenceName := "Go Conference"
	bookings := []string{}

	fmt.Println("Welcome to %v booking application. \nWe have a total pf %v are still available. \nGet your tickets here to attend\n")

	//Collect user information
	var firstName string
	var lastName string
	var email string
	var userTickets uint

	//Collect the data
	fmt.Println("Enter yout FirstName: ")
	fmt.Scan(&firstName)

	fmt.Println("Enter your LastName: ")
	fmt.Scan(&lastName)

	fmt.Printf("Enter your Email Address: ")
	fmt.Scan(&email)

	fmt.Println("Enter number of Tickets: ")
	fmt.Scan(&userTickets)

	//Logic for booking systems
	remainingTickets = remainingTickets - userTickets
	bookings = append(bookings, firstName+" "+lastName)

	// Output
	fmt.Printf("Thank you %s %s for booking %d tickets. You will receive a confirmation email at %s\n", firstName, lastName, userTickets, email)
	fmt.Printf("There are %d tickets left for the %s\n", remainingTickets, conferenceName)
	fmt.Printf("These are all the bookings: %v\n", bookings)
}
