from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.mm5_daymovingavg import get_ma5_data
from models.Candlestick import get_candle_body_data
from models.dailychange import get_daily_close_change
from models.Lowershadow import get_lower_shadow_data
from models.OHLC import get_ohlc_mean_data
from models.pricechange import get_price_change_data
from models.RSI import get_rsi_data
from models.volumechange import get_volume_change_data
from models.volatility import get_volatility_data
from models.EMA10 import get_ema10_data
from models.Uppershadow import get_upper_shadow_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/chart-data/{metric}")
def get_chart_data(metric: str):
    metric_function_map = {
        "MA5": get_ma5_data,
        "Candle Body Size": get_candle_body_data,
        "Daily Return": get_daily_close_change,
        "Lower Shadow Size": get_lower_shadow_data,
        "OHLC": get_ohlc_mean_data,
        "Price Change": get_price_change_data,
        "RSI": get_rsi_data,
        "Volume Change": get_volume_change_data,
        "Volatility": get_volatility_data,
        "EMA10": get_ema10_data,
        "Upper Shadow Size": get_upper_shadow_data,
    }

    if metric not in metric_function_map:
        return {"error": f"Invalid metric: {metric}"}

    data = metric_function_map[metric]()  # Call the appropriate function
    print(f"Returning data for metric: {metric}\n", data)  # Terminal log
    return data  # FastAPI automatically returns this as JSON