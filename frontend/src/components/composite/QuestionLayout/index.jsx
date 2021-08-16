import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function QuestionLayout({ children }) {
    return (
        <Container fluid>
            <Row className="justify-content-center my-3">
                <Col xs={11} sm={11} md={6} lg={6}>
                    {children}
                </Col>
            </Row>
        </Container>
    )
}

export default QuestionLayout;