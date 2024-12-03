package main

import (
	"fmt"
	"regexp"
	"os"
	"strconv"
	"strings"
)

func getSum(input string) int {
	// should be global/const, but w/e
	matcher := regexp.MustCompile(`mul\((?P<X>\d+),(?P<Y>\d+)\)`)

	sum := 0
	for _, matched := range matcher.FindAllStringSubmatch(input, -1) {
		x, _ := strconv.Atoi(matched[1])
		y, _ := strconv.Atoi(matched[2])
		sum += x*y
	}
	return sum;
}

func main() {
	f, _ := os.ReadFile(os.Args[1])
	input := string(f)

	fmt.Printf("Task 1: sum = %d\n", getSum(input))

	splitted := strings.Split(input, "don't()")

	// Whatever is before first dont() is enabled, so just grab all sums
	sum := getSum(splitted[0])

	for _, str := range splitted[1:] {
		// Here, the `str` is after `dont()` so the sum is disabled; we need to look for enabled (`do()`)
	//	fmt.Println("STR", str)
		splitted_do := strings.SplitN(str, "do()", 2)

		if len(splitted_do) > 1 {
			sum += getSum(splitted_do[1])
		}
	}
	fmt.Printf("Task 2: sum = %d\n", sum)
}
