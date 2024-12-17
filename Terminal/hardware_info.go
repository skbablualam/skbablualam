package main

import (
	"fmt"
	"os"
	"runtime"
)

func main() {
	// Operating System Information
	fmt.Println("System Information:")
	fmt.Println("====================")
	fmt.Printf("Operating System: %s\n", runtime.GOOS)
	fmt.Printf("Architecture: %s\n", runtime.GOARCH)

	// Hostname
	hostname, err := os.Hostname()
	if err != nil {
		fmt.Printf("Error retrieving hostname: %v\n", err)
	} else {
		fmt.Printf("Hostname: %s\n", hostname)
	}

	// CPU Details
	fmt.Printf("Number of CPUs: %d\n", runtime.NumCPU())

	// Go Version
	fmt.Printf("Go Version: %s\n", runtime.Version())
}
