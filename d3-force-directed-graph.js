// URL: https://beta.observablehq.com/@tx19980520/d3-force-directed-graph
// Title: D3 Force-Directed Graph
// Author: ty0207 (@tx19980520)
// Version: 92
// Runtime version: 1

const m0 = {
  id: "a7c4b2e7a225e5f8@92",
  variables: [
    {
      inputs: ["md"],
      value: (function(md){return(
md`# D3 Bilibili Force-Directed Graph

This graph is a demo of the similarity of the bilibili users(from real raw data).the more animes you both collect, the more similar you are `
)})
    },
    {
      name: "chart",
      inputs: ["data","d3","width","height","DOM","color","drag"],
      value: (function(data,d3,width,height,DOM,color,drag)
{
  const links = data.links.map(d => Object.create(d));
  const nodes = data.nodes.map(d => Object.create(d));
  
  const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id))
      .force("charge", d3.forceManyBody())
      .force("center", d3.forceCenter(width / 2, height / 2))
      .on("tick", ticked);
  
  const svg = d3.select(DOM.svg(width, height));
  
  const link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", d => Math.sqrt(d.value));
  
  const node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
    .selectAll("circle")
    .data(nodes)
    .enter().append("circle")
      .attr("r", 5)
      .attr("fill", color)
      .call(drag(simulation));

  node.append("title")
      .text(d => d.id);
  
  function ticked() {
    link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);
    
    node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
  }
  
  return svg.node();
}
)
    },
    {
      name: "data",
      value: (async function(){return(
(await fetch("http://127.0.0.1:80/study.json")).json()
)})
    },
    {
      name: "height",
      value: (function(){return(
600
)})
    },
    {
      name: "color",
      inputs: ["d3"],
      value: (function(d3)
{
  const scale = d3.scaleOrdinal(d3.schemeCategory10);
  return d => scale(d.group);
}
)
    },
    {
      name: "drag",
      inputs: ["d3"],
      value: (function(d3){return(
simulation => {
  
  function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }
  
  function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
  }
  
  function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
  
  return d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended);
}
)})
    },
    {
      name: "d3",
      inputs: ["require"],
      value: (function(require){return(
require("https://d3js.org/d3.v5.min.js")
)})
    }
  ]
};

const notebook = {
  id: "a7c4b2e7a225e5f8@92",
  modules: [m0]
};

export default notebook;
