import React, { Component } from "react";
import FilterTableComponent from './filterTable';
 
class TrackSections extends Component {
  render() {
    return (
      <div>
        <h2>Track Section Times</h2>
        <p>This page contains track section times for each car.</p>
        <div class="table-responsive">
            <FilterTableComponent />
        </div>
      </div>
    );
  }
}
 
export default TrackSections;