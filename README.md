# WebApp Template FastAPI, React.js

```
This is a template for a Webapp using React.js for the UI and FastAPI as the server.
```

# Getting Started

1.  Install UI dependencies and build app
2.  Install server dependencies
3.  Start the server

- In a browser navigate to
  - `localhost:8000/api/health` this should return `{ "status": "healthy" }`
  - `localhost:8000/` this should return a web page that says `Home`

```
# run from ui/ directory
npm install
npm run build
```

```
# run from server/ directory
pip install -r requirements.txt
```

```
# run from server/ directory
uvicorn main:app --reload
```
