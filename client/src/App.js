import React from 'react';
import { Provider } from 'react-redux'
import store from './store'
import MainWindow  from './components/MainWindow'
import "./App.scss";

function App() {
  return (
      <Provider store={store}>
        <div className="App">
          <MainWindow/>
        </div>
      </Provider>

  );
}

export default App
