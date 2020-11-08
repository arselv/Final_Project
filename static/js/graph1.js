// Model graph
d3.csv("static/data/graph_1.csv").then((data) => {
  // console.log(data);
  let x = data.map((d) => +d.Index);
  let y = data.map((d) => +d.opening_price);

  var trace_actual = {
    x: x,
    y: y,
    type: "scatter",
    name: "Opening Prices",
  };

  x2 = [];
  y2 = [];
  data.forEach((row) => {
    if (row.predicted_prices > 0) {
      x2.push(row.Index);
      y2.push(row.predicted_prices);
    }
  });

  var trace_predictions = {
    x: x2,
    y: y2,
    type: "scatter",
    name: "Predicted Prices",
  };

  let layout = {
    title: "LSTM Neural Network Model Training and Fitting",
  };

  let plot_data = [trace_actual, trace_predictions];

  Plotly.newPlot("plot1", plot_data, layout);
});


