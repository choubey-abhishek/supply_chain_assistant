import {BrowserRouter,Routes,Route} from "react-router-dom"
import Dashboard from "./pages/Dashboard"
import Assistant from "./pages/Assistant"
import Upload from "./pages/Upload"

function App(){

return(

<BrowserRouter>

<Routes>

<Route path="/" element={<Dashboard/>}/>
<Route path="/assistant" element={<Assistant/>}/>
<Route path="/upload" element={<Upload/>}/>

</Routes>

</BrowserRouter>

)

}

export default App
