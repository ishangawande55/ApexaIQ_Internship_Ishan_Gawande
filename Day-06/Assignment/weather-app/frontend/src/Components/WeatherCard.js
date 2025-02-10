import React from "react";
import { WiHumidity, WiStrongWind, WiThermometer, WiDaySunny } from "react-icons/wi";

const WeatherCard = ({ weather }) => {
  return (
    <div className="weather-card">
      <h2>{weather.location}, {weather.country}</h2>
      <img src={weather.weather.icon} alt={weather.weather.description} />
      <p>{weather.weather.description}</p>

      <h1>{weather.temperature.current}°C</h1>
      <p>Feels like: {weather.temperature.feels_like}°C</p>

      <div className="details">
        <p><WiThermometer /> Min: {weather.temperature.min}°C | Max: {weather.temperature.max}°C</p>
        <p><WiHumidity /> Humidity: {weather.humidity}%</p>
        <p><WiStrongWind /> Wind: {weather.wind.speed} m/s, Gust: {weather.wind.gust} m/s</p>
        <p>Direction: {weather.wind.direction}°</p>
        <p>Cloudiness: {weather.cloudiness}</p>
        <p>Visibility: {weather.visibility}</p>
      </div>
    </div>
  );
};

export default WeatherCard;