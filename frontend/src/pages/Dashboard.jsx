import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navbar */}
      <nav className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-blue-600 text-white rounded-xl flex items-center justify-center font-bold">SC</div>
            <h1 className="text-2xl font-bold text-gray-900">Supply Chain Assistant</h1>
          </div>
          <div className="flex gap-6 text-sm font-medium">
            <Link to="/" className="text-blue-600 border-b-2 border-blue-600 pb-1">Dashboard</Link>
            <Link to="/assistant" className="text-gray-600 hover:text-gray-900">AI Assistant</Link>
            <Link to="/upload" className="text-gray-600 hover:text-gray-900">Upload CSV</Link>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-6 py-8">
        <h2 className="text-3xl font-semibold text-gray-900 mb-2">Supply Chain Dashboard</h2>
        <p className="text-gray-600 mb-8">Real-time inventory overview • Last updated just now</p>

        {/* Metrics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
          <div className="bg-white rounded-2xl shadow-sm p-6 border border-gray-100">
            <p className="text-sm text-gray-500">Total SKUs</p>
            <p className="text-4xl font-bold text-gray-900 mt-2">1,284</p>
            <p className="text-green-600 text-sm mt-4 flex items-center gap-1">↑ 12% from last month</p>
          </div>
          <div className="bg-white rounded-2xl shadow-sm p-6 border border-gray-100">
            <p className="text-sm text-gray-500">Low Stock Items</p>
            <p className="text-4xl font-bold text-orange-600 mt-2">47</p>
            <p className="text-orange-600 text-sm mt-4">Needs immediate reorder</p>
          </div>
          <div className="bg-white rounded-2xl shadow-sm p-6 border border-gray-100">
            <p className="text-sm text-gray-500">Total Inventory Value</p>
            <p className="text-4xl font-bold text-gray-900 mt-2">₹8.4 Cr</p>
            <p className="text-green-600 text-sm mt-4">↑ 5% from last week</p>
          </div>
          <div className="bg-white rounded-2xl shadow-sm p-6 border border-gray-100">
            <p className="text-sm text-gray-500">Avg Lead Time</p>
            <p className="text-4xl font-bold text-gray-900 mt-2">14 days</p>
            <p className="text-red-600 text-sm mt-4">↓ 2 days improved</p>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="flex gap-4 mb-10">
          <Link
            to="/upload"
            className="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-medium flex items-center gap-2"
          >
            📤 Upload New CSV
          </Link>
          <Link
            to="/assistant"
            className="px-6 py-3 bg-white border border-gray-300 hover:border-gray-400 rounded-xl font-medium flex items-center gap-2"
          >
            🤖 Ask AI Assistant
          </Link>
        </div>

        {/* Sample Inventory Table */}
        <div className="bg-white rounded-2xl shadow-sm overflow-hidden">
          <div className="px-6 py-4 border-b flex justify-between items-center">
            <h3 className="font-semibold">Recent Inventory</h3>
            <Link to="/upload" className="text-blue-600 text-sm hover:underline">View full inventory →</Link>
          </div>
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500">ITEM</th>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500">STOCK</th>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500">STATUS</th>
                <th className="text-left px-6 py-3 text-xs font-medium text-gray-500">VALUE</th>
              </tr>
            </thead>
            <tbody className="divide-y">
              <tr className="hover:bg-gray-50">
                <td className="px-6 py-4">Wireless Earbuds Pro</td>
                <td className="px-6 py-4 font-medium text-green-600">142</td>
                <td className="px-6 py-4"><span className="px-3 py-1 text-xs bg-green-100 text-green-700 rounded-full">In Stock</span></td>
                <td className="px-6 py-4">₹3,84,000</td>
              </tr>
              <tr className="hover:bg-gray-50">
                <td className="px-6 py-4">Smart Watch Ultra</td>
                <td className="px-6 py-4 font-medium text-orange-600">23</td>
                <td className="px-6 py-4"><span className="px-3 py-1 text-xs bg-orange-100 text-orange-700 rounded-full">Low Stock</span></td>
                <td className="px-6 py-4">₹1,92,000</td>
              </tr>
              <tr className="hover:bg-gray-50">
                <td className="px-6 py-4">Laptop Stand Ergonomic</td>
                <td className="px-6 py-4 font-medium text-green-600">89</td>
                <td className="px-6 py-4"><span className="px-3 py-1 text-xs bg-green-100 text-green-700 rounded-full">In Stock</span></td>
                <td className="px-6 py-4">₹1,24,000</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
