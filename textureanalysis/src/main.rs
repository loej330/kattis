use std::io;

fn is_even(texture: &str) -> bool {
    //first passthrough - find stride length
    let mut dist = 0;
    let mut nchar = texture.chars().skip(1);
    while let Some(pixel) = nchar.next() {
        if pixel == '*' { break; }
        dist += 1;
    } 
    //test all passthrough to see if it matches first
    let mut ndist = 0;
    while let Some(pixel) = nchar.next() {
        if pixel == '*' { 
            if ndist != dist { return false; }
            ndist = 0;
        } else {
            ndist += 1;
        }
    } 
    return true;
}

fn main() {
    let mut i = 1;
    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("");
        let texture = input.trim();
        if texture == "END" { break; }

        if is_even(texture) {
            println!("{} EVEN", i);
        } else {
            println!("{} NOT EVEN", i);
        }
        i += 1;
    }
}
