import React, {useContext} from 'react';
import {Context} from '../App.jsx';

function ReadContextExample(){
    const [context, updateContext] = useContext(Context);

    return <div>
        <h2>{context.hello}</h2>
    </div>
}

export default ReadContextExample