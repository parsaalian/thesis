import React, { Component } from 'react';
import { connect } from 'react-redux';
import LoginForm from '../../components/composite/LoginForm';
import { loginAction } from '../../redux/actions/account';

class LoginPage extends Component {
    render() {
        const { login } = this.props;
        return (
            <>
                <LoginForm onSubmit={login} />
            </>
        )
    }
}

function mapStateToProps(state) {
    return {}
}

function mapDispatchToProps(dispatch) {
    return {
        login: (username, password) => dispatch(loginAction({ username, password }))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(LoginPage);