import React, {useState} from 'react'

function UseStateExample(){
    
    let text = "Some text"
    const [headline, headlineChanger] = useState('My headline')

    return <>
        <h1>{headline}</h1>
        <p>{text}</p>
        <button onClick={()=>headlineChanger("Your headline")}>Click me</button>
    </>
}

export default UseStateExample