// App.js
// App.js
import React from 'react';
import { Route, NavLink, HashRouter} from "react-router-dom";
import Home from "./components/Home";
import AverageLoops from "./components/AverageLoop";
import TrackSections from "./components/TrackSection";
import './App.css';

function App() {

  return (
    <div className="App">
    <HashRouter>
        <h1>F1 Race Data</h1>
            <ul className="header">
                <li><NavLink to="/">Home</NavLink></li>
                <li><NavLink to="/averageLoops">Average Loop Times</NavLink></li>
                <li><NavLink to="/trackSections">Track Section Times</NavLink></li>
            </ul>
        <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/averageLoops" component={AverageLoops}/>
            <Route path="/trackSections" component={TrackSections}/>
        </div>
    </HashRouter>
    </div>
  );
}

export default App;