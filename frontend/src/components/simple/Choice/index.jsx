import React from 'react';
import styled from '@emotion/styled';
import Card from 'react-bootstrap/Card';

const HoverCard = styled(Card)({
    '&:hover': {
        cursor: 'pointer',
    }
});

function Choice({ bg, children }) {
    return (
        <HoverCard bg={bg} text={bg === 'light' ? 'dark' : 'white'} className="text-center">
            <Card.Body>
                <Card.Title>{children}</Card.Title>
            </Card.Body>
        </HoverCard>
    )
}

export default Choice;