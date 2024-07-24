// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Recommendations from './pages/Recommendations';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/profile" component={Profile} />
          <Route path="/recommendations" component={Recommendations} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;

// components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/profile">Profile</Link></li>
          <li><Link to="/recommendations">Recommendations</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;

// pages/Home.js
import React from 'react';

function Home() {
  return (
    <div>
      <h1>Welcome to User Experience Center</h1>
      <p>Explore our personalized recommendations and manage your profile.</p>
    </div>
  );
}

export default Home;
