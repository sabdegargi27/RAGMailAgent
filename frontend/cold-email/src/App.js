import './App.css';
import { useState } from 'react';

const App = () => {
  const [url, setUrl] = useState("");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const sendEmail = async (event) => {
    event.preventDefault()
    setLoading(true)
    const res = await fetch("http://127.0.0.1:8000?url=" + url)
    const data = await res.json()
    for (const item of data.message) {
      console.log(item)
      setOutput(item)
    }
    setLoading(false)
  }
  const copyToClipboard = () => {
    navigator.clipboard.writeText(output)
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>Cold Email</h1>
        <div className="input-container">
          <div className="input-with-button">
            <input className="input" type="text" placeholder="Enter the job posting link" value={url} onChange={(e) => setUrl(e.target.value)} />
            <button className={`input-button ${loading || !url ? "disabled" : ""}`} onClick={sendEmail} disabled={loading || !url}>{loading ? "Sending..." : "Send Email"}</button>
          </div>
        </div>
        {output && (
          <div className="output-container" style={{ whiteSpace: 'pre-line' }}>
            {output}
            <button className="copy-button" onClick={copyToClipboard}>Copy</button>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
