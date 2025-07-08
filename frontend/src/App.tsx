import { useState } from 'react';
import './App.css';
import { Chart } from './chart';
import { Button } from './components/ui/button';

function App() {
  const [chart, setChart] = useState<string>('none');

  const handleChartChange = (type: string) => {
    setChart(type);
  };

  return (
    <div className="min-h-screen bg-black text-white p-6">
      {/* Header */}
      <div className="mb-6 text-center">
        <h1 className="text-4xl font-bold mb-2">Analytics Dashboard</h1>
        <p className="text-lg text-gray-400">SPY Stock</p>
      </div>

      {/* Button row */}
      <div className="overflow-x-auto whitespace-nowrap pb-4 mb-6">
        <div className="flex gap-3 w-max">
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Daily Return')}>Daily Return</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Price Change')}>Price Change</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Volatility')}>Volatility</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('MA5')}>MA5</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('EMA10')}>EMA10</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Volume Change')}>Volume Change</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('OHLC')}>OHLC</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Candle Body Size')}>Candle Body Size</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Upper Shadow Size')}>Upper Shadow Size</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('Lower Shadow Size')}>Lower Shadow Size</Button>
          <Button className="bg-white text-black hover:bg-gray-200" onClick={() => handleChartChange('RSI')}>RSI</Button>
        </div>
      </div>


      {/* Your chart component */}
      <Chart selectedChart={chart} />
    </div>
  );
}

export default App;