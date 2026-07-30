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
func fibonnacii(n int) int {
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	return fibonnacii(n-1) + fibonnacii(n-2)
}

// fabonicii with for loop

func faboF(n int) int {
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 1
	}
	theSum := 1
	fabp := 1
	fabc := 1
	for i := 0; i < n-1; i++ {
		theSum = fabc + fabp
		fabp = fabc
		fabc = theSum
	}
	return theSum
}
