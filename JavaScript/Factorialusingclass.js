class Factorial {
    constructor(n) {
      this.n = n;
    }
  
    calculate() {
      if (this.n < 0) {
        throw new Error('Factorial is not defined for negative numbers');
      }
      return this._factorial(this.n);
    }
  
    _factorial(num) {
      if (num ==0 || num==1) 
          return 1;
      return num * this._factorial(num - 1);
    }
  }
  
  // Sample input
  const number = 5;
  const factorialObj = new Factorial(number);
  console.log(`Factorial of ${number} is: ${factorialObj.calculate()}`);
  
