import { isNull } from 'lodash';
import React, { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Choice from '../../components/simple/Choice';

function QuestionChoices({ choices, answer, onAnswer }) {
    const [clicked, setClicked] = useState(null);

    const onChoiceClick = (choice) => {
        if (isNull(clicked)) {
            setClicked(choice);
            onAnswer(choice);
        }
    }

    const getChoiceBackground = (choice) => {
        if (isNull(clicked)) {
            return 'light';
        }
        if (choice === answer) {
            return 'success';
        }
        if (clicked === choice) {
            return 'danger';
        }
        return 'light';
    }

    return (
        <Container fluid>
            <Row>
                {choices.map((choice, i) => {
                    return (
                        <Col key={i} xs={12} sm={12} md={6} lg={6} className="mt-4">
                            <div onClick={() => onChoiceClick(i)}>
                                <Choice bg={getChoiceBackground(i)}>
                                    {choice}
                                </Choice>
                            </div>
                        </Col>
                    );
                })}
            </Row>
        </Container>
    )
}

export default QuestionChoices;