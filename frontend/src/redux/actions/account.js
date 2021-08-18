import { postLoginAPI, postRefreshTokenAPI } from '../../services/account';

export const SET_TOKENS = 'SET_TOKENS';
export const SET_ACCESS_TOKEN = 'SET_ACCESS_TOKEN';

export function setTokensAction({ access, refresh }) {
    return {
        type: SET_TOKENS,
        payload: {
            access,
            refresh,
        },
    }
}

export function setAccessTokenAction({ access }) {
    return {
        type: SET_ACCESS_TOKEN,
        payload: {
            access,
        }
    }
}

export function loginAction({ username, password }) {
    return (dispatch, _) => {
        postLoginAPI({ username, password }).then(
            (response) => {
                const { data } = response;
                const { access, refresh } = data;
                dispatch(setTokensAction({ access, refresh }));
            }
        )
    }
}

export function refreshAction() {
    return (dispatch, getState) => {
        const { refresh } = getState().account;
        postRefreshTokenAPI({ refresh }).then(
            (response) => {
                const { data } = response;
                const { access } = data;
                dispatch(setAccessTokenAction({ access }));
            }
        )
    }
}