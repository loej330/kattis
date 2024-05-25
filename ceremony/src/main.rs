use std::{collections::BTreeMap, io::{self, BufRead}};

fn main() {
    let line = io::stdin().lock().lines().nth(1).unwrap().unwrap();

    let mut towers: BTreeMap<i32, i32> = std::collections::BTreeMap::new();
    for item in line.split_whitespace() {
        let height: i32 = item.parse().unwrap();
        towers.entry(height).and_modify(|x| *x += 1).or_insert(1);
    }
    let mut towers: Vec<(i32, i32)> = towers.into_iter().collect();

    let mut moves = 0;
    while towers.len() > 0 {
        let tallest = towers.last().unwrap();
        if tallest.0 as usize > towers.len() {
            moves += tallest.1;
            towers.pop();
        } else {
            towers.iter_mut().for_each(|x| x.0 -= 1);
            towers.retain(|x| x.0 > 0);
            moves += 1
        }
    }
    println!("{moves}");
}
