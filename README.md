## **React & Flask Data Exchange Setup 🚀**

This project demonstrates how to send data from a **React frontend** to a **Flask backend** and receive a response.

---

## **📌 Features**

✅ Send JSON data from React to Flask  
✅ Receive processed data from Flask in React  
✅ Uses `axios` for HTTP requests  
✅ CORS enabled for seamless communication

---

## **📂 Project Structure**

```
react-flask-app/      # Root folder
│
├── backend/          # Flask Backend
│   ├── server.py     # Flask application
│   ├── venv/         # Virtual environment (optional)
│
├── frontend/         # React Frontend
│   ├── src/
│   │   ├── SendData.js  # React component to send data
│   │   ├── App.js       # Main React component
│   ├── package.json     # React dependencies
```

---

## **🛠️ Setup Instructions**

### **1️⃣ Install and Set Up the Backend (Flask)**

#### **🔹 Step 1: Create and Activate Virtual Environment**

```bash
python -m venv venv
```

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

#### **🔹 Step 2: Install Dependencies**

```bash
pip install flask flask-cors
```

#### **🔹 Step 3: Create `server.py`**

Create a file `server.py` and paste:

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

@app.route('/send-data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received data:", data)
    response_data = {"message": "Data received successfully", "received": data}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
```

#### **🔹 Step 4: Run Flask Server**

```bash
python server.py
```

Flask will start at **http://127.0.0.1:5000**.

---

### **2️⃣ Install and Set Up the Frontend (React)**

#### **🔹 Step 1: Create React App**

```bash
npx create-react-app react-flask-app
cd react-flask-app
```

#### **🔹 Step 2: Install Axios**

```bash
npm install axios
```

#### **🔹 Step 3: Create `SendData.js`**

Inside `src/`, create `SendData.js` and paste:

```jsx
import React, { useState } from "react";
import axios from "axios";

const SendData = () => {
  const [response, setResponse] = useState(null);

  const sendDataToFlask = async () => {
    try {
      const data = { name: "Aayush", message: "Hello from React!" };
      const res = await axios.post("http://127.0.0.1:5000/send-data", data);
      setResponse(res.data);
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  return (
    <div>
      <h2>Send Data to Flask</h2>
      <button onClick={sendDataToFlask}>Send Data</button>
      {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
    </div>
  );
};

export default SendData;
```

#### **🔹 Step 4: Modify `App.js`**

Replace `src/App.js` with:

```jsx
import React from "react";
import SendData from "./SendData";

function App() {
  return (
    <div>
      <h1>React & Flask Integration</h1>
      <SendData />
    </div>
  );
}

export default App;
```

#### **🔹 Step 5: Start React App**

```bash
npm start
```

React will start at **http://localhost:3000**.

---

## **🚀 How to Test**

1️⃣ Open **http://localhost:3000/** in a browser.  
2️⃣ Click the **"Send Data"** button.  
3️⃣ Check the Flask server logs to see the received data.  
4️⃣ React will display the response from Flask.

---

## **🎯 Summary**

✅ **Flask backend** runs at `http://127.0.0.1:5000`  
✅ **React frontend** runs at `http://localhost:3000`  
✅ **React sends data to Flask, Flask processes it, and sends a response back**

---

## **🔧 Future Enhancements**

- ✅ Add authentication (JWT)
- ✅ Connect Flask to a database (SQLite/PostgreSQL)
- ✅ Deploy Flask on **Render** and React on **Vercel**

🚀 **Happy Coding!** 🎉
