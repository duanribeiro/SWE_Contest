import { createStore } from 'redux'

const INITIAL_STATE =  {
    'data': {
      'life': 3
    }
}
function courses(state=INITIAL_STATE, action) {
    switch (action.type) {
        case 'ADD_LIFE':
            return {...state, data : [...state.data.life, ...state.data.life + 1]}
        default:
            return state
    }
}

const store = createStore(courses)

export default store