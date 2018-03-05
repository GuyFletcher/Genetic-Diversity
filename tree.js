function main() {
    
var stuff = ["0", "Gen 1", 0]

var mydata = JSON.parse(data);
var mydata1 = JSON.parse(data1);
var mydata2 = JSON.parse(data2); //{"id": mydata1[0].id, "label": mydata1[0].label, "level": mydata1[0].level},

    
    var graph = {
        nodes: new vis.DataSet([
            {'id': '0', 'label': 'Male Gen 0', 'level': 0},{'id': '1', 'label': 'Female Gen 0', 'level': 0},{'id': '2', 'label': 'Male Gen 0', 'level': 0},{'id': '3', 'label': 'Female Gen 0', 'level': 0},{'id': '4', 'label': 'Male Gen 0', 'level': 0},{'id': '5', 'label': 'Female Gen 0', 'level': 0},{'id': '6', 'label': 'Male Gen 0', 'level': 0},{'id': '7', 'label': 'Female Gen 0', 'level': 0},{'id': '8', 'label': 'Male Gen 0', 'level': 0},{'id': '9', 'label': 'Female Gen 0', 'level': 0}, 
{'id': '10', 'label': 'Male Gen 1', 'level': 1},{'id': '11', 'label': 'Female Gen 1', 'level': 1},{'id': '12', 'label': 'Male Gen 1', 'level': 1},{'id': '13', 'label': 'Female Gen 1', 'level': 1},{'id': '14', 'label': 'Male Gen 1', 'level': 1},{'id': '15', 'label': 'Female Gen 1', 'level': 1},{'id': '16', 'label': 'Male Gen 1', 'level': 1},{'id': '17', 'label': 'Male Gen 1', 'level': 1},{'id': '18', 'label': 'Male Gen 1', 'level': 1},{'id': '19', 'label': 'Male Gen 1', 'level': 1}, 
{'id': '20', 'label': 'Male Gen 2', 'level': 2},{'id': '21', 'label': 'Female Gen 2', 'level': 2},{'id': '22', 'label': 'Male Gen 2', 'level': 2},{'id': '23', 'label': 'Male Gen 2', 'level': 2},{'id': '24', 'label': 'Male Gen 2', 'level': 2},{'id': '25', 'label': 'Male Gen 2', 'level': 2}, 
{'id': '30', 'label': 'Male Gen 3', 'level': 3},{'id': '31', 'label': 'Female Gen 3', 'level': 3}, 
{'id': '40', 'label': 'Male Gen 4', 'level': 4},{'id': '41', 'label': 'Male Gen 4', 'level': 4},
        ]),
        edges: new vis.DataSet([
            {'from': '0', 'to': '10'},{'from': '1', 'to': '10'},{'from': '0', 'to': '11'},{'from': '1', 'to': '11'},{'from': '2', 'to': '12'},{'from': '3', 'to': '12'},{'from': '4', 'to': '13'},{'from': '5', 'to': '13'},{'from': '2', 'to': '14'},{'from': '3', 'to': '14'},{'from': '8', 'to': '15'},{'from': '9', 'to': '15'},{'from': '4', 'to': '16'},{'from': '5', 'to': '16'},{'from': '6', 'to': '17'},{'from': '7', 'to': '17'},{'from': '6', 'to': '18'},{'from': '7', 'to': '18'},{'from': '8', 'to': '19'},{'from': '9', 'to': '19'}, 
{'from': '10', 'to': '20'},{'from': '11', 'to': '20'},{'from': '12', 'to': '21'},{'from': '13', 'to': '21'},{'from': '10', 'to': '22'},{'from': '11', 'to': '22'},{'from': '12', 'to': '23'},{'from': '13', 'to': '23'},{'from': '14', 'to': '24'},{'from': '15', 'to': '24'},{'from': '14', 'to': '25'},{'from': '15', 'to': '25'}, 
{'from': '20', 'to': '30'},{'from': '21', 'to': '30'},{'from': '20', 'to': '31'},{'from': '21', 'to': '31'}, 
{'from': '30', 'to': '40'},{'from': '31', 'to': '40'},{'from': '30', 'to': '41'},{'from': '31', 'to': '41'}, 

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