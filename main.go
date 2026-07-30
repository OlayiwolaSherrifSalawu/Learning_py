package main

import "fmt"

func main() {
	fmt.Println(factorial(6))
}

func factorial(n int) int {
	if n < 1 {
		return 0
	}
	if n < 2 {
		return 1
	}
	return n * factorial(n-1)
}
