import React, {useContext} from 'react';
import {Context} from '../App.jsx';

function UpdateContextExample(){
    const [context, updateContext] = useContext(Context);

    return <button onClick={()=>{ updateContext({hello:"updated context"}) }}>update context..</button>
}

export default UpdateContextExample