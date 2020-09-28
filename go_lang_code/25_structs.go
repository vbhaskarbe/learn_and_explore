/* Show structures in Go with example */
package main

import "fmt"

type Books struct {
	title   string
	author  string
	subject string
	book_id int
	price   float64
}

func main() {
	var book1 Books
	var book2 Books

	book1.title   = "Go Programming"
	book1.author  = "V. Bhaskar"
	book1.subject = "Go Programming Tutorial"
	book1.book_id = 6495408
	book1.price   = 292.0

	book2.title	  = "Microservices using Go"
	book2.author  = "V. Lehit"
	book2.subject = "Writing Microservices using Go language"
	book2.book_id = 6495409
	book2.price   = 580.0

	fmt.Printf("Book 1 Title  : %s\n", book1.title)
	fmt.Printf("Book 1 Author : %s\n", book1.author)
	fmt.Printf("Book 1 Subject: %s\n", book1.subject)
	fmt.Printf("Book 1 Book Id: %d\n", book1.book_id)
	fmt.Printf("Book 1 Price  : %f\n", book1.price)
	fmt.Println()
	fmt.Printf("Book 2 Title  : %s\n", book2.title)
	fmt.Printf("Book 2 Author : %s\n", book2.author)
	fmt.Printf("Book 2 Subject: %s\n", book2.subject)
	fmt.Printf("Book 2 Book Id: %d\n", book2.book_id)
	fmt.Printf("Book 2 Price  : %f\n", book2.price)

	printBook( book1)

	printBook2( &book2)
}

func printBook( book Books) {
	fmt.Printf("\n-:-:- PRINTING BOOK DETAILS -:-:-\n")
	fmt.Printf("Book Title  : %s\n", book.title)
	fmt.Printf("Book Author : %s\n", book.author)
	fmt.Printf("Book Subject: %s\n", book.subject)
	fmt.Printf("Book Book Id: %d\n", book.book_id)
	fmt.Printf("Book Price  : %f\n", book.price)

}

func printBook2( book *Books) {
	fmt.Printf("\n-:-:- PRINTING BOOK DETAILS WITH POINTER-:-:-\n")
	fmt.Printf("Book Title  : %s\n", book.title)
	fmt.Printf("Book Author : %s\n", book.author)
	fmt.Printf("Book Subject: %s\n", book.subject)
	fmt.Printf("Book Book Id: %d\n", book.book_id)
	fmt.Printf("Book Price  : %f\n", book.price)

}

