import axios from 'axios';
import BASE_ADDR from '.';

const LOGIN = `${BASE_ADDR}/accounts/login`;
const REFRESH = `${BASE_ADDR}/accounts/refresh`;

export function postLoginAPI({ username, password }) {
    return axios.post(LOGIN, { username, password }, {
        'Access-Control-Allow-Headers': '*'
    });
}

export function postRefreshTokenAPI({ refresh }) {
    return axios.post(REFRESH, { refresh }, {
        'Access-Control-Allow-Headers': '*'
    });
}