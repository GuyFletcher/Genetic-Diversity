function main() {

//var nodes = JSON.parse(nodes);
    //same seed/set of people, run it 10 times, see how often different occurnces happen, how often diesease/sterile

    var graph = {
        nodes: new vis.DataSet(nodeArray),
        edges: new vis.DataSet(connections)
    };
    
    var options = {
      nodes: {
        borderWidth: 1,
        borderWidthSelected: 1,
        shape: "box",
        color: {
          border: 'lightgray',
          background: 'white',
          highlight: {
            border: 'lightgray',
            background: 'lightblue'
          },
          hover: {
            border: 'lightgray',
            background: 'lightblue'
          }
        }
      },
      edges: {
        smooth: {
          type: 'cubicBezier',
          forceDirection: 'vertical',
          roundness: 1
        },
        length: 95,
        color: 'lightgray'
      },
      layout: {
        hierarchical: {
          direction: 'UD',
          nodeSpacing: 100,
          levelSeparation: 250, 
          sortMethod: 'hubsize',
          edgeMinimization : false
        },
        improvedLayout: true
      },
      interaction: {dragNodes :false},
      physics:false,
      
      };
    var network = new vis.Network(document.getElementById("network"), graph, options);
    
    for(i=0;i<nodeArray.length;i++) 
    {
        blue_color = 255 - (Math.floor((nodeArray[i].sim/100)*255))
        red_color = (Math.floor((nodeArray[i].sim/100)*255))
        green_color = (Math.floor((nodeArray[i].sim/100)*255))
        if(blue_color <= 0)
            blue_color = 255
        if(red_color <= 0)
            red_color = 255
        if(green_color <= 0)
            green_color = 255
        
        color_string = "rgba(255," + green_color + "," + red_color +", 255)"
        //color_string = "rgba(" + blue_color + "," + green_color + "," + red_color +", 255)"
        //console.log(color_string)
        var newNode = graph.nodes.get(nodeArray[i].id);
        newNode.color = {
          border: '#000000',
          background: color_string
        }
        graph.nodes.update(newNode);
        graph.nodes.update(newNode);
    }
    
    network.on( 'click', function(properties) {
        console.log(genes.length);
        for(i=0;i<nodeArray.length;i++)
        {
            if (nodeArray[i].id == properties['nodes'])
            {
                document.getElementById('genes').innerHTML = '<h2>Click event:</h2>' + genes[i].genes;//get node index
                console.log('Done');
            }
        }
    
});
}