import React, { useState } from "react";
import axios from "axios";
import WeatherCard from "../Components/WeatherCard";
import "../styles.css";

const Home = () => {
  const [lat, setLat] = useState("");
  const [lon, setLon] = useState("");
  const [weatherData, setWeatherData] = useState(null);
  const [error, setError] = useState("");

  const fetchWeather = async () => {
    setError("");  // Clear any previous errors
  
    if (!lat || !lon) {
      setError("Please enter valid latitude and longitude!");
      return;
    }
  
    try {
      const response = await axios.get(`http://127.0.0.1:8000/weather`, {
        params: { lat: parseFloat(lat), lon: parseFloat(lon) }  // Ensure lat/lon are numbers
      });
  
      setWeatherData(response.data);
    } catch (err) {
      console.error("API Error:", err);
      setError("Location not found or API error");
    }
  };

  return (
    <div className="container">
      <h1>Weather App</h1>
      <input
        type="text"
        placeholder="Enter Latitude..."
        value={lat}
        onChange={(e) => setLat(e.target.value)}
      />
      <input
        type="text"
        placeholder="Enter Longitude..."
        value={lon}
        onChange={(e) => setLon(e.target.value)}
      />
      <button onClick={fetchWeather}>Get Weather</button>

      {error && <p className="error">{error}</p>}
      {weatherData && <WeatherCard weather={weatherData} />}
    </div>
  );
};

export default Home;