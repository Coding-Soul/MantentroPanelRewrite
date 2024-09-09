import React from 'react';

function App() {
  return (
    <div className="h-screen bg-gray-900">
      <div className="flex flex-col justify-center items-center text-center h-full">
        <h1 className="text-7xl font-bold text-white mb-2">
          Welcome to
        </h1>
        <h1 className="text-5xl font-bold text-yellow-600 text">
          MantentroPanel
        </h1>
      </div>

      <div className="flex flex-col justify-center items-center mt-4 space-y-20 pb-40">
        <h1 className="text-yellow-600 text-5xl">Login</h1> 
        <button className="py-2 px-12 btn btn-primary">
          Dashboard
        </button>
      </div>
    </div>
  );
}

export default App;