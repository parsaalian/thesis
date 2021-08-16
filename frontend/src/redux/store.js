import thunk from 'redux-thunk';
import logger from 'redux-logger';
import { applyMiddleware, createStore } from 'redux';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import reducers from './reducers';
import storeInitialState from './initialState';

function makeStore(initialState = storeInitialState) {
    const persistConfig = {
        key: 'root',
        storage,
    };

    const store = createStore(
        persistReducer(persistConfig, reducers),
        initialState,
        (process.env.NODE_ENV === 'development' ? applyMiddleware(thunk, logger) : applyMiddleware(thunk)),
    );

    store.__PERSISTOR = persistStore(store);

    return store;
}

export default makeStore;