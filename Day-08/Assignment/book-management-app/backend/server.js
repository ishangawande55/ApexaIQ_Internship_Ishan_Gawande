require("dotenv").config(); // Load environment variables first
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const bookRoutes = require("./routes/bookRoutes");

const app = express();

// Middleware
app.use(cors({ origin: "*" }));
app.use(express.json()); 

// Test Route
app.get("/", (req, res) => {
    res.send("Welcome to the Book Management API 📚");
});

// Use Book Routes
app.use("/api", bookRoutes);

// MongoDB Connection
const PORT = process.env.PORT || 8000;
const MONGO_URI = process.env.MONGO_URI || "mongodb://mongo:27017/books"; 

mongoose
    .connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true }) 
    .then(() => {
        console.log("MongoDB Connected ✅");
        app.listen(PORT, () => console.log(`Server running on port ${PORT} 🚀`));
    })
    .catch((err) => console.error("MongoDB Connection Error ❌", err));