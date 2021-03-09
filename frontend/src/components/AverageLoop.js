import React, { Component } from "react";
import Table from './filterTable';

function AverageLoopTableComponent(props) {
  const columns = React.useMemo(
      () => [
          {
              Header: 'Vehicle',
              columns: [
                  {
                      Header: 'Model',
                      accessor: 'carModel',
                  },
                  {
                      Header: 'Version',
                      accessor: 'carVersion'
                  },
              ],
          },
          {
              Header: 'Stats',
              columns: [
                  {
                      Header: 'Average Loop Time',
                      accessor: 'averageTime'
                  },
                  {
                      Header: 'Attempts',
                      accessor: 'attempts'
                  },
              ],
          },
      ],
      []
  )

  return (
      <Table columns={columns} data={props.data} />
  )
}

class AverageLoops extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [
        {
          "carVersion": "C1_V5",
          "carModel": "C1",
          "averageTime": '1hr 3sec',
          "attempts": '2',
        },
        {
          "carVersion": "C2_V7",
          "carModel": "C1",
          "averageTime": '1hr 45sec',
          "attempts": '5',
        },
        {
          "carVersion": "C2_V7",
          "carModel": "C1",
          "averageTime": '1hr 45sec',
          "attempts": '5',
        },
        {
          "carVersion": "C2_V7",
          "carModel": "C1",
          "averageTime": '1hr 45sec',
          "attempts": '5',
        },
    ]
    }
  };

  render() {
    return (
      <div>
        <h2>Average Loop Times</h2>
        <p>The following table shows the average loop times for each car across the F1 track</p>
        <div className="table-responsive">
            <AverageLoopTableComponent data={this.state.data}/>
        </div>
      </div>
    );
  }
}
 
export default AverageLoops;