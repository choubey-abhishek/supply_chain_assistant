import {useState} from "react"
import API from "../services/api"

export default function ChatBox(){

const[msg,setMsg]=useState("")
const[res,setRes]=useState("")

const send=async()=>{

const r = await API.post("/chat",{message:msg})

setRes(r.data.response)

}

return(

<div>

<input
value={msg}
onChange={(e)=>setMsg(e.target.value)}
placeholder="Ask supply chain question"
/>

<button onClick={send}>Ask</button>

<p>{res}</p>

</div>

)

}
