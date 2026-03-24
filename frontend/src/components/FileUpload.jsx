import {useState} from "react"
import API from "../services/api"

export default function FileUpload(){

const[file,setFile]=useState(null)
const[result,setResult]=useState(null)

const upload=async()=>{

const form=new FormData()
form.append("file",file)

const res = await API.post("/upload",form)

setResult(res.data.summary)

}

return(

<div>

<input type="file" onChange={(e)=>setFile(e.target.files[0])}/>

<button onClick={upload}>Upload</button>

<pre>{JSON.stringify(result,null,2)}</pre>

</div>

)

}
