import { combineReducers } from 'redux';
import questionReducer from './question';

export default combineReducers({
    question: questionReducer,
});