use std::fs::File;
use std::io::Read;


fn solve(lines: &String, parse_line: &Fn(&str) -> u32) -> u32 {
    let mut sum : u32 = 0;

    for line in lines.split('\n') {
        sum += parse_line(line);
    }

    sum
}


fn calc_maxmin_diff(line: &str) -> u32 {
    let mut iter = line.split_whitespace()
                       .filter_map(|x| x.parse::<u32>().ok());

    let mut min = match iter.next() {
        Some(num) =>  num,
        None => 0,
    };
    let mut max = min;
    
    for num in iter {
        if num > max {
            max = num;
        }
        else if num < min {
            min = num;
        }
    }
    
    max - min
}


fn parse_task2(line: &str) -> u32 {
    let items : Vec<u32> = line.split_whitespace()
                               .filter_map(|x| x.parse::<u32>().ok())
                               .collect();

    for i in 0 .. items.len() {
        for j in i+1 .. items.len() {
            let val = match items[i] > items[j] {
                true => items[i] as f64 / items[j] as f64,
                false => items[j] as f64 / items[i] as f64,
            };

            if val.fract() == 0.0 {
                return val as u32
            }
        }
    }
    0
}


fn main() {
    let testcase = String::from("5 1 9 5\n7 5 3  \n2 4 6 8");

    let mut file = File::open("./input").expect("Unable to open `input` file");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Unable to read `input` file");

    println!("## TASK 1:");
    println!("Testcase:\n{}\nResult: {}", &testcase, solve(&testcase, &calc_maxmin_diff));
    println!("Result for input: {}\n", solve(&contents, &calc_maxmin_diff));

    let testcase2 = String::from("5 9 2 8\n9 4 7 3\n3 8 6 5");

    println!("## TASK 2");
    println!("Testcase:\n{}\nResult: {}", &testcase2, solve(&testcase2, &parse_task2));
    println!("Result for input: {}\n", solve(&contents, &parse_task2));
}
