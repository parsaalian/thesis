import React from 'react';
import Avatar, { genConfig } from 'react-nice-avatar'

const randomElement = (array) => array[Math.floor(Math.random() * array.length)];

function AvatarGenerator({ size }) {
    const config = genConfig({
        sex: randomElement(['man', 'woman']),
        earSize: randomElement(['small', 'big']),
        hairSize: randomElement(['normal', 'thick', 'mohawk', 'womanLong', 'womanShort']),
        hairStyleMan: randomElement(['normal', 'thick', 'mohawk']),
        hairStyleWoman: randomElement(['normal', 'womanLong', 'womanShort']),
        hatStyle: randomElement(['beanie','turban', 'none']),
        eyeStyle: randomElement(['circle', 'oval', 'smile']),
        glassesStyle: randomElement(['round', 'square', 'none']),
        noseStyle: randomElement(['short', 'long', 'round']),
        mouthStyle: randomElement(['laugh', 'smile', 'peace']),
        shirtStyle: randomElement(['hoody', 'short', 'polo']),
        eyeBrowStyle: randomElement(['up', 'upWoman']),
    });

    console.log(config);

    return <Avatar style={{ width: size, height: size }} {...config} />
}

export default AvatarGenerator;