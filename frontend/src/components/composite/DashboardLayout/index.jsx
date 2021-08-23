import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function DashboardLayout({ navbar, children }) {
    return (
        <Container fluid>
            <Row>
                <Col md={3} lg={2} style={{ padding: 0 }}>
                    {navbar}
                </Col>
                <Col md="auto" lg="auto">
                    {children}
                </Col>
            </Row>
        </Container>
    )
}

export default DashboardLayout;