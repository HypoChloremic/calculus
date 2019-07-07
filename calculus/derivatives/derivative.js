
let x = [];
let y = [];

function firstForm(x){
    // x^5 - 10x^4 + 25^3
    return mu = (x**5 - (10 * (x**4)) + (25*(x**3)))

}


function mainLoop(arraySize=100, multiplier=1, formula=firstForm){
    let min = - arraySize / 2;
    let max =   arraySize / 2

    for (let i=min; i<max; i++){
      
      x.push((i*multiplier))
      y.push(formula(i))
    }
    return x, y
}

x,y = mainLoop(arraySize=100, multiplier=1)



// varname = {} creates an object
// that we then use by passing as an argument
// to the newPlot function of plotly
let trace1 = {
  x: x,
  y: y,
  type: "scatter",

};

let data = [trace1];

Plotly.newPlot('myDiv', data, {}, {showSendToCloud: true});