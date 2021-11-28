import React, {useState, useEffect} from 'react'

function UseEffectExample(){
    
    const [value, updateValue] = useState('default');

    useEffect( async() => {
        let result = await fetch('');
        let data = await result.json();
        console.log(data);
    },[]);

    return <>
        <h1>{value}</h1>
    </>
}

export default UseEffectExample