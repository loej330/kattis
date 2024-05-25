use std::{collections::HashMap, io::{self, BufRead}};

fn main() {
    let mut lines = io::stdin().lock().lines();
    let n:i32 = lines.next().unwrap().unwrap().parse().unwrap();
    for i in 0..n {
        let mut guests = HashMap::new();
        let line = lines.nth(1).unwrap().unwrap();
        for item in line.split_whitespace() {
            if guests.contains_key(item) { *guests.get_mut(item).unwrap() += 1; }
            else { guests.insert(item, 1); }
        }
        for (id, count) in guests {
            if count == 1 {
                println!("Case #{}: {}", i+1, id);
                break;
            }
        }
    }
}
