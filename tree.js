function main() {
    
var stuff = ["0", "Gen 1", 0]

var mydata = JSON.parse(data);
var mydata1 = JSON.parse(data1);
var mydata2 = JSON.parse(data2);
    
    var graph = {
        nodes: new vis.DataSet([
          {"id": mydata[0].id, "label": mydata[0].label, "level": mydata[0].level}, 
          
          {"id": mydata1[0].id, "label": mydata1[0].label, "level": mydata1[0].level},
          {"id": mydata2[0].id, "label": mydata2[0].label, "level": mydata2[0].level},

        ]),
        edges: new vis.DataSet([
          {"from": "0", "to": "0.1"},
          {"from": "1", "to": "0.1"},
        ])
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
        color: 'lightgray'
      },
      layout: {
        hierarchical: {
          direction: 'UD',
          nodeSpacing: 150
        }
      },
      interaction: {dragNodes :false},
      physics:false
      };
    var network = new vis.Network(document.getElementById("network"), graph, options);
}