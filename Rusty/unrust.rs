const CHARSET: &[u8] = b"QWlKoxp3mT9EeRb4YzgG6rNj1OLvZ5SDfMBaXtP8JyIFVH07uh2wicdnUAC#@q";

fn main() {
    let encoded = "OPhMOnVheP1hRaOa1Pmi1GrBbGm21PRaepxXOPxMeG1iOaYd1ji=";
    let encoded_bytes = encoded.as_bytes();

    let mut temp = 0u32;
    let mut temp_len = 0u8;
    let mut decoded = Vec::new();

    for &byte in encoded_bytes {
        if byte == b'=' {
            break; // Padding character, end of encoding
        }
        let value = CHARSET.iter().position(|&c| c == byte).unwrap() as u32;
        temp = (temp << 6) | value;
        temp_len += 6;

        while temp_len >= 8 {
            temp_len -= 8;
            decoded.push((temp >> temp_len) as u8);
        }
    }

    let decoded_str = String::from_utf8(decoded).unwrap();
    println!("{}", decoded_str);
}

