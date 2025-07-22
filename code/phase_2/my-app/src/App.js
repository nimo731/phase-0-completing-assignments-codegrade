
import './App.css';
import Contact from './Pages/Contact';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="App">
     
        <h1 className='text-4xl'>Welcome to My React App</h1>
       <Navbar/>
       <Contact/>
    </div>
  );
}

export default App;
