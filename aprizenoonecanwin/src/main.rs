use std::io::{self, BufRead};

fn main() {
    let mut lines = io::stdin().lock().lines();

    let line = lines.next().unwrap().unwrap();
    let mut items = line.split_whitespace();
    items.next();
    let x:i32 = items.next().unwrap().parse().unwrap();

    let line = lines.next().unwrap().unwrap();
    let mut items: Vec<i32> = line.split_whitespace()
        .map(|s| s.parse().unwrap()).collect();
    items.sort_unstable();

    if items.len() == 1 { return println!("1"); }
    if items[0] > x { return println!("1"); }
    for i in 1..items.len() {
        if items[i] + items[i-1] > x { return println!("{}", i); }
    }
    return println!("{}",items.len()); 
}
