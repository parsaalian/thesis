import produce from 'immer';
import { SET_TOKENS, SET_ACCESS_TOKEN } from '../actions/account';
import initialState from '../initialState';

function setTokensReducer(state = initialState.account, action) {
    return produce(state, (draft) => {
        const { access, refresh } = action.payload;
        draft.access = access;
        draft.refresh = refresh;
        return draft;
    });
}

function setAccessTokenReducer(state = initialState.account, action) {
    return produce(state, (draft) => {
        const { access } = action.payload;
        draft.access = access;
        return draft;
    });
}

function accountReducer(state = initialState.account, action) {
    switch (action.type) {
        case SET_TOKENS:
            return setTokensReducer(state, action);
        case SET_ACCESS_TOKEN:
            return setAccessTokenReducer(state, action);
        default:
            return state;
    }
}

export default accountReducer;