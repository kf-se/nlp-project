import { useState, createContext} from 'react'
import UseStateExample from './components/UseStateExample.jsx'
import UseEffectExample from './components/UseEffectExample.jsx'
import ReadContextExample from './components/ReadContextExample.jsx';
import UpdateContextExample from './components/UpdateContextExample.jsx';
import FormInputWrapperMethod from './components/FormInputWrapperMethod.jsx';

// Create and export a global context we can use as store
export const Context = createContext();

function App() {

  const [contextVal, setContext] = useState({
    hello: "default context data"
  })

  function updateContext(updates){
    setContext({
      ...contextVal, 
      ...updates
    })
  }

  return (
      <Context.Provider value={[contextVal, updateContext]}>
      <div> 
        <FormInputWrapperMethod/>
        <ReadContextExample/>
        <UpdateContextExample/>
        <UseEffectExample/>
        <UseStateExample/>
      </div>
      </Context.Provider>
  )
}

export default App
