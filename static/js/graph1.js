d3.select("#plot1").text("HELLLLOOO");

// Model graph
d3.csv("static/data/graph_1.csv").then((data) => {
  // console.log(data);
  let x = data.map((d) => +d[""]);
  let y = data.map((d) => +d.opening_price);

  var trace_actual = {
    x: x,
    y: y,
    type: "scatter",
  };

  var trace_predictions = {};

  Plotly.newPlot("plot1", [trace_actual]);
});

// Forecasting Graph
