import React from 'react';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';
import Avatar from '../../simple/Avatar';

function DashboardTopNav({ page }) {
    return (
        <Navbar className="w-100 px-0 mx-0 py-4">
            <Container fluid>
                <Navbar.Brand href="#home">{page}</Navbar.Brand>
                <Nav className="me-auto"></Nav>
                <Nav>
                    <Avatar />
                    <NavDropdown>
                        <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                        <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                        <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Container>
        </Navbar>
    )
}

export default DashboardTopNav;