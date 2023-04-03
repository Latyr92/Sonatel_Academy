const lengthInput = document.getElementById("length");
const uppercaseCheckbox = document.getElementById("uppercase");
const lowercaseCheckbox = document.getElementById("lowercase");
const numbersCheckbox = document.getElementById("numbers");
const specialCheckbox = document.getElementById("special");
const generateButton = document.getElementById("generate");
const passwordInput = document.getElementById("password");
const copyButton = document.getElementById("copy");

const generatePassword = () => {
                     let charset = "";
                     if (uppercaseCheckbox.checked) {
                     charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                     }
                     if (lowercaseCheckbox.checked) {
                     charset += "abcdefghijklmnopqrstuvwxyz";
                     }
                     if (numbersCheckbox.checked) {
                     charset += "0123456789";
                     }
                     if (specialCheckbox.checked) {
                     charset += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
                     }
                     let password = "";
                     for (let i = 0; i < lengthInput.value; i++) {
                     password += charset[Math.floor(Math.random() * charset.length)];
                     }
                     return password;
};

generateButton.addEventListener("click", () => {
                     if (uppercaseCheckbox.checked || lowercaseCheckbox.checked || numbersCheckbox.checked || specialCheckbox.checked) {
                     passwordInput.value = generatePassword();
                     copyButton.disabled = false;
                     } else {
                     alert("Vous devez cocher au moins un critère de mot de passe.");
                     }
});

copyButton.addEventListener("click", () => {
                     passwordInput.select
});