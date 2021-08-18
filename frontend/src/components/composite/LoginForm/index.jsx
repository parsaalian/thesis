import React, { useRef } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button';
import Input from '../../../containers/Input';

function LoginForm({ onSubmit }) {
    const username = useRef(null);
    const password = useRef(null);

    const submit = () => {
        onSubmit(
            username.current.state.value,
            password.current.state.value,
        );
    };

    return (
        <Form>
            <Input type='text' placeholder='' label='Username' ref={username} />
            <Input type='password' placeholder='' label='Password' ref={password} />
            <Button variant="primary" onClick={submit}>
                Login
            </Button>
        </Form>
    );
}

export default LoginForm;