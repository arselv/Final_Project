d3.csv("static/data/graph2_actual.csv").then((actual) => {
  d3.csv("static/data/graph2_predictions.csv").then((predictions) => {
    let x1 = actual.map((d) => d.Date);
    let y1 = actual.map((d) => d.Close);

    let x2 = predictions.map((d) => d[""]);
    let y2 = predictions.map((d) => d.Close);

    var trace_actual = {
      x: x1,
      y: y1,
      type: "scatter",
      name: "Opening Prices",
    };

    var trace_predictions = {
      x: x2,
      y: y2,
      type: "scatter",
      name: "Predicted Prices",
    };

    let layout = {
      title: "Forecasting the Next 7 days",
    };

    let plot_data = [trace_actual, trace_predictions];

    Plotly.newPlot("plot2", plot_data, layout);
  });
});
