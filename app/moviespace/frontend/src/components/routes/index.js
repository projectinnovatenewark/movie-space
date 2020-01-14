import * as React from 'react';

import { Redirect, Route, Router, Switch } from 'react-router';
import history from './history';
import Welcome from '../welcome/Welcome';
import Login from '../welcome/Signin';
import Signup from '../welcome/Signup';

function Routes() {
  return (
    <Router history={history}>
      <Switch>
        <Route exact path="/welcome" component={Welcome} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/signup" component={Signup} />
        {/* <Route exact path="/dashboard" component={Dashboard} /> */}
        {/* <Route exact path="/movies" component={Movies} /> */}
        <Redirect from="/" to="/welcome" />
      </Switch>
    </Router>
  );
};

export default Routes;
