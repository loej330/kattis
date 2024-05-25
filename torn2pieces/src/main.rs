use std::{collections::HashSet, io::{self, BufRead}};

#[derive(Debug)]
struct Station {
    name: String,
    // neighbors: HashSet<Station>,
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    let n = input.next().unwrap().unwrap();
    // let stations: Vec<Station> = input.map(
    let stations: Vec<String> = input.map(
        |line| {
        let word = String::from(line.unwrap());
        // word.split(" ").collect()
        // let lines = line.clone().unwrap().split(",");
        // Station { name: line.unwrap() }
    }).collect();

    print!("{:?}", stations);
}
