// d3 scatter plot
var width = 700;
var height = 400;

//var max = d3.select('#maximum').node().value;
var max = 5;
var margin = {
    top: 20,
    left: 30,
    right: 60,
    bottom: 30
};

var svg = d3.select("#vis")
    .append("svg")
        .attr('width', width)
        .attr('height', height)
    .append("g")
        .attr("transform", "translate(" + margin.top + "," + margin.left + ")");

width = width - margin.left - margin.right;
height = height - margin.top - margin.bottom;

var xscale = d3.scale.linear()
                .domain([0, max])
                .range([0, width]);

var yscale = d3.scale.linear()
                .domain([0, max])
                .range([height, 0]);

var xaxis = d3.svg.axis()
.scale(xscale)
.orient('bottom');

var yaxis = d3.svg.axis()
.scale(yscale)
.orient('left');

svg.append('g')
    .attr('transform', 'translate(0, ' + (height) + ')')
    .attr('class', 'x axis');

svg.append('g')
    .attr('class', 'y axis');

function update() {
    var t = d3.transition()
        .duration(100);
        //.ease(d3.easeQuadOut);

    //var max = d3.select('#maximum').node().value;
    var max = 5;

    var exampleData = data;

    maxX = d3.max(exampleData, function(d){ return d.x; });
    maxY = d3.max(exampleData, function(d){ return d.y });

    xscale.domain([0, maxX]);
    yscale.domain([0, maxY]);

    var dots = svg.selectAll(".dot")
       .data(exampleData);

    dots
        .enter()
            .append('circle')
            .attr('r', 3)
            .attr('fill', 'red')
            .attr('stroke', 'black')
            .attr('class','dot')
            .attr('cy', height)
            .attr('cx', 0)
        .merge(dots)
            .transition(t)
            .attr("cy", function(d, i){ return yscale(d.y); })
            .attr("cx", function(d, i){ return xscale(d.x); })

    dots
        .exit()
        .remove();

    var labels = svg.selectAll('.label')
        .data(exampleData);

    labels
        .enter()
            .append('text')
            .attr('class', 'label')
            .attr('x', 0)
            .attr('y', height)
        .merge(labels)
            .transition(t)
            .attr('x', function(d) {
                return xscale(d.x) + 2;
            })
            .attr('y', function(d){
                return yscale(d.y) - 2;
            })
            .text(function(d){
                return d.x + ", " + d.y;
            })

    labels
        .exit()
        .remove();
        
    svg.select('.x.axis')
        .transition(t)
        .call(xaxis);
    svg.select('.y.axis')
        .transition(t)
        .call(yaxis);
}

update();
