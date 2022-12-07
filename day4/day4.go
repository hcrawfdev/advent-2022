// program that checks for overlapping ranges of integers formatted as: 1-4,4-4, 6-8, etc
// and returns the number of overlapping ranges
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	//read input from input.txt
	file, _ := os.Open("test_input.txt")
	totalOverlaps := 0
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var input []string
	for scanner.Scan() {
		//fmt.Println(scanner.Text())
		input = append(input, scanner.Text())
	}

	//convert input to int slices
	var ranges [][][]int
	for _, line := range input {

		splitLine := strings.Split(line, ",")
		fmt.Println("split line: ", splitLine)
		setOfTwo := [][]int{}
		for _, line := range splitLine {
			parts := strings.Split(line, "-")
			fmt.Println("parts: ", parts)
			start, _ := strconv.Atoi(parts[0])
			end, _ := strconv.Atoi(parts[1])
			// if start == end {
			// 	start = math.MinInt32
			// }
			intArr := []int{start, end}
			setOfTwo = append(setOfTwo, intArr)
			sort.Slice(setOfTwo, func(i, j int) bool {
				return (setOfTwo[i][1] - setOfTwo[i][0]) > (setOfTwo[j][1] - setOfTwo[j][0])
			})
		}
		ranges = append(ranges, setOfTwo)
		fmt.Println("ranges after line: ", ranges)
	}
	//fmt.Println("ranges before: ", ranges)

	fmt.Println("ranges: ", ranges)
	//merge overlapping ranges

	for x := 0; x < len(ranges); x++ {
		//fmt.Println("x: ", ranges[x])
		if ranges[x][0][0] <= ranges[x][1][0] && ranges[x][0][1] >= ranges[x][1][1] {
			fmt.Println("overlapping")
			totalOverlaps++
			continue
		}

		// if ranges[x][1][0] <= ranges[x][0][1] && ranges[x][1][1] >= ranges[x][1][0] {
		// 	fmt.Println("overlapping")
		// 	totalOverlaps++
		// 	continue
		// }
	}

	//count the number of ranges
	fmt.Println("total overlaps: ", totalOverlaps)
}

//between 448 and 841
