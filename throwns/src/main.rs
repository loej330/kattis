use std::io::{self, BufRead};

fn main() {
    let mut lines = io::stdin().lock().lines();

    let line = lines.next().unwrap().unwrap();
    let mut items = line.split_whitespace();
    let n = items.next().unwrap().parse::<i32>().unwrap();

    let line = lines.next().unwrap().unwrap();
    let mut items = line.split_whitespace();
    let mut throws: Vec<String> = Vec::new();

    while let Some(item) = items.next() {
        if item == "undo" {
            for _ in 0..items.next().unwrap().parse::<i32>().unwrap() {
                throws.pop();
            }
        } else {
            throws.push(item.to_string());
        }
    }

    let mut id = 0;
    for throw in throws {
        let throw = throw.parse::<i32>().unwrap();
        id = (id + throw).rem_euclid(n);
    }
    println!("{}", id);
}
