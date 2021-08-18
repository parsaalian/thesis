import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import makeStore from './redux/store';
import routes from './pages';

function App() {
  const store = makeStore({});

  return (
    <Provider store={store}>
      <PersistGate persistor={store.__PERSISTOR}>
        <Router>
          <Switch>
            {routes.map(({ path, component: RouteComponent }) => {
              return (
                <Route path={path} key={path} exact>
                  <RouteComponent />
                </Route>
              );
            })}
          </Switch>
        </Router>
      </PersistGate>
    </Provider>
  );
}

export default App;