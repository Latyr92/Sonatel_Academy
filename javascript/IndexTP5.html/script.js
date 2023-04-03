const questions = [
                     {
                       question: "Quel est le langage de programmation le plus populaire?",
                       choices: ["JavaScript", "Python", "Java"],
                       correctAnswer: 1
                     },
                     {
                       question: "Quelle est la capitale de la France?",
                       choices: ["Londres", "Paris", "Madrid"],
                       correctAnswer: 1
                     },
                     {
                       question: "Quelle est la couleur du ciel par temps clair?",
                       choices: ["Bleu", "Vert", "Rouge"],
                       correctAnswer: 0
                     },
                     {
                       question: "Quel est le plus grand océan de la Terre ?",
                       choices: ["Atlantique", "Indien", "Arctique", "Pacifique"],
                       correctAnswer: 0
                     },
                     {
                       question: "Quelle est la capitale du Canada ?",
                       choices: ["Montréal", "Toronto", "Ottawa", "Vancouver"],
                       correctAnswer: 2
                     },
                     {
                       question: "Quel est le plus grand désert du monde ?",
                       choices: ["Sahara", "Antarctique", "Arctique", "Gobi"],
                       correctAnswer: 0
                     },
                     {
                       question: "Quelle est la plus haute montagne du monde ?",
                       choices: ["Mont Everest", "Mont Kilimandjaro", "Mont Blanc", "Mont Fuji"],
                       correctAnswer: 0
                     }
                   ];
                   
                   let currentQuestion = 0;
                   let score = 0;
                   
                   const questionElement = document.getElementById("question");
                   const choicesElement = document.getElementById("choices");
                   const submitButton = document.getElementById("submit");
                   const scoreElement = document.getElementById("score");
                   
                   displayQuestion();
                   
                   function displayQuestion() {
                     const question = questions[currentQuestion];
                   
                     questionElement.innerText = question.question;
                     choicesElement.innerHTML = '';
                   
                     question.choices.forEach((choice, index) => {
                       const label = document.createElement('label');
                       label.innerHTML = `<input type="radio" name="choice" value="${index}">${choice}`;
                       choicesElement.appendChild(label);
                     });
                   
                     submitButton.disabled = false;
                   }
                   
                   function checkAnswer() {
                     const choices = document.getElementsByName("choice");
                     let selectedChoice = -1;
                   
                     for (let i = 0; i < choices.length; i++) {
                       if (choices[i].checked) {
                         selectedChoice = choices[i].value;
                         break;
                       }
                     }
                   
                     if (selectedChoice == questions[currentQuestion].correctAnswer) {
                       score++;
                     }
                   
                     currentQuestion++;
                   
                     if (currentQuestion >= questions.length) {
                       displayScore();
                     } else {
                       displayQuestion();
                     }
                   }
                   
                   function displayScore() {
                     scoreElement.innerText = `Vous avez obtenu ${score} sur ${questions.length} points.`;
                     submitButton.innerText = 'Rejouer';
                     submitButton.disabled = false;
                     submitButton.removeEventListener('click', checkAnswer);
                     submitButton.addEventListener('click', resetQuiz);
                   }
                   
                   function restartQuiz() {
                         currentQuestion = 0;
                         score = 0;
                         displayQuestion();
                         const scoreElement = document.getElementById("score");
                         scoreElement.textContent = "";
                       }
                       
                     document.getElementById("submit").addEventListener("click", checkAnswer);
                     document.getElementById("reset").addEventListener("click", restartQuiz);