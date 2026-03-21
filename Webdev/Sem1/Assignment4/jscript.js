const quizQuestions = [
  { question: "What is the capital of France?", answer: "paris" },
  { question: "What does HTML stand for?", answer: "hypertext markup language" },
  { question: "What keyword makes a variable in JavaScript?", answer: "let" },
  { question: "Which symbol is used for comments in JS?", answer: "//" },
  { question: "What number does an array start with?", answer: "0" }
];
// function to run the quiz
function runQuiz() {
  let score = 0;

  for (let i = 0; i < quizQuestions.length; i++) {

    let userAnswer = prompt(quizQuestions[i].question);
    
    userAnswer = userAnswer.toLowerCase().trim();

    if (userAnswer === quizQuestions[i].answer) {
      alert("Correct! Nice job.");
      score++; // give a point
    } else {
      alert("Incorrect. The right answer is: " + quizQuestions[i].answer);
    }
  }

  // show final score
  alert("Quiz finished! You scored " + score + " out of " + quizQuestions.length);
}

runQuiz();
