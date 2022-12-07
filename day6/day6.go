package main

//go through string from file input.txt with cursor
//if last 4 chars behind cursor are unique, print index of cursor
//if not, move cursor forward 1
//if cursor reaches end of string, stop

import (
	"bufio"
	"fmt"
	"os"
)

func scanBuffer(buffer []string) bool {
	//iterate through buffer
	//if all chars are unique, return true
	//if not, return false and remove first char if length = 4
	bufferMap := make(map[string]bool)
	//dupes := true
	for _, char := range buffer {
		bufferMap[char] = true
	}
	// if len(buffer) == 4 {
	// 	buffer = buffer[1:]
	// 	fmt.Println("buffer: ", buffer)
	// }
	fmt.Println("bufferMap: ", buffer)
	if len(bufferMap) == 14 {
		return true
	} else {
		return false
	}
}
func main() {
	//read input from input.txt
	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var input string
	//var bufferToScan []string
	for scanner.Scan() {
		fmt.Println(scanner.Text())
		input = scanner.Text()
	}
	var bufferToScan []string
	for index, char := range input {
		//fmt.Println("char: ", string(char))
		//fmt.Println("index: ", index)
		bufferToScan = append(bufferToScan, string(char))
		bufferCheck := scanBuffer(bufferToScan)
		if bufferCheck {
			fmt.Println("Buffer at index: ", index+1)
			break
		} else if len(bufferToScan) == 14 {
			bufferToScan = bufferToScan[1:]
		}
	}
}
