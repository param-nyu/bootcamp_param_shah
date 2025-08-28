## Flask API

A minimal Flask API serves the trained SOXX mimic model:

- **POST `/predict`** – JSON features → model prediction  
- **GET `/predict/<input1>`**, **`/<input1>/<input2>`** – single/two-feature predictions  
- **GET `/plot`** – simple chart  

Demonstrates model persistence, endpoint exposure, error handling, and notebook-testable reproducibility.
