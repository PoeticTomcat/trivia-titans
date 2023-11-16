import React, { useState } from "react";
import NavBar from "./NavBar";
import PlayButton from "./PlayButton";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <header className="app-header">
        <NavBar />
      </header>
      <div className="content-container">
        <h1>Trivia Titans</h1>
      </div>
      <div className="PlayButton">
        <PlayButton />
      </div>
    </>
  );
}

export default App;