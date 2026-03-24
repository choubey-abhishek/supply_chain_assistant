import { useState } from "react";
import { sendMessage } from "../services/api";

export default function ChatBox() {
  const [msg, setMsg] = useState("");
  const [res, setRes] = useState("");

  const send = async () => {
    try {
      const r = await sendMessage(msg);
      setRes(r.data.response);
    } catch (err) {
      console.error(err);
      setRes("Error: Unable to get response");
    }
  };

  return (
    <div>
      <input
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        placeholder="Ask supply chain question"
      />

      <button onClick={send}>Ask</button>

      <p>{res}</p>
    </div>
  );
}
