
// var button = d3.select('select option:checked').text()

var selectElement = d3.select("select")

selectElement
  .on("change", function(event) {

 

    var sel = document.getElementById('select');
    selectValue = sel.options[sel.selectedIndex].value.toUpperCase();

    d3.select("#stock-value").text("Stock: "+ selectValue + " ...  calculating ....");

    // console.log(selectValue);
    drawGraphs(selectValue);
  });

const drawGraphs = tickerStr => {
  // Model graph
  d3.json("api/"+ tickerStr).then((data) => {
    // console.log(data);

    d3.select("#plot1").style("height","400px");
    d3.select("#plot2").style("height","400px");

    let x = Object.keys(data.closing_prices).map(d => +d);
    let y = Object.values(data.closing_prices);

    var trace_actual = {
      x: x,
      y: y,
      type: "scatter",
      name: "Closing Prices",
    };

    y2 = Object.values(data.predicted_prices);
    var index = 0;
    y2.forEach((y2_value) => {
      
      if (!y2_value) {
        index++;
      } 
    });

    x2 = x.slice(index);
    y2 = y2.slice(index);

    var trace_predictions = {
      x: x2,
      y: y2,
      type: "scatter",
      name: "Predicted Prices",
    };

    let layout = {
      title: "LSTM Neural Network Model Training and Fitting for " + tickerStr,
    };

    let plot_data = [trace_actual, trace_predictions];

    

    Plotly.newPlot("plot1", plot_data, layout);
  
    // END OF 1st GRAPH

    trace_actual = {
      x: x.slice(index),
      y: y.slice(index),
      type: "scatter",
      name: "Closing Prices",
    };

    layout = {
      title: "Model Predictions versus Actual Closing Prices for " + tickerStr,
    };

    plot_data = [trace_actual, trace_predictions];

    Plotly.newPlot("plot2", plot_data, layout);

    d3.select('#modelLoss')
      .attr("src","static/images/models/" + tickerStr + "_loss.png")

    d3.select("#stock-value").text("Stock: "+ tickerStr + " ...  finished predicting.");

    d3.select("#card-text").text("Line graph above is the closing prices used to train the model and the predicted prices.  Below is a zoomed-in version of the actual versus predicted prices on the testing data.  Finally, the last graph is the loss over epochs while the neural network was training.")
  });  // END OF d3.json

  
}  





// var canvas = d3.select("#plot0");

// var margin = {top: 20, right: 20, bottom: 30, left: 50},
//   width = canvas.node().getBoundingClientRect().width - margin.left - margin.right,
//   height = canvas.node().getBoundingClientRect().height - margin.top - margin.bottom;

// var svg = d3.select("#plot0")
//   .append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform","translate(" + margin.left + "," + margin.top + ")");

// d3.json("api/TSLA").then(data => {

//   var x_values = Object.keys(data.closing_prices).map(d=>+d)
//   var closing_prices = Object.values(data.closing_prices)

//   console.log(data.closing_prices)

//   // Add x-axis
//   var x = d3.scaleLinear()
//     .domain(d3.extent(x_values))
//     .range([0,width]);
//   svg.append("g")
//     .attr("transform","translate(0," + height + ")")
//     .call(d3.axisBottom(x));

//   // Add y-axis
//   var y = d3.scaleLinear()
//     .domain([0,d3.max(closing_prices)])
//     .range([height, 0])
//   svg.append("g")
//     .call(d3.axisLeft(y));

//   // Add the line
//   svg.append("path")
//     .datum(data.closing_prices)
//     .attr("fill","none")
//     .attr("stroke","steelblue")
//     .attr("stroke-width", 1.5)
    

// }).catch(err => console.log(err))