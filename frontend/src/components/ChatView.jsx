import React, {useContext, useState} from 'react';
import {Context} from '../App.jsx';

function ChatView(){
    const [context, updateContext] = useContext(Context);
    const [inputValue, inputValueUpdateMethod] = useState('...');

    const updateInputValue = (element) => {
        inputValueUpdateMethod(element.value)
        console.log(element.disabled)
    }

    return (
        <div>
            <h2>Chat box</h2>
            <p>Conversation:<em>{context.hello}</em></p>
            <input value={inputValue} onChange={(e)=>updateInputValue(e.target)}/>
            <button onClick={()=>{ updateContext({hello:inputValue}) }}>update context..</button>
        </div>
    )
}

export default ChatView