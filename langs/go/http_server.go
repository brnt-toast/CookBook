// https://www.digitalocean.com/community/tutorials/how-to-make-an-http-server-in-go
package main

import (
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
)

func getRoot( w http.ResponseWriter, r *http.Request) {
	fmt.Printf("got / request\n")
	io.WriteString(w, "This is my website!\n")
}

func getHello(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("got /hello request\n")
	io.WriteString(w, "Hello, HTTP!\n")
}

func main() {
	http.HandleFunc("/", getRoot)
	http.HandleFunc("/Hello", getHello)

	err := http.ListenAndServe(":3333", nil)

	if errors.Is(err, http.ErrServerClosed){
		fmt.Println("server closed")
	} else if err != nil {
		fmt.Printf("error starting erver: %s\n", err)
		os.Exit(1)
	}
}

