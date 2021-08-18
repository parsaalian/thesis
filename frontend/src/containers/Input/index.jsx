import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'

class Input extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
        }
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
      event.preventDefault();
      this.setState({ value: event.target.value});
    }

    render() {
        const { value } = this.props;
        const { label, type, placeholder } = this.props;
        return (
            <Form.Group className="mb-3" controlId={label.replace(/\s/g, '_')}>
              <Form.Label>{label}</Form.Label>
              <Form.Control
                type={type}
                placeholder={placeholder}
                value={value}
                onChange={this.handleChange}
              />
            </Form.Group>
        );
    }
}

Input.defaultProps = {
  label: 'test',
  type: 'text',
  placeholder: 'test'
}

export default Input;