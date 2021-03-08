import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App container">
      <header>
        <h2>Pomoplay</h2>
      </header>
      <div className="pomo">
        <div className="time">Minutes Left</div>
        <button className="start">Action</button>
        <button className="stop">Pause</button>
        <button className="reset">Reset</button>
      </div>
      <div className="game">
        <p>ToDo</p>
      </div>
      <menu>
        <p>Menu</p>
      </menu>
      <footer>© 2021 - Jemar & Cippy - Made because of 💜 </footer>
    </div>
  );
}

export default App;
