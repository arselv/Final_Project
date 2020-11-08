d3.select("#plot1").text("HELLLLOOO");

d3.csv("static/data/graph_1.csv").then((data) => {
  // console.log(data);
  let x = data.map((d) => +d[""]);
  let y = data.map((d) => +d.opening_price);

  var trace1 = {
    x: x,
    y: y,
    type: "scatter",
  };

  Plotly.newPlot("plot1", [trace1]);
});
