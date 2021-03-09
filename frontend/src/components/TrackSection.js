import React, { Component } from "react";
import axios from "axios";
import Table from './filterTable';
 

function TrackSectionTableComponent(props) {
  const columns = React.useMemo(
      () => [
          {
              Header: 'Vehicle',
              columns: [
                  {
                      Header: 'Model',
                      accessor: 'car_model',
                  },
                  {
                      Header: 'Version',
                      accessor: 'car_version'
                  },
              ],
          },
          {
              Header: 'Section Times',
              columns: [
                  {
                      Header: 'Starting Point',
                      accessor: 'start_point'
                  },
                  {
                      Header: 'Ending Point',
                      accessor: 'end_point'
                  },
                  {
                      Header: 'Status',
                      accessor: 'status'
                  },
                  {
                      Header: 'Duration (seconds)',
                      accessor: 'duration'
                  },
              ],
          },
      ],
      []
  )

  return (
      <Table columns={columns} data={props.data}/>
  )
}

class TrackSections extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      pagination: {
        nextPage: null,
        prevPage: null,
        currentPage: 1,
        totalPageCount: 1,
      },
      data: []
    }
  };

  async componentDidMount() {
    await this.fetchTrackSectionDataAsync("http://127.0.0.1:5000/api/get_section_time");
  }

  async goToPage(url) {
    this.setState({...this.state, loading: true});
      const response = await axios.get("http://127.0.0.1:5000"+url);
      console.log(response);
      this.setState({
        loading: false,
        nextPage: response.data._links.next,
        previousPage: response.data._links.prev,
        pagination: {
          nextPage: response.data._links.next,
          prevPage: response.data._links.prev,
          currentPage: response.data._meta.page,
          totalPageCount: response.data._meta.total_pages,
        },
        data: response.data.items,
      });
  }

  async fetchTrackSectionDataAsync(url) {
    try {
      this.setState({...this.state, loading: true});
      const response = await axios.get(url);
      console.log(response);
      this.setState({
        loading: false,
        nextPage: response.data._links.next,
        previousPage: response.data._links.prev,
        pagination: {
          nextPage: response.data._links.next,
          prevPage: response.data._links.prev,
          currentPage: response.data._meta.page,
          totalPageCount: response.data._meta.total_pages,
        },
        data: response.data.items,
      });
    } catch(e) {
      console.log(e);
      this.setState({
        loading: false,
        pagination: {
          nextPage: null,
          prevPage: null,
          currentPage: 1,
          totalPageCount: 1,
        },
        data: [],
      });
    }
  }

  render() {
    if (this.state.loading ) {
      return (<div>loading...</div>);
    }

    return (
      <div>
        <h2>Track Section Times</h2>
        <p>This page contains track section times for each car.</p>
        <div class="table-responsive">
            <TrackSectionTableComponent data={this.state.data}/>
        </div>
        <div className="pagination">
            <button onClick={() => this.goToPage(this.state.pagination.prevPage)} disabled={!this.state.pagination.prevPage}>
            {'<'}
            </button>{' '}
            <button onClick={() => this.goToPage(this.state.pagination.nextPage)} disabled={!this.state.pagination.nextPage}>
            {'>'}
            </button>{' '}
            <span>
            Page{' '}
            <strong>
                {this.state.pagination.currentPage} of {this.state.pagination.totalPageCount}
            </strong>{' '}
            </span>
        </div>
      </div>
    );
  }
}
 
export default TrackSections;