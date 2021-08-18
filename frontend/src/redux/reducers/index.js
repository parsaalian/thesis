import { combineReducers } from 'redux';
import accountReducer from './account';
import questionReducer from './question';

export default combineReducers({
    account: accountReducer,
    question: questionReducer,
});