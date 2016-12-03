package main

// NOTE: As I am learning Golang, this script might contain newbie comments
// explaining some of the functions I use (e.g. paste from REPL)
// As a REPL, gore has been used - https://github.com/motemen/gore

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func isTriangle(a, b, c int) bool {
    if a + b > c && a + c > b && b + c > a {
        return true
    }
    return false
}

func atoi(s string) int {
    val, err := strconv.Atoi(s)

    if err != nil {
        panic(err)
    }

    return val
}

func task1(lines []string) {
    possibleTriangles := 0

    for _, line := range lines {
        line = strings.TrimSpace(line)

        // gore> strings.Fields("1  2\t3")
        // []string{"1", "2", "3"}
        sides := strings.Fields(line)

        if isTriangle(atoi(sides[0]), atoi(sides[1]), atoi(sides[2])) {
            possibleTriangles += 1
        }
    }

    fmt.Println("Task 1")
    fmt.Println("Possible triangles:", possibleTriangles)
}

func task2(lines []string) {
    possibleTriangles := 0

    for i := 0; i < len(lines); i+=3 {
        triple_lines := [][]string {
            strings.Fields(strings.TrimSpace(lines[i])),
            strings.Fields(strings.TrimSpace(lines[i+1])),
            strings.Fields(strings.TrimSpace(lines[i+2])),
        }

        for col_idx := 0; col_idx < len(triple_lines); col_idx++ {
            if isTriangle(atoi(triple_lines[0][col_idx]),
                          atoi(triple_lines[1][col_idx]),
                          atoi(triple_lines[2][col_idx])) {
                possibleTriangles += 1
            }
        }
    }

    fmt.Println("Task 2")
    fmt.Println("Possible triangles:", possibleTriangles)
}

func main() {
    dat, err := ioutil.ReadFile("input.txt")

    if err != nil {
        panic(err)
    }

    // currently dat is []byte = [32 32 55 55 53 32 ...]
    data := string(dat)

    // gore> strings.Split("1 2 3\n11 22 33", "\n")
    // []string{"1 2 3", "11 22 33"}
    lines := strings.Split(data, "\r\n")

    task1(lines)
    task2(lines)
}
