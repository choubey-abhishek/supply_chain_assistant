import ChatBox from "../components/ChatBox";

export default function Assistant() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navbar - same as Dashboard */}
      <nav className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-blue-600 text-white rounded-xl flex items-center justify-center font-bold">SC</div>
            <h1 className="text-2xl font-bold text-gray-900">Supply Chain Assistant</h1>
          </div>
          <div className="flex gap-6 text-sm font-medium">
            <a href="/" className="text-gray-600 hover:text-gray-900">Dashboard</a>
            <a href="/assistant" className="text-blue-600 border-b-2 border-blue-600 pb-1">AI Assistant</a>
            <a href="/upload" className="text-gray-600 hover:text-gray-900">Upload CSV</a>
          </div>
        </div>
      </nav>

      <div className="max-w-4xl mx-auto px-6 py-8">
        <h2 className="text-3xl font-semibold text-gray-900 mb-6">AI Supply Chain Assistant</h2>
        <ChatBox />
      </div>
    </div>
  );
}
