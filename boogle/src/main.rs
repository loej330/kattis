use std::{collections::HashSet, io::{self, BufRead}, usize};

const MOVES: [(i32, i32); 8] = [
    (-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1),
];

fn boggle(board: [[char; 4]; 4], word: &Vec<char>) -> bool {
    fn search(i: usize, point: (i32, i32), visited: &mut [[bool; 4]; 4], 
    board: [[char; 4]; 4], word: &Vec<char>) -> bool {
        if i == word.len() { return true; }
        for (x, y) in MOVES {
            let npoint = (point.0 + x, point.1 + y);
            if npoint.0 < 4 && npoint.0 >= 0 && npoint.1 < 4  && npoint.1 >= 0
            && board[npoint.0 as usize][npoint.1 as usize] == word[i] 
            && !visited[npoint.0 as usize][npoint.1 as usize] {
                visited[npoint.0 as usize][npoint.1 as usize] = true;
                let result = search(i+1, npoint, visited, board, word);
                visited[npoint.0 as usize][npoint.1 as usize] = false;
                return result;
            }
        }
        return false;
    }
    let mut visited = [[false; 4]; 4];
    for i in 0..4 {
        for j in 0..4 {
           if board[i][j] == word[0] {
               let point = (i as i32, j as i32); 
               visited[i][j] = true;
               if search(1, point, &mut visited, board, word) { return true; }
               visited[i][j] = false;
           }
        }
    }
    return false;
}

fn main() {
    let mut lines = io::stdin().lock().lines();
    let w: usize = lines.next().unwrap().unwrap().parse().unwrap();
    let mut words: HashSet<Vec<char>> = HashSet::new();
    for _ in 0..w { words.insert(lines.next().unwrap().unwrap().chars().collect()); }
    let b: i32 = lines.nth(1).unwrap().unwrap().parse().unwrap();
    for _ in 0..b {
        let mut board: [[char; 4]; 4] = Default::default();
        for i in 0..4 {
            for (j, c) in lines.next().unwrap().unwrap().chars().enumerate() {
                board[i][j] = c; 
            }
        }
        lines.next();
        let mut longest: String = String::from("");
        let mut score = 0;
        let mut n_found = 0;
        for word in &words {
            if boggle(board, word) {
                let word_str: String = word.into_iter().collect();
                if word_str.len() > longest.len() { longest = word_str; }
                else if word.len() == longest.len() {
                    if word_str < longest { longest = word_str; }
                }
                score += match word.len() {
                    3 | 4 => 1, 5 => 2, 6 => 3, 7 => 5, 8 => 11, _ => 0,
                };
                n_found += 1;
            }
        }
        println!("{} {} {}", score, longest, n_found);
    }
}
