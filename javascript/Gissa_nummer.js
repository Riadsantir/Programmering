function guessNumber() {
    const number = Math.floor(Math.random() * 100) + 1;
    const guess = parseInt(prompt("Gissa ett nummer mellan 1 och 100: "));
    if (guess === number) {
        alert("Grattis, du har gissat rätt!");
    } else {
        alert(`Tyvärr, det rätta numret var ${number}.`);
    }
}

guessNumber();

