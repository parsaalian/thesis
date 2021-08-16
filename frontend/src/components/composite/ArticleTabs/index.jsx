import React from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import Title from '../../simple/Title';
import Markdown from '../../simple/Markdown';

function ArticleTabs({ articles }) {
    return (
        <Tabs defaultActiveKey={articles[0].href} className="mb-3">
            {articles.map(article => (
                <Tab key={article.href} eventKey={article.href} title={article.title}>
                    <span>
                        By <Title>{article.author.toLowerCase()}</Title> | 
                        Source: <a href={article.href} target="_blank" rel="noreferrer">Investopedia</a>
                    </span>
                    <Markdown body={article.body} />
                </Tab>
            ))}
        </Tabs>
    );
}

export default ArticleTabs;