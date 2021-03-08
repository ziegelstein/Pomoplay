import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App container">
      <header>
        <h2>Pomoplay</h2>
      </header>
      <div class="pomo"></div>
      <div class="game">
        <div class="timer">Minutes Left</div>
        <div class="buttons">
          <button>Action</button>
          <button>Pause</button>
          <button>Reset</button>
        </div>
      </div>
      <menu>
        <p>Menu</p>
      </menu>
      <footer>© 2021 - Jemar & Cippy - Made because of 💜 </footer>
    </div>
  );
}

export default App;
