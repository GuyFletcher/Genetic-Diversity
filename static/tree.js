function main() {
    
var stuff = ["0", "Gen 1", 0];

//var nodes = JSON.parse(nodes);

//thing = [{'id': '0', 'label': 'Male Gen 0', 'level': 0},{'id': '1', 'label': 'Female Gen 0', 'level': 0},{'id': '2', 'label': 'Male Gen 0', 'level': 0},{'id': '3', 'label': 'Female Gen 0', 'level': 0},{'id': '4', 'label': 'Male Gen 0', 'level': 0},{'id': '5', 'label': 'Female Gen 0', 'level': 0},{'id': '6', 'label': 'Male Gen 0', 'level': 0},{'id': '7', 'label': 'Female Gen 0', 'level': 0},{'id': '8', 'label': 'Male Gen 0', 'level': 0},{'id': '9', 'label': 'Female Gen 0', 'level': 0},{'id': '10', 'label': 'Male Gen 1', 'level': 1},{'id': '11', 'label': 'Female Gen 1', 'level': 1},{'id': '12', 'label': 'Male Gen 1', 'level': 1},{'id': '13', 'label': 'Female Gen 1', 'level': 1},{'id': '14', 'label': 'Male Gen 1', 'level': 1},{'id': '15', 'label': 'Female Gen 1', 'level': 1},{'id': '16', 'label': 'Male Gen 1', 'level': 1},{'id': '17', 'label': 'Female Gen 1', 'level': 1},{'id': '18', 'label': 'Male Gen 1', 'level': 1},{'id': '19', 'label': 'Female Gen 1', 'level': 1},{'id': '20', 'label': 'Male Gen 2', 'level': 2},{'id': '21', 'label': 'Female Gen 2', 'level': 2},{'id': '22', 'label': 'Male Gen 2', 'level': 2},{'id': '23', 'label': 'Female Gen 2', 'level': 2},{'id': '24', 'label': 'Male Gen 2', 'level': 2},{'id': '25', 'label': 'Female Gen 2', 'level': 2},{'id': '26', 'label': 'Male Gen 2', 'level': 2},{'id': '27', 'label': 'Female Gen 2', 'level': 2},{'id': '28', 'label': 'Male Gen 2', 'level': 2},{'id': '29', 'label': 'Male Gen 2', 'level': 2},{'id': '30', 'label': 'Male Gen 3', 'level': 3},{'id': '31', 'label': 'Female Gen 3', 'level': 3},{'id': '32', 'label': 'Male Gen 3', 'level': 3},{'id': '33', 'label': 'Female Gen 3', 'level': 3},{'id': '34', 'label': 'Male Gen 3', 'level': 3},{'id': '35', 'label': 'Female Gen 3', 'level': 3},{'id': '36', 'label': 'Male Gen 3', 'level': 3},{'id': '37', 'label': 'Male Gen 3', 'level': 3},{'id': '40', 'label': 'Male Gen 4', 'level': 4},{'id': '41', 'label': 'Female Gen 4', 'level': 4},{'id': '42', 'label': 'Male Gen 4', 'level': 4},{'id': '43', 'label': 'Female Gen 4', 'level': 4},{'id': '44', 'label': 'Male Gen 4', 'level': 4},{'id': '45', 'label': 'Male Gen 4', 'level': 4}]

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
          sortMethod: 'hubSize',
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
        color = (Math.floor((nodeArray[i].sim/100)*255))
        
        if(color == 0)
            color = 255
        
        color_string = "rgba(255,255,"+ color +", 255)"
        console.log(color_string)
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