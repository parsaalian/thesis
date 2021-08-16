import React from 'react';
import MDX from '@mdx-js/runtime'

const components = {
    img: (props) => <img width="100%" {...props} />
}

function Markdown({ body }) {
    return <MDX components={components} children={body} />;
}

export default Markdown;