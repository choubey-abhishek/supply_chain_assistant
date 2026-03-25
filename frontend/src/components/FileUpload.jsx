import { useState } from "react"
import { uploadFile } from "../services/api"

export default function FileUpload() {
  const [file, setFile] = useState(null)
  const [result, setResult] = useState(null)

  const handleUpload = async () => {
    if (!file) return alert("Please select a file")

    try {
      const res = await uploadFile(file)
      setResult(res.data.summary)
    } catch (err) {
      console.error(err)
      alert("Upload failed")
    }
  }

  return (
    <div className="p-6 bg-white rounded-2xl shadow">
      <input 
        type="file" 
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button 
        onClick={handleUpload}
        className="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700"
      >
        Upload CSV
      </button>

      {result && (
        <pre className="mt-6 bg-gray-100 p-4 rounded-xl text-sm overflow-auto">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  )
}
