import React from 'react';
import QuestionChoices from '../../../containers/QuestionChoices';

function Question({ question }) {
    const { answer, choices, prompt } = question;
    console.log(question);
    return (
        <>
            <h3 className="mt-3">{prompt}</h3>
            <QuestionChoices choices={choices} answer={answer} />
        </>
    );
}

export default Question;