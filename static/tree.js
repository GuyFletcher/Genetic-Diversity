var test = require('tape');

test("color value test", function(assert) {
    assert.plan(2);
    assert.equal(returnColor(100), "rgba(255,255,255,255)", "Expect 255");
    assert.equal(returnColor(50), "rgba(127,127,255,255)", "Expect 127");
    assert.end();
});

function returnColor(simVal) {
    colorVal = (Math.floor((simVal/100)*255));
    if(colorVal <= 0)
        colorVal = 255;
    
    color_string = "rgba(" + colorVal + "," + colorVal + ",255,255)";
    return color_string
}

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
        if(nodeArray[i].disease == "True")
        {
            color_string = "rgba(255,0,0,255)"
        }
        else {
            color_string = returnColor(nodeArray[i].sim)
        }
        
        var newNode = graph.nodes.get(nodeArray[i].id);
        newNode.color = {
          border: '#000000',
          background: color_string
        }
        graph.nodes.update(newNode);
        graph.nodes.update(newNode);
    }
    
    network.on( 'click', function(properties) {
        
        for(i=0;i<nodeArray.length;i++)
        {
            if (nodeArray[i].id == properties['nodes'])
            {
                console.log(nodeArray[i].disease);
                document.getElementById('genes').innerHTML = '<h2>Click event:</h2>' + genes[i].genes;//get node index
                console.log('Done');
            }
        }
    
});
}