const { brotliCompressSync } = require("zlib");

const input = require("fs").readFileSync("input", "utf-8").split('\r\n\r\n');

const searchString = ['ecl', 'byr', 'iyr', 'hcl', 'eyr', 'hgt', 'pid']

let validator = {
    ecl : { params : }
    byr : { params : }
    iyr : { params : }
    hcl : { params : }
    eyr : { params : }
    hgt :{ params : }
    pid : { params : }
}