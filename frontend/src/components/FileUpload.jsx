import { useState } from "react"
import { uploadFile } from "../services/api"

export default function FileUpload() {
  const [file, setFile] = useState(null)
  const [result, setResult] = useState(null)

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a CSV file")
      return
    }

    try {
      const res = await uploadFile(file)
      setResult(res.data.summary)
      alert("Upload successful!")
    } catch (err) {
      console.error(err)
      alert("Upload failed. Check console.")
    }
  }

  return (
    <div className="p-8 bg-white rounded-3xl shadow">
      <input 
        type="file" 
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
        className="block w-full text-sm text-gray-500 file:mr-4 file:py-3 file:px-6 file:rounded-xl file:border-0 file:text-sm file:font-medium file:bg-blue-600 file:text-white hover:file:bg-blue-700"
      />
      <button 
        onClick={handleUpload}
        className="mt-6 w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-2xl font-medium"
      >
        Upload CSV
      </button>

      {result && (
        <pre className="mt-8 bg-gray-100 p-6 rounded-2xl text-sm overflow-auto">
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  )
}
