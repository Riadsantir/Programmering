function guessNumber() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const number = Math.floor(Math.random() * 100) + 1;

    rl.question('Gissa ett nummer mellan 1 och 100: ', (answer) => {
        const guess = parseInt(answer);
        if (guess === number) {
            console.log("Grattis, du har gissat rätt!");
        } else {
            console.log(`Tyvärr, det rätta numret var ${number}.`);
        }
        rl.close();
    });
}

guessNumber();
