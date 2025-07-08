import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <div className="w-full min-h-screen flex flex-col items-center justify-center p-5">
    <App />
    </div>
  </StrictMode>,
)
