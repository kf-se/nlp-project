import React, {useState} from 'react'

function FormInputWrapperMethod(){

    const [inputValue, inputValueUpdateMethod] = useState('default-value');

    const updateInputValue = (element) => {
        inputValueUpdateMethod(element.value)
        console.log(element.disabled)
    }

    return (
        <div>
            <h2>Form input</h2>
            <input value={inputValue} onChange={(e)=>updateInputValue(e.target)}/>
            <p>Current value from input <em>{inputValue}</em></p>
        </div>
    )
}

export default FormInputWrapperMethod