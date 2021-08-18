import React from 'react';
import QuestionChoices from '../../../containers/QuestionChoices';

function Question({ question, onAnswer }) {
    const { answer, choices, prompt } = question;
    return (
        <>
            <h3 className="mt-3">{prompt}</h3>
            <QuestionChoices choices={choices} answer={answer} onAnswer={onAnswer} />
        </>
    );
}

export default Question;