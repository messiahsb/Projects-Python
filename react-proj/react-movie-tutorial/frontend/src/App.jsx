import { Routes, Route } from 'react-router-dom';
import './App.css'
import Home from './pages/Home';
import Favorites from './pages/favorites';
import NavBar from './components/NavBar';

// component
function App() {
  return (
    <div>
      <NavBar />
      <main className='main-content'>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/favorites' element={<Favorites />} />
        </Routes>
      </main>
    </div>
  )
}


export default App
