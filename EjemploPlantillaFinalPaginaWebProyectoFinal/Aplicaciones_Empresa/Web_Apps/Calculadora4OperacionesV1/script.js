let currentInput = '';
let currentOperator = '';
let prevInput = '';
let isOperatorClicked = false;

function appendNumber(num) {
    if (currentInput === '0' || isOperatorClicked) {
        currentInput = num;
        isOperatorClicked = false;
    } else {
        currentInput += num;
    }
    updateScreen();
}

function appendOperator(operator) {
    currentOperator = operator;
    prevInput = currentInput;
    isOperatorClicked = true;
}

function calculate() {
    let result;
    const num1 = parseFloat(prevInput);
    const num2 = parseFloat(currentInput);

    switch (currentOperator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        default:
            return;
    }

    currentInput = result.toString();
    updateScreen();
    currentOperator = '';
}

function clearScreen() {
    currentInput = '0';
    currentOperator = '';
    prevInput = '';
    isOperatorClicked = false;
    updateScreen();
}

function updateScreen() {
    const screen = document.getElementById('result');
    screen.textContent = currentInput;
}

updateScreen();
