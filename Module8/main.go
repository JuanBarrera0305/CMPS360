package main

import (
	"io"
	"net/http"
	"os"
)

func main() {

	http.HandleFunc("/", Handler)
	http.ListenAndServe(":3030", nil)

}

func Handler(w http.ResponseWriter, r *http.Request) {
	//Getting the data from the request
	f, _ := os.Open("./models.txt.") //File to
	io.Copy(w, f)                    //Sending it the client

}
