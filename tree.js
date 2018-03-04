function main() {
    
var stuff = ["0", "Gen 1", 0]

var mydata = JSON.parse(data);
var mydata1 = JSON.parse(data1);
var mydata2 = JSON.parse(data2); //{"id": mydata1[0].id, "label": mydata1[0].label, "level": mydata1[0].level},

    
    var graph = {
        nodes: new vis.DataSet([
            {'id': '0', 'label': 'Male 0', 'level': 0},{'id': '1', 'label': 'Female 0', 'level': 0},{'id': '2', 'label': 'Male 1', 'level': 0},{'id': '3', 'label': 'Female 1', 'level': 0},{'id': '4', 'label': 'Male 2', 'level': 0},{'id': '5', 'label': 'Female 2', 'level': 0},{'id': '6', 'label': 'Male 3', 'level': 0},{'id': '7', 'label': 'Female 3', 'level': 0},{'id': '8', 'label': 'Male 4', 'level': 0},{'id': '9', 'label': 'Female 4', 'level': 0}, 
{'id': '10', 'label': 'Male 1 + Female 1', 'level': 1},{'id': '11', 'label': 'Male 0 + Female 0', 'level': 1},{'id': '12', 'label': 'Male 1 + Female 1', 'level': 1},{'id': '13', 'label': 'Male 0 + Female 0', 'level': 1},{'id': '14', 'label': 'Male 3 + Female 3', 'level': 1},{'id': '15', 'label': 'Male 2 + Female 2', 'level': 1},{'id': '16', 'label': 'Male 3 + Female 3', 'level': 1},{'id': '17', 'label': 'Male 2 + Female 2', 'level': 1},{'id': '18', 'label': 'Male 4 + Female 4', 'level': 1}, 
{'id': '20', 'label': 'Male 1 + Female 1 + Male 0 + Female 0', 'level': 2},{'id': '21', 'label': 'Male 1 + Female 1 + Male 0 + Female 0', 'level': 2},{'id': '22', 'label': 'Male 1 + Female 1 + Male 0 + Female 0', 'level': 2},{'id': '23', 'label': 'Male 1 + Female 1 + Male 0 + Female 0', 'level': 2},{'id': '24', 'label': 'Male 3 + Female 3 + Male 2 + Female 2', 'level': 2},{'id': '25', 'label': 'Male 3 + Female 3 + Male 2 + Female 2', 'level': 2},{'id': '26', 'label': 'Male 3 + Female 3 + Male 2 + Female 2', 'level': 2}, 


        ]),
        edges: new vis.DataSet([
            {'from': '2', 'to': '10'},{'from': '3', 'to': '10'},{'from': '0', 'to': '11'},{'from': '1', 'to': '11'},{'from': '2', 'to': '12'},{'from': '3', 'to': '12'},{'from': '0', 'to': '13'},{'from': '1', 'to': '13'},{'from': '6', 'to': '14'},{'from': '7', 'to': '14'},{'from': '4', 'to': '15'},{'from': '5', 'to': '15'},{'from': '6', 'to': '16'},{'from': '7', 'to': '16'},{'from': '4', 'to': '17'},{'from': '5', 'to': '17'},{'from': '8', 'to': '18'},{'from': '9', 'to': '18'}, 
{'from': '12', 'to': '20'},{'from': '13', 'to': '20'},{'from': '12', 'to': '21'},{'from': '13', 'to': '21'},{'from': '12', 'to': '22'},{'from': '13', 'to': '22'},{'from': '12', 'to': '23'},{'from': '13', 'to': '23'},{'from': '16', 'to': '24'},{'from': '17', 'to': '24'},{'from': '16', 'to': '25'},{'from': '17', 'to': '25'},{'from': '16', 'to': '26'},{'from': '17', 'to': '26'}, 

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