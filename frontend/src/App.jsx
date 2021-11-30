import { useState, createContext} from 'react'

import {
  BrowserRouter as Router,
  Route,
  Routes,
  Link
} from "react-router-dom"

import ChatView from './components/ChatView.jsx';


// Create and export a global context we can use as store
export const Context = createContext();

function App() {

  const [contextVal, setContext] = useState({
    hello:"NaN"
  })

  function updateContext(updates){
    setContext({
      ...contextVal, 
      ...updates
    })
  }

  return (
      <Context.Provider value={[contextVal, updateContext]}>
        <Router>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/chat">Chat box</Link>
          </nav>
          <Routes>
            <Route path="/chat" element={<ChatView/>}/>
          </Routes>
        </Router>
      </Context.Provider>
  )
}

export default App
