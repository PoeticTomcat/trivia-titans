import React from "react";
import NavBar from "./NavBar";
import PlayButton from "./components/PlayButton";
import useToken from "@galvanize-inc/jwtdown-for-react";
import "./Home.css";
import { useEffect, useState } from "react";

function Home() {
  const { token } = useToken();
  const [user, setUser] = useState("");
  const [storageUser, setStorageUser] = useState();

  const getUser = async (e) => {
    if (token !== null) {
      const getToken = await fetch(
        `${import.meta.env.VITE_REACT_APP_API_HOST}/token`,
        {
          credentials: "include",
        }
      );
      if (getToken.ok) {
        const data = await getToken.json();
        setUser(data.account);
        localStorage.setItem("user", JSON.stringify(data.account));
      }
    }
  };
  useEffect(() => {
    getUser();
    setStorageUser(JSON.parse(localStorage.getItem("user")));
  }, []);

  return (
    <>
      <header className="app-header"></header>
      <div>
        <h1 className="title">TRIVIA TITANS</h1>
      </div>
      {token && storageUser && (
        <div>
          <h2>Welcome, {storageUser.name} </h2>
        </div>
      )}
      <div className="PlayButton">
        <PlayButton />
      </div>
    </>
  );
}

export default Home;
