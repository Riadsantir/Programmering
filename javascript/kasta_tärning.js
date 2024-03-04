// function kastaTarning() {
//     return Math.floor(Math.random() * 6) + 1;
// }

// const tarningskast = Array.from({ length: 5 }, kastaTarning);

// if (tarningskast.every(tarning => tarning === tarningskast[0])) {
//     console.log("Yatzy");
// } else {
//     console.log("Inte Yatzy");
// }

function kastaTarning() {
    return Math.floor(Math.random() * 6) + 1;
}

let tarningskast;
do {
    tarningskast = Array.from({ length: 5 }, kastaTarning);
    if (tarningskast.every(tarning => tarning === tarningskast[0])) {
        console.log("Yatzy");
    } else {
        console.log("Inte Yatzy");
    }
} while (!tarningskast.every(tarning => tarning === tarningskast[0]));
