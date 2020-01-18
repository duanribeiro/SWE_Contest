import { createStore } from 'redux'

const INITIAL_STATE =  {
    'life': 3,
    'time': Date.now() + 5000
}

function courses(state=INITIAL_STATE, action) {

    switch (action.type) {
        case 'ADD_LIFE':
            return {...state, life : state.life + Number(action.size)}
        case 'REMOVE_LIFE':
            return {...state, life : state.life - Number(action.size)}
        case 'ADD_TIME':
            return {...state, time : [...state.data.time, ...state.data.time + Number(action.size)]}
        case 'REMOVE_TIME':
            return {...state, time : [...state.data.time, ...state.data.time - Number(action.size)]}
        default:
            return state
    }
}

const store = createStore(courses)

export default store