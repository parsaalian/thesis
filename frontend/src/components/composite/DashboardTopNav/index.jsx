import React from 'react';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import Avatar from '../../simple/Avatar';

function DashboardTopNav({ page }) {
    return (
        <Navbar className="w-100 px-0 mx-0 py-4">
            <Container fluid>
                <Navbar.Brand>{page}</Navbar.Brand>
                <Nav className="me-auto"></Nav>
                <Nav>
                    <Form className="d-flex">
                        <FormControl
                            type="search"
                            placeholder="Search"
                            className="mx-3"
                            aria-label="Search"
                        />
                    </Form>
                    <Avatar size={40} />
                    <NavDropdown>
                        <NavDropdown.Item href="/dashboard/profile">Profile</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="/logout">Logout</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Container>
        </Navbar>
    )
}

export default DashboardTopNav;