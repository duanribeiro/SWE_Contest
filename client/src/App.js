import React from 'react';
import { Provider } from 'react-redux'
import store from './store'
import CourseList  from './components/CourseList'

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <CourseList/>
      </div>
    </Provider>

  );
}

export default App
